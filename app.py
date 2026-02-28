from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database Configuration
db_config = {
    'host': 'book-rds.cinsoscgioqa.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'SuperSecretPass123',
    'database': 'prod'
    }
