#!/usr/bin/env python3
"""Analyse data."""
import requests
import io
import zipfile
insert_school = __import__('9-insert_school').insert_school
from pymongo import MongoClient


url = 'https://s3.amazonaws.com/\
intranet-projects-files/\
holbertonschool-webstack/411/dump.zip'
response = requests.get(url)
if response.status_code == 200:
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        extracted_files = {
                          name: zip_ref.read(name)
                          for name in zip_ref.namelist()
                          }
client = MongoClient("mongodb://localhost:27017")
data = client.temp
collect = data.downloads
insert_school(collect, **extracted_files)
gets = data.count_documents({"get" : True})
posts = data.count_documents({"get" : True})
puts = data.count_documents({"put" : True})
patchs = data.count_documents({"patch" : True})
deletions = data.count_documents({"delete" : True})
all_d = data.count_documents({})
print(f'{all_d} logs\
            Methods\
                method GET: {gets}\
                method POST: {posts}\
                method PUT : {puts}\
                method PATCH: {patchs}\
                method DELETE: {deletions}')
