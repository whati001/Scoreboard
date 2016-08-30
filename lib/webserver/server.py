#WebSocket with autobahn

import sys
from twisted.internet import reactor, tksupport
from twisted.python import log

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

excel_init_value = None
teamnames_init_value = None
gamescore_init_value = None

class BroadcastServerProtocol(WebSocketServerProtocol):

	def onOpen(self):
		self.factory.register(self)

	def onMessage(self, payload, isBinary):
		if not isBinary:
			msg = "{} from {}".format(payload.decode('utf8'), self.peer)
			self.factory.update(msg)

	def connectionLost(self, reason):
		WebSocketServerProtocol.connectionLost(self, reason)
		self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
	global excel_init_value
	global teamnames_init_value
	
	
	def __init__(self, url, debug=False, debugCodePaths=False):
		WebSocketServerFactory.__init__(self, url, debug=debug, debugCodePaths=debugCodePaths)
		self.clients = []
		#self.tickcount = 0
		#self.tick()

	'''def tick(self):
			self.tickcount += 1
			self.update("tick %d from server" % self.tickcount)
			reactor.callLater(1, self.tick)'''

	def register(self, client):
		if client not in self.clients:
			print("registered client {}".format(client.peer))
			self.clients.append(client)
			if excel_init_value != None:
				client.sendMessage(str("sco_"+excel_init_value).encode('utf8'))
			#print(teamnames_init_value)
			if teamnames_init_value != None:
				client.sendMessage(str("utn_"+str(teamnames_init_value)).encode('utf8'))
			if gamescore_init_value != None:
				client.sendMessage(str("uts_"+str(gamescore_init_value)).encode('utf8'))

	def unregister(self, client):
		if client in self.clients:
			print("unregistered client {}".format(client.peer))
			self.clients.remove(client)

	def update(self, msg):
		#print("broadcasting message '{}' ..".format(msg))
		for c in self.clients:
			c.sendMessage(msg.encode('utf8'))
			print("message sent to {}".format(c.peer))


if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == 'debug':
		log.startLogging(sys.stdout)
		debug = True
	else:
		debug = False

	ServerFactory = BroadcastServerFactory

	factory = ServerFactory(u"ws://localhost:9000", debug=debug, debugCodePaths=debug)

	factory.protocol = BroadcastServerProtocol
	listenWS(factory)

	reactor.run()
