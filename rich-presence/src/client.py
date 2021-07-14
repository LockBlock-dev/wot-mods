from pypresence import Presence
import socket
import time
import ast

HOST = '127.0.0.1'
PORT = 7777

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

while not connected:
    try:
        socket.connect((HOST, PORT))
        connected = True
    except Exception as e:
        pass
    time.sleep(2)

socket.send(b'CLIENT READY')
print('Connected to the rich presence')

client_id = '860799978749427712'
RPC = Presence(client_id)
RPC.connect()
timestamp = time.time()
updated = 0

def parse(msg):
    msg = msg.split(';')
    return { "size": int(msg[0]), "data": msg[1].split('$')[0] }

while True:
    message = (socket.recv(1024)).decode('utf-8')

    if not message:
        break

    size = parse(message)["size"]
    message = parse(message)["data"]

    if message == "END":
        break

    message = ast.literal_eval(message)

    rp = { "details": "Waiting for game", "state": "Waiting for game", "timestamp": time.time(), "version": "Waiting for game" }

    for key in message:
        if message[key]:
            rp[key] = message[key]

    rp["version"] = rp["version"].split(' ')[0]

    if time.time() - updated >= 15:
        print(RPC.update(
            details = rp["details"],
            state = rp["state"],
            large_image = "logo",
            large_text = rp["version"],
            start = timestamp
        ))

        updated = time.time()

        print('Rich presence updated')

socket.close()
print('Connection with the rich presence closed')
