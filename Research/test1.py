# Import gcloud
from google.cloud import storage
import os
# location of json file created
credential_path = "c:\example.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
# Enable Storage
client = storage.Client()

# Reference an existing bucket.
bucket = client.get_bucket('exampleprog-69f69.appspot.com')

#image has to be the same location as python script
# Upload a local file to a new file to be created in your bucket.
zebraBlob = bucket.blob('donk.jpg')
zebraBlob.upload_from_filename(filename='donk.jpg')

# Download a file from your bucket.
#giraffeBlob = bucket.get_blob('giraffe.jpg')
#giraffeBlob.download_as_string()
#In line client = storage.Client()
