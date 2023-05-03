import weaviate
import os
import json
import logging

logging.basicConfig(level=logging.INFO)

client = weaviate.Client("http://localhost:8080")

data_path = os.path.abspath(os.path.join(os.getcwd(), 'data', 'tldr_records.json'))
with open(data_path, 'r') as f:
    data = json.load(f)

with client.batch as batch:
    batch.batch_size=100
    # Batch import all Records
    print("loading records")
    for i, d in enumerate(data):
        properties = {
            "newsletter": "TLDR Newsletter",
            "sender": d["from"],
            "header": d["title"],
            "received_date": d["date"],
            "links": d["links"],
            "text_content": d["description"],
            "email_id": d["id"]
        }
        # this next thing produces logs
        client.batch.add_data_object(properties, "Newsletter")


