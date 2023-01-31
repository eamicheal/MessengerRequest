from scaffold.messagetype import MessageType

class Message:
    
    def __init__(self, message_type: MessageType, sender: str, reciever: str, payload: object) -> None:
        self.message_type = message_type
        self.sender = sender
        self.reciever = reciever
        self.payload = payload
    
    def message_print(self):
        print(f"Sender:\t{self.sender}")
        print(f"Reciever:\t{self.reciever}")
        print(f"MessageType:\t{self.message_type}")
        print(f"Payload:\t{self.payload}")
    
    def get_reciever(self):
        return self.reciever