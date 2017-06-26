import random

def cardpick():

	x = str(random.randint(1,14))

	if x == '11':
		return 'J'
	elif x == '12':
		return 'Q'
	elif x == '13':
		return 'K'
	elif x == '14':
		return 'A'
	else:
		return x

rules = "Here are the rules for the game of Blackjack: \n You and the dealer are both dealt cards. Depending on the cards you have, you can choose to hit for one more card, or stand pat. The dealer is given the same option \n If you stand pat you and the dealer will show your cards. \n If you and the dealer both have a hand over 21, that means the game is a bust. \n If you are over 21, but the dealer is not, or the dealer is closer to 21 than you, dealer wins. \n If the opposite case happens, then you win."

class Deck(object):

	def __init__(self):

		self.posscards = ['1','2','3','4','5','6','7','8','9','10','J','K','Q','A']
		self.deck = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10': 10, 'J': 10, 'K':10, 'Q':10, 'A':1}


class Player(Deck):

	def __init__(self,cash=100):
		Deck.__init__(self)
		self.playerhand = []
		self.num = 0
		self.cash = 100
		self.bet = 0

	def createdeck(self,cardone,cardtwo):
		self.playerhand.append(cardone)
		self.playerhand.append(cardtwo)

	def hit(self,card):
		self.playerhand.append(card)

	def hand(self):
		print self.playerhand

	def total(self):
		for k,v in self.deck.iteritems():
			for val in self.playerhand:
				if val == k:
					self.num += v
		for val in self.playerhand:
			if val == 'A' and self.num <= 11:
				self.num += 10
		return self.num

	def placebet(self,bet):
		self.bet = bet

	def winbet(self):
		self.cash += self.bet

	def losebet(self):
		self.cash -= self.bet

class House(Deck):

	def __init__(self):
		Deck.__init__(self)
		self.playerhand = []
		self.num = 0

	def createdeck(self, cardone, cardtwo):
		self.playerhand.append(cardone)
		self.playerhand.append(cardtwo)

	def hit(self,card):
		self.playerhand.append(card)


	def total(self):
		for k,v in self.deck.iteritems():
			for val in self.playerhand:
				if val == k:
					self.num += v
		for val in self.playerhand:
			if val == 'A' and self.num <= 11:
				self.num += 10
		return self.num

wins = 0
losses = 0
busts = 0
continuegame = 'no'

print rules

while True:

	newgame = raw_input("Would you like to play? y or n")

	if newgame == 'y' and continuegame == 'no':
		human = Player()
		dealer = House()
		human.createdeck(cardpick(),cardpick())
		dealer.createdeck(cardpick(),cardpick())
	elif newgame == 'n':
		print "Thanks for stopping by. We would enjoy it if you come back to the casino!"
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 
		break
	elif newgame == 'y' and continuegame == 'yes':
		human.playerhand = []
		dealer.playerhand = []
		human.num = 0
		dealer.num = 0
		human.createdeck(cardpick(),cardpick())
		dealer.createdeck(cardpick(),cardpick())
	else:	
		continue

	human.bet = 0

	option = input("How much of a bet would you like to place?")

	if option > human.cash:
		print "This is more cash than you have: we're setting you to a default 10 dollar bet."
		human.placebet(10)
	else:
		human.placebet(option)

	optionone = raw_input("Would you like to look at your cards? y or n")

	if optionone == 'y':
		human.hand()
	else:
		print "Ok. Moving on."

	optiontwo = raw_input("Would you like to hit or stand?")

	if optiontwo == 'hit':
		print "Taking a hit."
		human.hit(cardpick())
		if dealer.total() < 15:
			dealer.hit(cardpick())
			print "Dealer took a hit."

	if optiontwo == 'stand':
		print "Standing pat."
		if dealer.total() < 15:
			dealer.hit(cardpick())
			print "Dealer took a hit."

	print "Time to see who wins."
	
	human.hand()
	human.total()
	print dealer.playerhand
	dealer.num = 0
	dealer.total()
	print human.num
	print dealer.num

	if human.num > dealer.num and human.num <= 21:
		wins += 1
		human.winbet()
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if human.num <= 21 and dealer.num > 21:
		wins += 1
		human.winbet()
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if human.num > 21 and dealer.num > 21:
		busts += 1
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if human.num < dealer.num and dealer.num <= 21:
		losses += 1
		human.losebet()
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if human.num > 21 and dealer.num <= 21:
		losses += 1
		human.losebet()
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if dealer.num == human.num:
		busts += 1
		print "Wins: ", wins
		print "Losses: ", losses
		print "Busts: ", busts
		print "Total Cash: ", human.cash 

	if human.cash == 0:
		print "You have no more money. Game over."
		break

	rotateagain = raw_input("Would you like to play again? y or n")

	if rotateagain == "y":
		continuegame = "yes"
		print "Starting up again!"
	else:
		print "Thanks for playing."
		break

#The comments below were for the purpose of testing class functionality
#Jeff = Player('J','3')

#Jeff.createdeck()

#Jeff.hit(cardpick())

#Jeff.hand()

#print Jeff.deck['1']

#print Jeff.deck['Q']

#Jeff.total()

