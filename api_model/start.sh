#!/bin/bash
sleep 2
python write_cleaned_data_to_db.py
gunicorn --bind 0.0.0.0:5000 api_model:app