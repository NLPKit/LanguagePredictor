# Language Predictor [![CircleCI](https://circleci.com/gh/NLPKit/LanguagePredictor.svg?style=svg)](https://circleci.com/gh/NLPKit/LanguagePredictor)

Language Predictor is a lightweight server for detecting the language of arbitrary text. For development information, see the [Contributor Guide](./CONTRIBUTING.md).

## API

The main endpoint exposed by Language Predictor is an HTTP POST request at `/api/v1/language/predict`. The endpoint expects a JSON request with a `"text"` key. The text key should contain text in an undetermined language.

Consider the following curl command for testing the local server:

```
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"text": "Encantado de conocerte."}' \
  http://localhost:8080/api/v1/language/predict
```

This will return a response like the following:

```json
{
  "prediction": {
    "language":"spa",
    "confidence":0.995512843132019
  }
}
```

## Running Locally

To run the server locally, you must specify the fasttext model file:

```
python language_predictor.py --model ./data/tatoeba/langdetect.ftz
```

By default the server will bind to http://127.0.0.1:8080.

## Prometheus Metrics

By default, Language Predictor serves a metrics endpoint in the Prometheus format at `/metrics`. To see what metrics are available, you can run the following curl command locally:

```
curl http://localhost:8080/metrics
```

## Getting Help

For questions, feature requests, bug reports, etc, please file a [GitHub Issue](https://github.com/NLPKit/LanguagePredictor/issues/new).
