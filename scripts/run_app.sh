#!/bin/bash

# Install the project in editable/developement mode
pip install -e .
uvicorn main:app --reload --port 8000 --host 0.0.0.0 

# to run the app: sh scripts/run_app.sh
