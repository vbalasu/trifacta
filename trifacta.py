
# coding: utf-8

# # trifacta
# 
# 1. Connect to a remote Trifacta instance
# 2. Run jobs
# 3. Send and receive files

# In[1]:


#!pip install pywebhdfs


# In[2]:


import requests, json, time, datetime, io
from pywebhdfs.webhdfs import PyWebHdfsClient
from urllib.parse import urlparse
import pandas as pd
class Trifacta:
    def __init__(self, trifacta_base_url, user_id, password):
        """Example: t = Trifacta('https://partnerdemo.trifacta.net', 'guest_user', 'guest_password')"""
        self.trifacta_base_url = trifacta_base_url
        self.user_id = user_id
        self.password = password
    def get_job_status(self, job_group_id):
        response = requests.get(self.trifacta_base_url + '/v3/jobGroups/{0}/status'.format(job_group_id), auth=('admin@trifacta.local', 'Tr1f@ct@1!'))
        return json.loads(response.text)
    def run_job(self, wrangled_dataset_id):
        """Get the wrangled_dataset_id from your browser's URL when editing the recipe"""
        request_body = {"wrangledDataset": {"id": wrangled_dataset_id }}
        print('About to run job', flush=True)
        response = requests.post(self.trifacta_base_url + '/v3/jobGroups', auth=(self.user_id, self.password), json=request_body)
        response_obj = json.loads(response.text)
        print(response_obj, flush=True)
        self.job_group_id = response_obj['jobgroupId']
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

