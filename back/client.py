import socketio
import time

# Create a Socket.IO client
sio = socketio.Client()

# Define event handlers
@sio.on('connect')
def on_connect(data=None):
    print('Connected to server : ', data)

@sio.on('data')
def on_data(data=None):
    print('Received data from server: ', data)

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Keep the client running
try:
    # Connect to server
    sio.connect('http://localhost:5001')

    while True:
        # Send data to server
        sio.emit('data', {'message': 'Hello from client'})
        # Let server some time for rest...
        time.sleep(1)

except KeyboardInterrupt:
    # Disconnect on Ctrl+C
    sio.disconnect()