import os, aiml

kernel = aiml.Kernel()

def reply(user, username, message):
	filename = "aiml/"+  user +"/brain/" + username + ".brn"
	if os.path.isfile(filename):
		kernel.bootstrap(brainFile = filename)
	else:
		res = 'unknown user' + name
		return res

	bot_response = kernel.respond(message)

	return bot_response
