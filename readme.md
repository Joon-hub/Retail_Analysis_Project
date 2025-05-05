
## Retail Analysis Project

### Overview

The **Retail Analysis Project** is a hands-on exploration of building a clean, modular `PySpark` application for processing large retail-transaction datasets. Rather than working in a single monolithic notebook, the logic is divided into reusable Python modules, wired together in `application_main.py`, and designed with best practices in configuration, logging, and testing.

### Details
This repository demonstrates a modular approach to building and testing PySpark workflows, emphasizing:

* **Clean Code Structure**
  Organize ETL logic into reusable modules under `lib/` and drive the pipeline from `application_main.py`.

* **Flexible Configuration**
  Externalize Spark settings and logging through files in `configs/`, so you can tweak performance and verbosity without touching code.

* **Robust Testing**
  Leverage PyTest to validate transformations:

  * **Fixtures** in `conftest.py` for shared resources (e.g., SparkSession).
  * **Parameterized tests** and **markers** in `test_retail_project.py` to cover diverse scenarios.
  * Centralized settings in `pytest.ini`.

* **Reproducible Environment**
  Manage Python dependencies with Pipenv (`Pipfile`/`Pipfile.lock`) for consistent builds across machines.

### Project Structure

```plaintext
Retail_Analysis_Project/
├── __pycache__/           # Compiled bytecode
├── configs/               # Spark & Log4j configuration
├── data/                  # Sample datasets
├── lib/                   # Core ETL modules
├── metastore_db/          # Derby metastore files
├── Pipfile                # Pipenv dependency list
├── Pipfile.lock           # Locked dependency versions
├── application_main.py    # Entry point for Spark pipeline
├── conftest.py            # PyTest fixtures
├── derby.log              # Metastore logging
├── notes.txt              # Developer notes & todos
├── pytest.ini             # PyTest configuration
├── readme.md             
└── test_retail_project.py # Test suite (parameterized & marked)
```

### Getting Started

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

### What I Learned

- **PySpark setup & configuration**: how to bootstrap a `SparkSession`, tune memory settings, and manage Spark properties via external config files.
- **Modular code design**: the benefits of splitting a data pipeline into `loaders`, `transforms`, and `analytics` modules—each testable and reusable.
- **Automated testing with pytest**: writing fixtures that spin up a local Spark session, using markers to group slow vs. fast tests, and parameterizing inputs to cover edge cases.
- **Structured logging**: integrating `Log4j` into PySpark code to capture `INFO` / `WARN` / `ERROR` messages, which is critical for debugging jobs running on a cluster.
- **Environment management with pipenv**: keeping project dependencies isolated and reproducible, with `Pipfile` / `Pipfile.lock` to share exact versions.
