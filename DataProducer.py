import json
import random
from datetime import datetime, timedelta
from azure.eventhub import EventHubProducerClient, EventData




def generate_sample_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "timestamp": str(datetime.now()),  # Current timestamp
            "temperature": round(random.uniform(20.0, 30.0), 2),  # Random temperature (between 20.0 and 30.0)
            "humidity": round(random.uniform(40.0, 70.0), 2),  # Random humidity (between 40.0 and 70.0)
        }
        data.append(record)
    return data

if __name__ == "__main__":
    num_records_to_generate = 10  # You can adjust this as needed
    sample_data = generate_sample_data(num_records_to_generate)

    # Save the data to a JSON file
    with open("sample_data.json", "w") as json_file:
        json.dump(sample_data, json_file, indent=2)

    print(f"{num_records_to_generate} records generated and saved to sample_data.json.")

connection_str = "Endpoint=sb://mynewvm1.servicebus.windows.net/;SharedAccessKeyName=New_key;SharedAccessKey=rTmzn7wW3PHRmhMNeZaNDFnZh6ZtmS9v6+AEhNf0BDk="
eventhub_name = "eventhub_m"
producer = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

def send_data_to_eventhub(data):
    event_data_batch = producer.create_batch()
    for record in data:
        event_data_batch.add(EventData(json.dumps(record)))
    producer.send_batch(event_data_batch)

# Example usage:
sample_data = generate_sample_data(num_records_to_generate)  # Assuming you already have sample data
send_data_to_eventhub(sample_data)