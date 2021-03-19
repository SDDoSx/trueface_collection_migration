import requests
from databse_retriever import readBLOB

url = "http://0.0.0.0:8080/v1/enroll"

payload={'namespace': 'client123',
'collection_id': 'office_developers',
'label': 'Manuel'}
files=[
  ('image',('manuel.jpeg',open('/home/mark/Trueface/visionbox/manuel.jpeg','rb'),'image/jpeg'))
]
headers = {
  'Accept': '*/*'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

