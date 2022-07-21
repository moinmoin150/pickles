import streamlit as st
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
import pickle

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

def download_blob_into_memory(bucket_name, blob_name):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()
    return contents

# df = pickle.loads(download_blob_into_memory("voluble_transcription", "pickles/Replies to 1325516879033741319.csv"))
content = download_blob_into_memory("voluble_transcription", "pickles/Replies to 1325516879033741319.csv")
for line in content.strip().split("\n"):
    name, pet = line.split(",")[:2]
    st.write(f"{name} has a :{pet}:")
# st.dataframe(df.head())

