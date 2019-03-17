# Contributor Guide

The contributor guide has the following sections:

- [Setup](#setup)
- [Test](#test)
- [Run](#run)

## Setup

To get your development environment setup, you first must clone the source repository:

```
git clone git@github.com:NLPKit/LanguageDetector.git
```

To build and test the code, it is required to have the following minimal toolset installed:

- [Python (3.7)](https://www.python.org/downloads/)

You will also need the `fastText` Python library which must be built from source:

```
git clone git@github.com:facebookresearch/fastText.git
cd fastText
python setup.py install
```

To build the models, you may also want the `fasttext` binary:

```
git clone git@github.com:facebookresearch/fastText.git
cd fastText
make
cp ./fasttext /usr/local/bin/
```

## Test

From the root of the repository, you can run the following to run all of the tests:

```bash
python -m unittest discover ./test "test_*.py"
```

### Running A Full CI Build Locally

The CircleCI configuration includes a number of lint and test steps. If you'd like to run a complete, representative CI build locally, download the `circleci` CLI tool. See the [official installation instructions](https://circleci.com/docs/2.0/local-cli/#installing-the-circleci-local-cli-on-macos-and-linux-distros) for download information.

Once you have the tool installed in your path, run the following from the root of the repository:

```bash
circleci build
```

## Run

First, `cd` to the root of the repository. All commands assume you're running them from the root of the repository.

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Use the following command to run the local development server:

```bash
python language_predictor.py --model ./data/tatoeba/langdetect.ftz
```

The web application should now be available on http://localhost:8080.
