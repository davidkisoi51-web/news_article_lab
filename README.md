# NLP Text Analyzer

A lightweight Python command-line utility designed to parse and analyze text content from news articles. Built as a practical implementation of fundamental Natural Language Processing (NLP) techniques, this script handles basic string manipulation, regex tokenization, and text metric processing.

## Features

*   **Targeted Word Counting:** Finds precise matches for specific keywords using boundary-safe regex matching.
*   **Frequency Analysis:** Tracks and extracts the most frequently used word in a text body.
*   **Text Metrics:** Automatically calculates average word length (returned as a float).
*   **Structural Parsing:** Counts both distinct paragraphs and sentence boundaries (`.`, `!`, `?`).
*   **Interactive CLI:** Includes a built-in terminal menu to run a full analysis suite or query individual metrics.

## Requirements

*   Python 3.8+
*   No external dependencies required (uses built-in standard libraries `re` and `collections`).

## Setup & Usage

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.
3. Run the script using Python:

```bash
python pythonAssessment.py