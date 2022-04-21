import socket

HOST = '127.0.0.1'
PORT = 2222

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

while not connected:
    try:
        socket.connect((HOST, PORT))
        connected = True
    except Exception as e:
        pass

print 'Connected to %s:%s' % (HOST, PORT)

def parse(msg):
    msg = msg.split(';')
    return { "size": int(msg[0]), "data": msg[1].split('$')[0] }

while True:
    message = (socket.recv(1024)).decode('utf-8')

    if not message:
        break

    size = parse(message)["size"]
    message = parse(message)["data"]

    print 'Received > %s' % (message)

    if message == 'Disconnecting...':
        break

    request = raw_input('Request > ')

    socket.send(b'%s' % (request))

socket.close()
print 'Connection with %s:%s closed' % (HOST, PORT)
