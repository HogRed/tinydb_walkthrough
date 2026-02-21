# TinyDB Python CRUD Project

Inspired by tutorial on [Real Python](https://realpython.com/tinydb-python/?utm_source=notification_summary&utm_medium=email&utm_campaign=2026-02-16).

## Overview

This project demonstrates how to implement a NoSQL, document-oriented database using TinyDB. It provides a lightweight way to perform standard CRUD (Create, Read, Update, Delete) operations without the complex setup or configuration requirements of larger database systems.

Written entirely in Python, this project uses no external dependencies beyond TinyDB and pprint, making it incredibly easy to embed directly into any existing Python application. Data is persisted efficiently in JSON format and managed through a clean, Pythonic API.

## Features

- Zero Configuration: No external database servers or complex setups required.
- Embedded & Lightweight: Runs seamlessly inside your Python project.
- JSON Storage: Persists documents in an easy-to-read JSON format.
- Full CRUD Support: 
  -  Create: Generate databases, tables, and insert new documents.
  -  Read: Query and view documents based on diverse criteria using various search techniques.
  -  Update: Modify single or multiple documents dynamically.
  -  Delete: Remove specific documents or drop entire tables.

## Installation

Since TinyDB is written purely in Python, installation is quick and simple:

```python
pip install tinydb
```

## Advantages & Limitations

Advantages:
- Incredibly easy to learn and implement.
- Highly portable; the database is just a JSON file.
- 100% Pythonic API that feels natural to write.

Limitations:
- Not designed for high-concurrency environments (e.g., multiple processes writing simultaneously).
- Not suitable for massive datasets, as the entire database resides in memory during operations.