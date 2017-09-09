import os
from messages import messages
from pre import preprocessing as process

def train(client):
    uid = client.uid
    USER = client.fetchUserInfo(client.uid)[client.uid]
    name = USER.name.split(" ")[0]

    path = "msg/"
    if not os.path.exists(path):
        os.makedirs(path)

    path = "aiml/"
    if not os.path.exists(path):
        os.makedirs(path)

    path = "aiml/" + name
    if not os.path.exists(path):
        os.makedirs(path)

    path = "aiml/" + name + "/Temp"
    if not os.path.exists(path):
        os.makedirs(path)

    path1 = "aiml/" + name + "/XMLS"
    if not os.path.exists(path1):
        os.makedirs(path1)

    path2 = "aiml/" + name + "/brain"
    if not os.path.exists(path2):
        os.makedirs(path2)

    messages(client)
    process(name)
