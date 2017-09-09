import re, os
from update import update, remove, train
from glob import glob
from language import improve
from random import randint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def preprocessing(user_name):
	remove(user_name)
	files = glob("msg/" + "*.*")

	for txtfile in files:
		input = open(txtfile, 'rb')
		data = input.read()
		input.close

		name = txtfile.split('/')[1]
		name = name.split('.')[0]

		doc = "aiml/"+ user_name + "/Temp/" + name + ".aiml"
		output = open(doc,'wb')

		msgs = data.split(' &$&$\n')

		me = 0
		you = 0
		temp_you = []
		temp_me = []
		msgs = msgs[ :len(msgs)-1]

		for msg in msgs:
			detail = msg.split(' @$@$ ')
			other = detail[0]
			msg = detail[1]

			if msg != "":

				if other == name:
					you = 1
					message = improve(msg)
					temp_you.append(message)
				else:
					me = 1
					temp_me.append(msg)

				if you != 0 and me !=0:
					for ques in temp_you:
						num = randint(0,len(temp_me)-1)
						if ques.upper() != "" and temp_me[num] !="":
							mess = temp_me[num]
							for lol in [':p', ';p' , '<3', '<', '3<', '>', ':D', ':O', ';)', ':]', ':[' , ':)', ':(' , '&']:
								mess = mess.replace(lol.upper(),"")
								mess = mess.replace(lol.lower(),"")
							output.write("<category> "+'<pattern>'+ ques.upper().encode('utf-8') +'</pattern> ' + "<template>" + mess.encode('utf-8') + "</template>"+"</category>"+"\n")
					you = 0
					me = 0
					temp_you = []
					temp_me = []

		output.close()

	update(user_name)
	train(user_name)
