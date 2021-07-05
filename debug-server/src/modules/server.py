import socket
import datetime

HOST = '127.0.0.1'
PORT = 2222

def reply(data):
    return '%s;%s$' % (len(data), data)

def log(txt):
    ds = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M:%S')
    print '[Debug-Server] %s: %s' % (ds, txt)

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))

    while True:
        s.listen(1)
        client, address = s.accept()

        log('Connection from %s:%s' % (address[0], address[1]))

        client.send(b'%s' % (reply('Waiting for inputs...')))

        while True:
            message = (client.recv(1024)).decode('utf-8')

            log('Received > %s' % (message))

            if message.upper() == 'QUIT':
                break

            err = False

            try:
                try:
                    res = eval(message, globals())
                    client.send(b'%s' % (reply(str(res))))
                except SyntaxError:
                    err = True
                
                if err:
                    client.send(b'%s' % (reply('Success')))
                    exec message in globals()

            except Exception, e:
                import traceback
                client.send(b'%s' % (reply(str(traceback.format_exc()))))

        client.send(b'%s' % (reply('Disconnecting...')))
        log('Connection from %s:%s closed' % (address[0], address[1]))

        client.close()
        s.close()

def run_server():
    log('Starting server...')
    try:
        while True:
            start()
    except:
        log('* Crashed *')
        import traceback
        traceback.print_exc()
    log('Server stopped!')

run = True

if run:
    log('Starting thread...')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.setDaemon(True)
        thread.start()

        log('Thread started')
    except:
        import traceback
        traceback.print_exc()