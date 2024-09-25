import json
import random
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

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

    # Replace with your actual values
    connection_str = "Endpoint=sb://mynewvm1.servicebus.windows.net/;SharedAccessKeyName=New_key;SharedAccessKey=rTmzn7wW3PHRmhMNeZaNDFnZh6ZtmS9v6+AEhNf0BDk="
    eventhub_name = "eventhub_m"

    producer = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

    try:
        with producer:
            event_data_batch = producer.create_batch()
            for record in sample_data:
                event_data_batch.add(EventData(json.dumps(record)))
            producer.send_batch(event_data_batch)
            print(f"{num_records_to_generate} records sent to Event Hub.")
    except Exception as e:
        print(f"Error sending data: {str(e)}")
