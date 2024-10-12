from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_ENDPOINT')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable overhead tracking for SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)
