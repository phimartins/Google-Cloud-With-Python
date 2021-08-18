import os
from google.cloud import storage
from googleapiclient import discovery
from googleapiclient import errors

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\phili\Downloads\projeto-automacao-iam-0fd267ec73b3.json'
os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

storage_client = storage.Client()
# Making authenticated request to return the list of buckets
buckets = list(storage_client.list_buckets())
for bucket in buckets:
 print(bucket)
 
project = "projeto-automacao-iam"
zone="us-east1-b"
compute = discovery.build('compute', 'v1')
instances = compute.instances().list(project=project, zone=zone).execute()
projeto = instances['id']
vms = instances['items']
for i in range(len(vms)):
 print('Instance ID: '+vms[i]['id']+' - '+'Instance Name: '+vms[i]['name']+' - '+'Created At: '+vms[i]['creationTim
estamp'])

