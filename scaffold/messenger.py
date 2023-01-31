from queue import Queue
from threading import Thread

from scaffold.message import Message

class Messenger(Thread):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.inbox = Queue()
        self.reciever = None
        self.outbox = None
        self.running = True
    
    def getOutbox(self, outbox: Queue) -> None:
        self.outbox = outbox

    def sendMessage(self, message: Message) -> None:
        self.outbox.put(message)

    def getReciever(self, reciever: set) -> None:
        self.reciever = reciever

    def recieveMessage(self, message: Message) -> None:
        self.inbox.put(message)

    def processMessage(self) -> None:
        pass

    def get_name(self):
        return self.name

    def stop(self):
        self.running = False