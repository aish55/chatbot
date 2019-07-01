import random
greetings = ["hello", "hi", "hola"]
responses = ["hey there!","bonjour!", "hey bro"]
questions1 = ["tell me a riddle"]
response1  = ["i have two hands, two legs, a body,and no brain (What am I)" ]
reresponce1 = [ "it's you!!!"]
questions2 = [ "how old are you"]
response2 = [" older than you"]
questions3 = ["who created you"]
response3 = ["someone that is waaaaaay better you"]
questions4 = ["do you wish you were a human"]
response4 = ["no beacuse i would have to spend my life with you guys"]

while True:
	ask = input(">>> ")
	if ask in greetings:
		randomResponce= random.choice(responses)
		print(randomResponce)
	elif ask in questions1:
		randomResponce= random.choice(response1)
		print(randomResponce)
		askAgain = input(">>> ")
		print(reresponce1)

	elif ask in questions2:
		randomResponce= random.choice(response2)
		print(randomResponce)
	elif ask in questions3:
		randomResponce= random.choice(response3)
		print(randomResponce)
	elif ask in questions4:
		randomResponce= random.choice(response4)
		print(randomResponce)

	else:
		print("whaatt?")