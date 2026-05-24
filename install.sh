#!/bin/bash
echo "Installing PackingList Text Extractor..."
brew install tesseract poppler
git clone https://github.com/Karlpogi11/PackingList-Text-Extractor.git ~/Desktop/PackingList-Text-Extractor
echo "Done! To start, run:"
echo "  cd ~/Desktop/PackingList-Text-Extractor && ./run.sh"
