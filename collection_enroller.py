import requests
from databse_retriever import readBLOB

"""Make sure that visionbox is running"""

size_db = 5 #set the size of your database (number of identities you'll need to enroll)I'm hardcoding the size since this is an example


url = "http://0.0.0.0:8080/v1/enroll"


for x in range(size_db - 1):
    #This function will take the ID of the identity and store the picture in a chosen location named by it's ID.
    #To make it simple I'm just assuming my identities are named 0, 1, 2, 3, 4 (To make the recurssion easier)
    #Note that the ID can be the user name or an UUID. The loop integration will vary on those cases
    readBLOB(x,"/chosen/folder/location/to/store/the/picture"+x)

#Now all the pictures are named and stored in a desired folder

for x in range(size_db - 1):
    payload = {'namespace': 'Your_name_space',
               'collection_id': 'Your_collection_ID',
               'label': x}
    files = [
      ('image', (x + '.jpeg', open('/chosen/folder/location/to/store/the/picture/' + x + '.jpeg', 'rb'), 'image/jpeg'))
    ]
    headers = {
      'Accept': '*/*'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #This is to make sure that the identity was enrolled succesfully
    print(response.text)


