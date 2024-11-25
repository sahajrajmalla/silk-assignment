# Makefile for Silk Assignment

.PHONY: setup run clean

setup:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/python main.py
	venv/bin/streamlit run streamlit/app.py

clean:
	rm -rf venv
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

help:
	@echo "Available commands:"
	@echo "  setup   - Set up the virtual environment and install dependencies."
	@echo "  run     - Run the main pipeline and Streamlit dashboard."
	@echo "  clean   - Remove all temporary files and the virtual environment."
	@echo "  help    - Show this help message."
