# -*- encoding: utf-8 -*-
import sys
import StringIO
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log

class Evaluator():
    def __init__(self):
        self.globals = {}

    def myexec(self, code):
        codeOut = StringIO.StringIO()
        sys.stdout = codeOut
        exec(code, self.globals)
        sys.stdout = sys.__stdout__
        ret = codeOut.getvalue()
        return ret

    def eval(self, code):
        return eval(code, self.globals)

class PyBot(irc.IRCClient):
    nickname = "pybot"

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.evaluator = Evaluator()

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)

    def signedOn(self):
        self.join(self.factory.channel)

    def joined(self, channel):
        log.msg("[I have joined %s]" % channel)

    def privmsg(self, user, channel, msg):
        user = user.split('!', 1)[0]
        log.msg("%s: %s " % (user, msg))
        if msg.startswith('>>'):
            ret = self.evaluator.myexec(msg[2:])
            self.msg(channel, ret)
        elif msg.startswith('>'):
            ret = self.evaluator.eval(msg[1:])
            if type(ret) != str:
                ret = str(ret)
            self.msg(channel, ret)

class PyBotFactory(protocol.ClientFactory):
    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr):
        p = PyBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()

if __name__ == '__main__':
    log.startLogging(sys.stdout) 
    f = PyBotFactory(sys.argv[1])
    reactor.connectTCP("irc.freenode.net", 6667, f)
    reactor.run()
