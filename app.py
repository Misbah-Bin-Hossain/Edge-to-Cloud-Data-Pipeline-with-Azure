import os
from flask import Flask, render_template, jsonify
import pyodbc
import json
import traceback
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# SQL Server connection parameters from environment variables
sql_server = os.getenv('SQL_SERVER')
sql_database = os.getenv('SQL_DATABASE')
sql_username = os.getenv('SQL_USERNAME')
sql_password = os.getenv('SQL_PASSWORD')
sql_driver = os.getenv('SQL_DRIVER')

# Create a connection to the SQL Server using SQL Server authentication
def create_sql_connection():
    try:
        connection_string = (
            f"DRIVER={sql_driver};"
            f"SERVER=tcp:{sql_server},1433;"
            f"DATABASE={sql_database};"
            f"UID={sql_username};"
            f"PWD={sql_password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
        )
        
        print("Connecting to SQL Server...")
        conn = pyodbc.connect(connection_string)
        print("Connected successfully!")
        return conn
    except Exception as e:
        print(f"Error creating SQL connection: {str(e)}")
        print(traceback.format_exc())
        return None

# Function to get data from SQL Server
def get_data_from_sql():
    try:
        conn = create_sql_connection()
        if conn is None:
            raise Exception("Failed to create database connection")
        
        cursor = conn.cursor()
        query = "SELECT TOP 20 timestamp, temperature, humidity FROM [dbo].[SensorData] ORDER BY timestamp DESC"
        print(f"Executing query: {query}")
        cursor.execute(query)
        
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        print(f"Retrieved {len(data)} rows of data")
        return data
    except Exception as e:
        print(f"Database error: {str(e)}")
        print(traceback.format_exc())
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    print("Fetching data...")
    data = get_data_from_sql()
    if data is None:
        error_message = "Failed to fetch data from database. Check server logs for details."
        print(error_message)
        return jsonify({"error": error_message}), 500
    print(f"Returning {len(data)} rows of data")
    return jsonify(data)

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)