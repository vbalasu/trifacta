# # trifacta
# 
# 1. Connect to a remote Trifacta instance
# 2. Run jobs
# 3. Send and receive files

import requests, json, time, datetime, io
import boto3, ipywidgets as widgets, ijson, simplejson
from pywebhdfs.webhdfs import PyWebHdfsClient
from urllib.parse import urlparse
import pandas as pd
class Client:
    def __init__(self, trifacta_base_url, trifacta_token):
        """Example: t = Trifacta('https://partnerdemo.trifacta.net', 'MY_TRIFACTA_TOKEN')"""
        self.trifacta_base_url = trifacta_base_url
        self.trifacta_token = trifacta_token
    def dataexchange_list_datasets(self, region_name='us-east-1'):
        self.dx = boto3.client('dataexchange', region_name=region_name)
        self.datasets = {i['Name']:i['Id'] for i in self.dx.list_data_sets(Origin='ENTITLED')['DataSets']}
        return self.datasets
    def dataexchange_choose_dataset(self, region_name='us-east-1'):
        self.dataexchange_list_datasets(region_name=region_name)
        self.d =  widgets.RadioButtons(options=self.datasets.keys(), description='Dataset: ', layout=widgets.Layout(width='100%'))
        return self.d
    def dataexchange_list_revisions(self, region_name='us-east-1'):
        self.revisions = {i['CreatedAt'].isoformat():i['Id'] for i in self.dx.list_data_set_revisions(DataSetId=self.datasets[self.d.value])['Revisions']}
        return self.revisions
    def dataexchange_choose_revision(self, region_name='us-east-1'):
        self.dataexchange_list_revisions(region_name=region_name)
        self.r = widgets.RadioButtons(options=self.revisions.keys(), description='Revision: ', layout=widgets.Layout(width='100%'))
        return self.r
    def dataexchange_runjob_download(self, bucket_name, region_name='us-east-1'):
        self.assets = [{'AssetId':i['Id'], 'Bucket': bucket_name, 'Key': i['Name']} for i in self.dx.list_revision_assets(DataSetId=self.datasets[self.d.value], RevisionId=self.revisions[self.r.value])['Assets']]
        self.createjob_response = self.dx.create_job(
            Details={
                'ExportAssetsToS3': {
                    'AssetDestinations': self.assets,
                    'DataSetId': self.datasets[self.d.value],
                    'RevisionId': self.revisions[self.r.value]
                }
            },
            Type='EXPORT_ASSETS_TO_S3'
        )
        self.startjob_response = self.dx.start_job(JobId=self.createjob_response['Id'])
        self.dx_job_id = self.createjob_response['Id']
        print('JobId '+self.dx_job_id+' started')
        import time
        status=self.dx.get_job(JobId=self.dx_job_id)['State']
        while status not in ['ERROR','COMPLETED','CANCELLED','TIMED_OUT']:
            print(status)
            time.sleep(5)
            status=self.dx.get_job(JobId=self.dx_job_id)['State']
        print(status)
        return True
    def dataexchange_runjob_status(self, job_id):
        return self.dx.get_job(JobId=job_id)['State']
    def json_to_jsonlines(self, input_json, output_jsonlines, array_element):
        f = open(input_json)
        out = open(output_jsonlines, 'w+')
        objects = ijson.items(f, array_element+'.item')
        for o in objects:
            out.write(simplejson.dumps(o)+'\n')
        out.close()
        f.close()
    def get_job_status(self, job_group_id):
        response = requests.get(self.trifacta_base_url + '/v4/jobGroups/{0}/status'.format(job_group_id), headers = {"Authorization": "Bearer "+self.trifacta_token})
        return json.loads(response.text)
    def run_job(self, wrangled_dataset_id):
        """Get the wrangled_dataset_id from your browser's URL when editing the recipe"""
        request_body = {"wrangledDataset": {"id": wrangled_dataset_id }}
        print('About to run job', flush=True)
        response = requests.post(self.trifacta_base_url + '/v4/jobGroups', headers = {"Authorization": "Bearer "+self.trifacta_token}, json=request_body)
        response_obj = json.loads(response.text)
        print(response_obj, flush=True)
        self.job_group_id = response_obj['id']
        job_status = self.get_job_status(self.job_group_id)
        while job_status != 'Complete':
            print(datetime.datetime.today(), job_status, flush=True)
            time.sleep(5)
            job_status = self.get_job_status(self.job_group_id)
        print(datetime.datetime.today(), job_status, flush=True)
        return True
    def get_file_contents(self, hdfs_path, user_name='trifacta', httpfs_port='14000'):
        hdfs = PyWebHdfsClient(host=urlparse(self.trifacta_base_url).netloc,port=httpfs_port, user_name=user_name)
        return hdfs.read_file(hdfs_path).decode('utf-8')
    def get_dataframe(self, hdfs_path_to_csv):
        csv_string = self.get_file_contents(hdfs_path_to_csv)
        return pd.read_csv(io.StringIO(csv_string))
    def put_file_contents(self, hdfs_path, file_contents, user_name='trifacta', httpfs_port='14000'):
        hdfs = PyWebHdfsClient(host=urlparse(self.trifacta_base_url).netloc,port=httpfs_port, user_name=user_name)
        hdfs.create_file(hdfs_path, file_contents, overwrite=True)
        return True

