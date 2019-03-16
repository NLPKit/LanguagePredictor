#!/bin/sh

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"text": "Que pasa?"}' \
  http://localhost:8080/api/v1/language/predict
