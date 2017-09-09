from fbchat import Client, log
from getpass import getpass
from reply import reply
from train import train
import time

username = str(raw_input("Username: "))
password = getpass()

status = str(raw_input("type y if you Wanna Train first: "))

if status.lower() == 'y':
    client = Client(username, password)
    train(client)

else:
    class EchoBot(Client):
        def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
            self.markAsDelivered(author_id, thread_id)
            self.markAsRead(author_id)

            time.sleep(1)

            uid = client.uid
            USER = client.fetchUserInfo(client.uid)[client.uid]
            name = USER.name.split(" ")[0]

            if author_id == '100012175542876':
    		message = reply(name, author_id, message)
    		if message == "":
    			message = "Don't Know :p"
    		self.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

    client = EchoBot(username, password)
    client.listen()
