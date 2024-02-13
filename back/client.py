import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Define event handlers
@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('data')
def on_data(data):
    print('Received data from server:', data)

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Connect to server
sio.connect('http://localhost:5001')

# Send data to server
sio.emit('data', {'message': 'Hello from client'})

# Keep the client running
try:
    while True:
        pass
except KeyboardInterrupt:
    # Disconnect on Ctrl+C
    sio.disconnect()
