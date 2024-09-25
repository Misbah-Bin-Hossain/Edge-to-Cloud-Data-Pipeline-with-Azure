import pyodbc
import json
from azure.eventhub import EventHubConsumerClient
from datetime import datetime

# SQL Server connection parameters
sql_server = 'misbahserver.database.windows.net'
sql_database = 'My_database'
sql_username = 'misbahbin.hossain@yh.nackademin.se'  # Your Microsoft Entra admin email
sql_password = 'w3dgiEf6'  # Replace with your actual password
sql_driver = '{ODBC Driver 18 for SQL Server}'

# Create a connection to the SQL Server using Microsoft Entra password authentication
def create_sql_connection():
    try:
        # Create the connection string using Microsoft Entra Password Authentication
        connection_string = (
            f"DRIVER={sql_driver};"
            f"SERVER=tcp:{sql_server},1433;"
            f"DATABASE={sql_database};"
            f"UID={sql_username};"
            f"PWD={sql_password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
            f"Authentication=ActiveDirectoryPassword;"
        )
        
        print("Connecting to SQL Server...")
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"Error creating SQL connection: {str(e)}")
        raise

# Function to insert data into SQL Server
def insert_data_to_sql(timestamp, temperature, humidity):
    try:
        print(f"Inserting data to SQL Server: {timestamp}, {temperature}, {humidity}")
        conn = create_sql_connection()
        cursor = conn.cursor()

        # Define the insert query for your SensorData table
        insert_query = """
            INSERT INTO SensorData (timestamp, temperature, humidity)
            VALUES (?, ?, ?)
        """
        # Execute the query with the data
        cursor.execute(insert_query, (timestamp, temperature, humidity))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Successfully inserted data: {timestamp}, {temperature}, {humidity}")
    except Exception as e:
        print(f"Error inserting data into SQL: {str(e)}")

# Process the received event from Event Hub
def process_event(partition_context, event):
    try:
        print("Processing event...")
        event_data = event.body_as_str()
        json_data = json.loads(event_data)
        
        timestamp = datetime.strptime(json_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        temperature = json_data['temperature']
        humidity = json_data['humidity']

        insert_data_to_sql(timestamp, temperature, humidity)
        print(f"Processed event data: {json_data}")
    except Exception as e:
        print(f"Error processing event: {str(e)}")

# Event Hub connection parameters
eventhub_connection_str = "Endpoint=sb://mynewvm1.servicebus.windows.net/;SharedAccessKeyName=New_key;SharedAccessKey=rTmzn7wW3PHRmhMNeZaNDFnZh6ZtmS9v6+AEhNf0BDk="
eventhub_name = "eventhub_m"
consumer_group = "$Default"

# Create a consumer client with the required consumer group
consumer_client = EventHubConsumerClient.from_connection_string(
    eventhub_connection_str,
    eventhub_name=eventhub_name,
    consumer_group=consumer_group
)

# Start receiving events
try:
    print("Starting Event Hub listener...")
    with consumer_client:
        consumer_client.receive(process_event, starting_position="-1")  # Receive from the beginning of the stream
except Exception as e:
    print(f"Error receiving data: {str(e)}")
finally:
    print("Closing Event Hub consumer...")
    consumer_client.close()
