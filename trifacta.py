# Trifacta List Lobs
import requests
import base64

def list_jobs(baseurl = "http://partnerdemo.trifacta.net:3005", user_id = 'demo@trifacta.com', password = 'demo'):
    url = baseurl + '/v3/jobGroups'
    authorization = 'Basic ' + base64.b64encode(str.encode(user_id + ':' + password)).decode('utf-8')
    headers = {
        'Authorization': authorization,
        'Cache-Control': "no-cache"
        }
    return requests.request("GET", url, headers=headers).text

# print(list_jobs())

# Trifacta Run Job
def run_job(wrangled_dataset_id = 5184, baseurl = 'http://partnerdemo.trifacta.net:3005', user_id = 'demo@trifacta.com', password = 'demo'):
    url = baseurl + "/v3/jobGroups"
    authorization = 'Basic ' + base64.b64encode(str.encode(user_id + ':' + password)).decode('utf-8')
    payload = "{\n  \"wrangledDataset\": {\n\"id\": " + str(wrangled_dataset_id) + " }\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': authorization,
        'Cache-Control': "no-cache"
        }
    return requests.request("POST", url, data=payload, headers=headers).text

# print(run_job(wrangled_dataset_id = 5184))

# Trifacta Get Job Status
def get_job_status(job_group_id, baseurl = 'http://partnerdemo.trifacta.net:3005', user_id = 'demo@trifacta.com', password = 'demo'):
    url = baseurl + "/v3/jobGroups/" + str(job_group_id) + "/status"
    authorization = 'Basic ' + base64.b64encode(str.encode(user_id + ':' + password)).decode('utf-8')
    headers = {
        'Authorization': authorization,
        'Cache-Control': "no-cache"
        }
    return requests.request("GET", url, headers=headers).text

# print(get_job_status(1501))

