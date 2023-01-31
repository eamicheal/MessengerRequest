from queue import Queue
from threading import Thread
from time import sleep

from scaffold.messenger import Messenger

class PostMaster(Thread):

    def __init__(self) -> None:
        super().__init__()
        self.phonebook = dict()
        self.messages = Queue()
        self.running = True

    def deliver_message(self) -> None:
        pass

    def register_messenger(self, messenger: Messenger) -> None:
        self.phonebook[messenger.get_name()] = messenger
        messenger.getOutbox(self.messages)
        print("registered: " + messenger.get_name())

    def unregister_messenger(self, messenger: Messenger) -> None:
        if messenger.get_name() in self.phonebook: # TODO: Besser lösen
            del self.phonebook[messenger.get_name()]

    def stop(self):
        self.running = False