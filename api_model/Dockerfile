FROM python:3.10

RUN python -m pip install flask flask_restful gunicorn pandas numpy \
    joblib scikit-learn catboost sqlalchemy psycopg2

WORKDIR /app

ADD api_model.py api_model.py
ADD model_cbr.pkl model_cbr.pkl
ADD cleaned_data.csv cleaned_data.csv
ADD write_cleaned_data_to_db.py write_cleaned_data_to_db.py
ADD start.sh start.sh

RUN chmod +x start.sh

EXPOSE 5000

CMD ["/bin/bash", "./start.sh"]
#CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "api_model:app" ]

