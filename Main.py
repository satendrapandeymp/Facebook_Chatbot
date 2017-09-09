from fbchat import Client, log
from getpass import getpass
from reply import reply
from gtts import gTTS
from train import train
import time, os

username = str(raw_input("Username: "))
password = getpass()

status = str(raw_input("type y if you Wanna Train first: "))

if status.lower() == 'y':
    client = Client(username, password)
    train(client)

else:
    sound = str(raw_input("Wanna hear incoming messages y for yes: "))
    if sound == 'y':
        class EchoBot(Client):
            def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
                self.markAsDelivered(author_id, thread_id)
                self.markAsRead(author_id)

                uid = client.uid
                USER = client.fetchUserInfo(client.uid)[client.uid]
                myname = USER.name.split(" ")[0]

                USER = client.fetchUserInfo(author_id)[author_id]
                from_ = USER.name.split(" ")[0] + " " + USER.name.split(" ")[1]

                if author_id != self.uid:

                    name = "temp.mp3"
                    data = "you got a message from " + from_ + ". The message is " + message
                    tts = gTTS(text=data , lang='en')
                    tts.save(name)
                    name = "mpg321 %s"%(name)
                    os.system(name)

                    message = reply(myname, author_id, message)
                    if message == "":
            			message = "Don't Know :p"
                    self.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

        client = EchoBot(username, password)
        client.listen()
    else:
        class EchoBot(Client):
            def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
                self.markAsDelivered(author_id, thread_id)
                self.markAsRead(author_id)

                time.sleep(1)

                uid = client.uid
                USER = client.fetchUserInfo(client.uid)[client.uid]
                name = USER.name.split(" ")[0]

                if author_id != self.uid:
            		message = reply(name, author_id, message)
            		if message == "":
            			message = "Don't Know :p"
        		self.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

        client = EchoBot(username, password)
        client.listen()
