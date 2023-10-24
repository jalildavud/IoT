from azure.iot.device import IoTHubDeviceClient, Message
import random
import time

# Device-specific connection details
connection_str = "HostName=project-1.azure-devices.net;DeviceId=deviceiot;SharedAccessKey=cjWjJM8s/uGBWRNN3NOrQXkj5jUytMrAqAIoTN0Lv+o="

# Create an IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(connection_str)

# Connect to the IoT Hub
client.connect()

while True:
    # Simulate sensor data (replace with your actual data)
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 60.0)

    # Create a message
    message = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')

    # Send the message
    client.send_message(message)
    print(f"Message sent: {message}")

    # Send data every 120 seconds (adjust as needed)
    time.sleep(120)
