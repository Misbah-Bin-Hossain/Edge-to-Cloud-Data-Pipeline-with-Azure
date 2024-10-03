import os
from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API is running"

@app.route('/api/data')
def get_data():
    conn_str = os.environ['AZURE_SQL_CONNECTION_STRING']
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 100 timestamp, temperature, humidity FROM your_table ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    data = [{'timestamp': str(row.timestamp), 'temperature': row.temperature, 'humidity': row.humidity} for row in rows]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
