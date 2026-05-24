#!/bin/bash
cd "$(dirname "$0")"
pip3 install pdfplumber pymupdf pytesseract pillow pdf2image openpyxl watchdog -q
python3 watcher.py
