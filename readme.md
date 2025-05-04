
# Retail Analysis Project

## Overview

The **Retail Analysis Project** is a hands-on exploration of building a clean, modular `PySpark` application for processing large retail-transaction datasets. Rather than working in a single monolithic notebook, the logic is divided into reusable Python modules, wired together in `application_main.py`, and designed with best practices in configuration, logging, and testing.

## Project Structure

```plaintext
Retail_Analysis_Project/
├── application_main.py      # Entry point: integrates all modules
├── lib/                     # Core data-processing modules
│   ├── loaders.py           # Functions to read raw data into DataFrames
│   ├── transforms.py        # Data cleaning & feature-engineering logic
│   └── analytics.py         # Business-logic computations & aggregations
├── configs/                 # Configuration files (e.g., Spark settings)
├── data/                    # Sample input datasets (e.g., CSVs, Parquet)
├── conftest.py              # pytest fixtures for setting up Spark session
├── pytest.ini               # pytest configuration (markers, etc.)
├── test_retail_project.py   # Parameterized tests covering each module
├── notes.txt                # Environment & pipenv setup notes
└── Pipfile / Pipfile.lock   # pipenv dependency management
```

## Getting Started

1. **Install dependencies**  
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

2. **Launch your shell**  
   ```bash
   pipenv shell
   ```

3. **Run tests**  
   ```bash
   pytest
   ```

4. **Execute the pipeline**  
   ```bash
   pipenv run python application_main.py
   ```

## What I Learned

- **PySpark setup & configuration**: how to bootstrap a `SparkSession`, tune memory settings, and manage Spark properties via external config files.
- **Modular code design**: the benefits of splitting a data pipeline into `loaders`, `transforms`, and `analytics` modules—each testable and reusable.
- **Automated testing with pytest**: writing fixtures that spin up a local Spark session, using markers to group slow vs. fast tests, and parameterizing inputs to cover edge cases.
- **Structured logging**: integrating `Log4j` into PySpark code to capture `INFO` / `WARN` / `ERROR` messages, which is critical for debugging jobs running on a cluster.
- **Environment management with pipenv**: keeping project dependencies isolated and reproducible, with `Pipfile` / `Pipfile.lock` to share exact versions.
