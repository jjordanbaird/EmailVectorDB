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
    "dataType": ["text"]
  },
  {
    "name": "received_date",
    "description": "The date when the newsletter was received.",
    "dataType": ["date"]
  },
  {
    "name": "text",
    "description": "The text content from the newsletter.",
    "dataType": ["string"],
    "moduleConfig": {
        "text2vec-transformers": {
          "skip": True,
          "vectorizePropertyName": True
        }
      }
  },
  {
    "name": "embedding",
    "description": "The vector representation of text content from the newsletter",
    "dataType": ["text"]
  }
]
}
# add the schema
client.schema.create_class(newsletter_class_obj)

# # get the schema
# schema = client.schema.get()
# # print the schema
# print(json.dumps(schema, indent=4))
"""
{
    "classes": [
        {
            "class": "Newsletter",
            "description": "Newsletter class",
            "invertedIndexConfig": {
                "bm25": {
                    "b": 0.75,
                    "k1": 1.2
                },
                "cleanupIntervalSeconds": 60,
                "stopwords": {
                    "additions": null,
                    "preset": "en",
                    "removals": null
                }
            },
            "moduleConfig": {
                "text2vec-transformers": {
                    "poolingStrategy": "masked_mean",
                    "vectorizeClassName": true
                }
            },
            "properties": [
                {
                    "dataType": [
                        "text"
                    ],
                    "description": "The title or name of the newsletter.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": false,
                            "vectorizePropertyName": false
                        }
                    },
                    "name": "newsletter",
                    "tokenization": "word"
                },
                {
                    "dataType": [
                        "text"
                    ],
                    "description": "The email address or name of the sender.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": false,
                            "vectorizePropertyName": false
                        }
                    },
                    "name": "sender",
                    "tokenization": "word"
                },
                {
                    "dataType": [
                        "date"
                    ],
                    "description": "The date when the newsletter was received.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": false,
                            "vectorizePropertyName": false
                        }
                    },
                    "name": "received_date"
                },
                {
                    "dataType": [
                        "string"
                    ],
                    "description": "The text content from the newsletter.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": true,
                            "vectorizePropertyName": true
                        }
                    },
                    "name": "text",
                    "tokenization": "word"
                },
                {
                    "dataType": [
                        "text"
                    ],
                    "description": "The vector representation of text content from the newsletter",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": false,
                            "vectorizePropertyName": false
                        }
                    },
                    "name": "embedding",
                    "tokenization": "word"
                }
            ],
            "replicationConfig": {
                "factor": 1
            },
            "shardingConfig": {
                "virtualPerPhysical": 128,
                "desiredCount": 1,
                "actualCount": 1,
                "desiredVirtualCount": 128,
                "actualVirtualCount": 128,
                "key": "_id",
                "strategy": "hash",
                "function": "murmur3"
            },
            "vectorIndexConfig": {
                "skip": false,
                "cleanupIntervalSeconds": 300,
                "maxConnections": 64,
                "efConstruction": 128,
                "ef": -1,
                "dynamicEfMin": 100,
                "dynamicEfMax": 500,
                "dynamicEfFactor": 8,
                "vectorCacheMaxObjects": 1000000000000,
                "flatSearchCutoff": 40000,
                "distance": "cosine",
                "pq": {
                    "enabled": false,
                    "bitCompression": false,
                    "segments": 0,
                    "centroids": 256,
                    "encoder": {
                        "type": "kmeans",
                        "distribution": "log-normal"
                    }
                }
            },
            "vectorIndexType": "hnsw",
            "vectorizer": "text2vec-transformers"
        }
    ]
}
"""