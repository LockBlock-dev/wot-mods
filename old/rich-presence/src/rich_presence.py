def reply(data):
    return '%s;%s$' % (len(data), data)

def log(txt):
    ds = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M:%S')
    print '[Rich-Presence] %s: %s' % (ds, txt)

def rich_presence(client, tanksDB):
    import time

    #enter the garage
    
    import helpers
    from Account import PlayerAccount

    def new_Account_onBecomePlayer(self):

        old_Account_onBecomePlayer(self)

        version = helpers.getClientVersion()

        rp = { "details": "Hanging around", "state": "In the garage", "timestamp": time.time(), "version": version }

        client.send(b'%s' % (reply(rp)))

    old_Account_onBecomePlayer = PlayerAccount.onBecomePlayer
    PlayerAccount.onBecomePlayer = new_Account_onBecomePlayer


    #enter a battle

    import BigWorld
    import helpers
    from Avatar import PlayerAvatar

    def new_onEnterWorld(self, prereqs):

        old_onEnterWorld(self, prereqs)

        tankName = tanksDB[BigWorld.player().vehicle.typeDescriptor.name]['shortName']

        version = helpers.getClientVersion()
        
        rp = { "details": "Playing with %s" % (tankName), "state": "In a battle", "timestamp": time.time(), "version": version }
        
        client.send(b'%s' % (reply(rp)))

    old_onEnterWorld = PlayerAvatar.onEnterWorld
    PlayerAvatar.onEnterWorld = new_onEnterWorld

    import game

    def new_fini():

        old_fini()

        log('Game closed')

        client.send(b'%s' % (reply('END')))

        client.close()

    old_fini = game.fini
    game.fini = new_fini


def createDB():
    import nations
    from items import vehicles

    try:
        tanksDB = dict()
        for nation in nations.NAMES:
            nationID = nations.INDICES[nation]
            for (id, descr) in vehicles.g_list.getList(nationID).iteritems():
                if descr.name.endswith('training'):
                    continue

                #item = vehicles.g_cache.vehicle(nationID, id)

                tanksDB[descr.name] = {
                    'id': descr.compactDescr,
                    'nation': nation,
                    'level': descr.level,
                    'class': tuple(vehicles.VEHICLE_CLASS_TAGS & descr.tags)[0],
                    'shortName': descr.shortUserString,
                    'premium': 'premium' in descr.tags and 'special' not in descr.tags,
                    'special': 'special' in descr.tags
                }

        log('%s tanks loaded!' % (len(tanksDB)))

        return tanksDB

    except:
        import traceback
        traceback.print_exc()

import socket
import datetime

HOST = '127.0.0.1'
PORT = 7777

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))

    while True:
        s.listen(1)
        client, address = s.accept()

        log('Connection from %s:%s' % (address[0], address[1]))

        tanksDB = createDB()

        while True:
            message = (client.recv(1024)).decode('utf-8')

            if not message:
                break

            log(message)

            rich_presence(client, tanksDB)

        client.close()
        log('Connection from %s:%s closed' % (address[0], address[1]))
        s.close()


def run_server():
    log('Starting...')
    try:
        while True:
            start()
    except:
        log('Stopped!')
        log('If you didn\'t close the game, that means the Rich-Presence server crashed !')
        import traceback
        traceback.print_exc()

run = True

if run:
    log('Starting thread...')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.setDaemon(True)
        thread.start()

        log('Thread started!')
    except:
        import traceback
        traceback.print_exc()