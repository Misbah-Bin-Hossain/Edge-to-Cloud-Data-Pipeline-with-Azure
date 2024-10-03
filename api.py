from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/api/data')
def get_data():
    conn_str = os.getenv('AZURE_SQL_CONNECTION_STRING')
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 100 timestamp, temperature, humidity FROM your_table ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    data = [{'timestamp': str(row.timestamp), 'temperature': row.temperature, 'humidity': row.humidity} for row in rows]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
