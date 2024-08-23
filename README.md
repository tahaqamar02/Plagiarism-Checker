# Plagiarism Checker

## Overview

This Python project provides a tool to measure the similarity between two text documents using **TF-IDF Vectorization** and **Cosine Similarity**. It supports both `.txt` and `.docx` file formats and features a simple graphical user interface (GUI) for file selection.

## Features

- **Supports Multiple Formats**: Compare `.txt` and `.docx` files.
- **TF-IDF Vectorization**: Converts text to numerical vectors based on term frequency and inverse document frequency.
- **Cosine Similarity**: Computes the similarity score between the two text vectors.
- **User-Friendly Interface**: Select files using a graphical interface with `tkinter`.

## Installation

### Prerequisites

Ensure you have Python 3.x installed. You will also need to install the following libraries:

- `scikit-learn` for machine learning tools
- `python-docx` for reading `.docx` files
- `tkinter` for the GUI

You can install the required libraries using pip:

```bash
pip install scikit-learn python-docx
