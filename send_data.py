import os
import json
import random
from datetime import datetime
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy
from dotenv import load_dotenv

load_dotenv()

def generate_sample_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "timestamp": str(datetime.now()),
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2),
        }
        data.append(record)
    return data

if __name__ == "__main__":
    num_records_to_generate = 10  # You can adjust this as needed
    sample_data = generate_sample_data(num_records_to_generate)

    # Use environment variables
    connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.environ.get('AZURE_STORAGE_QUEUE_NAME')

    if not connection_string or not queue_name:
        raise ValueError("Please set the AZURE_STORAGE_CONNECTION_STRING and AZURE_STORAGE_QUEUE_NAME environment variables.")

    queue_client = QueueClient.from_connection_string(
        connection_string, 
        queue_name,
        message_encode_policy=BinaryBase64EncodePolicy()
    )

    try:
        for record in sample_data:
            message = json.dumps(record).encode('utf-8')  # Convert to bytes
            queue_client.send_message(message)
        print(f"{num_records_to_generate} records sent to Azure Storage Queue.")
    except Exception as e:
        print(f"Error sending data: {str(e)}")