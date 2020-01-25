# Scholar API

Still in development. Zeros guarantee for anything.

Testing on python 3.6~3.8

![Build Status](https://travis-ci.org/AtomScott/scholar-api.svg?branch=master)

[![Coverage Status](https://coveralls.io/repos/github/AtomScott/scholar-api/badge.svg?branch=master)](https://coveralls.io/github/AtomScott/scholar-api?branch=master)

## Install via pip

```
pip install git+https://github.com/AtomScott/scholar-api.git
```

## Easy run

```bash
acasearch --query 'Attention is all you need' --out 'out' --num 5
```
This should output a json file @ ./out/6785239.json. The contents are something like:

```json
{
    "referencesFrom": [
        {
            "articleId": 100128869,
            "authors": [
                {
                    "id": 43571357,
                    "name": "Yifu Liu"
                },
                {
                    "id": 50562182,
                    "name": "Chenfeng Xu"
                },
                {
                    "id": 3736337,
                    "name": "Zhihong Chen"
                }
            ],
            "authorsCount": 0,
            "citationsCount": 0,
            "title": "Deep Dual-Stream Network with Scale Context Selection Attention Module for Semantic Segmentation",
            "year": 2020
        },
        {

```

Results are still very bad..

## Arguments

optional arguments:

-  -h, --help            show this help message and exit
-  --bibtex_path BIBTEX_PATH  Path to .bib file
-  --query QUERY         title of paper
-  --out OUT             path to output results
-  --verbose             Call for debug run
-  --num NUM
