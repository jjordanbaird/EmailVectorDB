import weaviate
import json

client = weaviate.Client("http://localhost:8080")


newsletter_class_obj = {
"class": "Newsletter",
"description": "Newsletter class",
"vectorizer": "text2vec-transformers",
"properties": [
  {
    "name": "newsletter",
    "description": "The title or name of the newsletter.",
    "dataType": ["text"]
  },
  {
    "name": "sender",
    "description": "The email address or name of the sender.",
    "dataType": ["text"], 
    "moduleConfig": {
        "text2vec-transformers": {
          "skip": True,
          "vectorizePropertyName": False
        }
      }
  },
  {
    "name": "header",
    "description": "The header of the section of the newsletter.",
    "dataType": ["text"]
  },
  {
    "name": "received_date",
    "description": "The date when the newsletter was received.",
    "dataType": ["date"]
  },
  {
    "name": "links",
    "description": "The links in the newsletter.",
    "dataType": ["string[]"],
    "moduleConfig": {
        "text2vec-transformers": {
          "skip": True,
          "vectorizePropertyName": False
        }
      }
  },
  {
    "name": "text_content",
    "description": "The text content from the newsletter.",
    "dataType": ["string"],
    "moduleConfig": {
        "text2vec-transformers": {
          "skip": False,
          "vectorizePropertyName": True
        }
      }
  },
  {
    "name": "email_id",
    "description": "ID of email.",
    "dataType": ["string"],
    "moduleConfig": {
        "text2vec-transformers": {
          "skip": True,
          "vectorizePropertyName": False
        }
      }
  }
]
}


# add the schema
client.schema.delete_class('Newsletter')
client.schema.create_class(newsletter_class_obj)
