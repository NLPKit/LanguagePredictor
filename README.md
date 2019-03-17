# Language Predictor [![CircleCI](https://circleci.com/gh/NLPKit/LanguagePredictor.svg?style=svg)](https://circleci.com/gh/NLPKit/LanguagePredictor)

Language Predictor is a lightweight server for detecting the language of arbitrary text. For development information, see the [Contributor Guide](./CONTRIBUTING.md).

## API

The main endpoint exposed by Language Predictor is an HTTP POST request at `/api/v1/language/predict`. The endpoint expects a JSON request with a `"text"` key. The text key should contain text in an undetermined language.

Consider the following curl command:

```
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"text": "Encantado de conocerte."}' \
  http://localhost:8080/api/v1/language/predict
```
