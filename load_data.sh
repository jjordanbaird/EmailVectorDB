#!/bin/bash

# pulls/parses email
python main.py

# create weaviate newsletter schema
python tldr/newsletter_schema.py

# load data into weaviate
python tldr/weaviate_load.py
