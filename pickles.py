import streamlit as st
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
import pickle

export GOOGLE_APPLICATION_CREDENTIALS="google_crendentials.json"

storage_client = storage.Client()

@st.experimental_memo
def download_blob_into_memory(bucket_name, blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()
    return contents

df = pickle.loads(download_blob_into_memory("voluble_transcription", "pickles/tweets_df.pkl"))
st.dataframe(df.head())

