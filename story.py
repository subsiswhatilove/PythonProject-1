def begin_story():
	user_response = 0
	print("Pick your character")
	user_response = int(input("1.Play as Johny the human\n2.Sally the monster\n3.Teo the superhero"))
	decision1(user_response)
	
def decision1(user_response):
	if user_response == 1:
		print("User selected 1. Johny was gardening his flowers in his apartment when a noise arose in his balcony")
		user_response = int(input("1.Go to balcony\n2.Ignore the noise \n3.GRAB YOUR GUN!!"))
		decision2_1(user_response)
	elif user_response == 2:
		print("User selected 2. Sally was bored, so she called up her friends for a girl's night out")
		user_response = int(input("1.Spend the day eating humans\n2.Discuss some daily juicy gossip\n3.Play fifa with the girls"))
		decision2_2(user_response)
	elif user_response == 3:
		print("User selected 3.Teo was thinking about coming out of retirement and becoming a superhero again.")
		user_response = int(input("1.Become a hero again\n2.Stay retired\n3.Play fifa with the boys"))
		decision2_3(user_response)
	
def decision2_1(user_response):
	if user_response == 1:
		print("User selected 1.Johny went to the balcony and realized he was getting attacked by monsters.")
		user_response = int(input("1.Jump off the balcony\n2.Loot a local store\n3.Talk to one of the monsters"))
	elif user_response == 2:
		print("User selected 2. Johny ignored the noise, turns out one of his vase fell off the table outside. Oh well.")
		user_response = int(input("1.Ignore the noise\n2.Watch TV\n3.Get drunk"))
	elif user_response == 3:
		print("User selected 3. Johny's gun is gone")
		user_response = int(input("1.Get investigative\n2.Buy a new gun\n3.Get a kitchen knife instead"))

def decision2_2(user_response):
	if user_response == 1:
		print("User selected 1. Sally and her girls went on to the nearest town to eat some humans. But Teo the superhero interrupted their lunch.")
		user_response = int(input("1.Beat him up\n2.Teo think you're a beautiful monster and has asked you on a date\n3.Run away"))
		decision4_1(user_response)
	elif user_response == 2:
		print("User selected 2. Ok, check it out. So Sally was on the phone with Fiona who had a sort of on and off relationship with her friend Paul, but it turns out that Paul was cheating on Fiona during this time. So Fiona got all angry with Paul and decided to post a humilating picture of him on monstergram. Paul got extremely angry and said she was a terrible friend and that Kelly; the girl he was cheating with, was a much better girlfreind. Fiona was in shock, saying there is no way Paul could've been with her since she was in vacation for the past 3 weeks. However, the only reason Fiona knew this was because Kelly told her. Paul replied by saying she lied to Fiona, and that him and her were having a baby (not true) together. Fiona was certain that Kelly would never do this, after some clarification from friends; it was concluded that Kelly was in a 'vacation' because Kelly was hooking up with Fiona's brother at the same time. Everyone on monstergram tuning on the dispute, suggested that Fiona should get a pregnancy test. She realized she was the mother of Paul's baby. A week later Paul and Fiona's brother were caught in a lustful act, Paul was a bisexual. To piss off Kelly, Fiona posted about the scene she witnessed and declared to discuss matters at her house. Eventually, in Fiona's house, Kelly gets an overwhelming sense of betrayal and start to hit both Paul and Fiona's brother. As the guys protect each other from Kelly's devestating blows... Fiona is recording the whole thing. Kelly sees this and punches Fiona in the stomach several times, making her lose the baby. ")
		user_response = int(input("1.Sympathize with Fiona\n2.Tell her to sue Kelly"))
	decision4_2(user_response)
	elif user_response == 3:
		print("User selected 3. Pick a team")
		user_response = int(input("1.Barcelona\n2.Real Madrid\n3.Los Granjeros de Sinaloa"))

def decision2_3(user_response):
	if user_response == 1:
		print("User selected 1. Teo sets off on a new adventure to find his archenemy Sally the monster. But instead finds Johny, a local townsmen buying a gun")
		user_response = int(input("1.Ask Johny if he wants to be his sidekick\n2. Ask Johny if he wants to become his new villain"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. Well, the world was invaded by monsters and you're a slave now. The end.")
	elif user_response == 3:
		print("User selected 3. You find out instead that Sally the monster and her firends are online. What do you don?")
		user_response = int(input("1.Challenge her to a duel\n2.Spam her with invites\n3.Discuss politics"))
		decision3_3(user_response)
		
def decision3_1(user_response):
  if user_response == 1:
    print (" Johny was a terrible sidekick and ended up killing himself. The end.")
  elif user_response == 2:
    print (" He said yes, so you flew up in the air and disintegrated him with some special moves. The end.")
    
def decision3_3(user_response):
  if user_response == 1: 
    print("She picked Barcelona. The end")
  elif user_response == 2: 
    print (" You're a spammer, no one likes you. The end.")
  elif user_response == 3: 
    print ("Oops, she's a republican. The end")
    


	
#This runs the game
user_name = ("enter your name")
begin_story()
