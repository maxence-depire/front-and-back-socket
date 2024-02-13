import websocket

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://localhost:5000", origin="client.com")
ws.send("Hello, Server")
print(ws.recv())
ws.close()