import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def messages(client):

	threads = client.fetchThreadList()
	for i in range(10):
		offset = 20*(i+1)
		threads += client.fetchThreadList(offset = offset)

	for thread in threads:
		data = str(thread).split(" ")
		if len(data) == 4:
			id = data[3].split('(')[1].split(')')[0]

			other_name = str(data[1]) + ' ' + str(data[2])

			print other_name

			other_user = client.searchForUsers(other_name)
			if len(other_user)>0:
				other_user = other_user[0]
				name_file = other_user.uid
			else:
				name_file = "random"
			filename = "msg/" + str(name_file) + ".txt"

			messages = client.fetchThreadMessages(thread_id=id, limit=25000)

			print len(messages)

			if len(messages) > 20:
				file = open(filename, 'wb')
				for message in messages:
					if message.text is not None or message.text == "":
							file.write(message.author + ' @$@$ ' + message.text.encode('utf-8') + ' &$&$\n' )
				file.close()
