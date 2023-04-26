#/bin/bash
curl localhost:9090/vectors/ -H 'Content-Type: application/json' -d '{"text": "foo bar"}'