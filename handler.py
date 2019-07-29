import os
import json
import logging
import copy
import random
import mysql.connector as sql
import requests
import numpy as np
import hashlib
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

user = os.environ['DATABASE_USER']
password = os.environ['DATABASE_PASSWORD']
host = os.environ['DATABASE_HOST']
name = os.environ['DATABASE_NAME']
# google_api_key = os.environ['GOOGLE_API_KEY']

def hello(event, context):
    print("ingreso final")
    #logger.info(user+" "+password+" "+host+" "+database_name)
    try:
        #conn = sql.connect(user="pulsedb", password="asdf1234", host="pulsedbid.cquegzdtu9b8.us-east-1.rds.amazonaws.com", database="pulsedbinst")
        conn = sql.connect(user=user, password=password, host=host, database=name)
        logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

        conn.close()
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")


    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
