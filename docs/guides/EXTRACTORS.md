# Extractors Guide

## Contract

Each extractor should return a DataFrame compatible with BigQuery loading expectations.

## Registration

Register new extractors in `src/extractors/__init__.py` under `EXTRACTORS`.
