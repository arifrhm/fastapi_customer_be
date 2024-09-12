#!/bin/bash

# Find and remove all __pycache__ directories and .pyc files
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

echo "Python bytecode cache cleared."
