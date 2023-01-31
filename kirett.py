from time import sleep
from unittest import main
from scaffold.messagetype import MessageType
from scaffold.message import Message
from scaffold.messenger import Messenger
from scaffold.postmaster import PostMaster

class MainClass(PostMaster):
    
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        while self.running:
            nameprint(self, "going to sleep")
            sleep(2)
            nameprint(self,"now working...")
            while not self.messages.empty():
                inter_message = self.messages.get()
                tmp_rec = self.phonebook[inter_message.get_reciever()]
                tmp_rec.recieveMessage(inter_message)
            nameprint(self, "work finished.")

    def get_name(self):
        return "Kalle"


class MessengerPrinter(Messenger):

    def __init__(self, name) -> None:
        super().__init__(name)

    def run(self):
        while self.running:
            nameprint(self,"going to sleep")
            sleep(2)
            nameprint(self,"now working...")
            while not self.inbox.empty():
                nameprint(self,"Processing Message")
                sleep(5)
                self.inbox.get().message_print()
                sleep(2)
            nameprint(self, "work finished.")


class MessengerCreator(Messenger):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.number = 0

    def run(self):
        #while self.running:
        for x in range(5):
            nameprint(self,"going to sleep")
            # sleep(1)
            nameprint(self,"now working...")
            nameprint(self,"Creating Message")
            # sleep(1)
            self.sendMessage(self.generate_message())
            # sleep(1)
            nameprint(self, "work finished.")

    def generate_message(self):
        self.number += 1
        return Message(
            MessageType.REQUEST,
            self.get_name(),
            "printer",
            f"This is message no. {self.number}"
        )

def nameprint(obj, string: str):
    print(f"{obj.get_name()}:\t{string}")


if __name__ == "__main__":
    print("Hello")

    maintest = MainClass()
    message_printer = MessengerPrinter("printer")
    message_creator = MessengerCreator("creator")

    maintest.register_messenger(message_creator)
    maintest.register_messenger(message_printer)

    maintest.start()
    message_printer.start()
    message_creator.start()

    sleep(10)
    maintest.stop()
    message_creator.stop()
    message_printer.stop()

    print("fertig")


