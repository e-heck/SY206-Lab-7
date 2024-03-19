##Heck lab 7
import time
from inputimeout import inputimeout
import random


class Node:
	def __init__(self, data, desc):
		self.data = data #Integer
		self.left = None
		self.right = None
		self.desc = desc #Description of events/choices from a given node
	
	def __str__(self):
		return f"{self.data}"


class BST:
	def __init__(self):
		self.root = None
	
	##Recursive insert (w/ helper)
	def rec_insert(self, data, desc):
		self.__rec_insert(self.root, data, desc)
		
	def __rec_insert(self, cur, data, desc):
		new = Node(data, desc)
		if cur == None: #Base case
			self.root = new
		elif data <= cur.data: #Smaller values go left
			if cur.left == None:
				cur.left = new
			else: #If there is already a value for cur.left, recursively run function with next left cur.
				self.__rec_insert(cur.left, data, desc)
		elif data >= cur.data: #Greater values go right
			if cur.right == None:
				cur.right = new
			else: #If there is already a value for cur.right, recursively run function with next right cur.
				self.__rec_insert(cur.right, data, desc)

	def print_desc(self):
		self.__print_desc(self.root)
		
	def __print_desc(self, cur):
		if cur != None:
			print(cur.desc)
			if cur.left != None:	
				self.__print_desc(cur.left)
			if cur.right != None:
				self.__print_desc(cur.right)
		else:
			print("You did nothing")

	def clear(self):
		cur = self.root
		cur.left = None
		cur.right = None
		self.root.desc = ""

def timer(t):
	try:
		usr_input = inputimeout(prompt="\n", timeout=t)
	except:
		usr_input = None
	return usr_input
		
		
def main():

	##Create storyline (BST):
	myBST = BST()
	
	##Menus and pathway decisions for game
	start_menu = True
	while start_menu:
		start_selection = input("What do you want to do?\n(1) Begin adventure\n(2) Quit\n")
		if start_selection == "1":
			myBST.rec_insert(10, "You began your epic adventure!") #root - home
			print("...Adventure beginning...\n")
			time.sleep(1)
			print("You walk out of a tavern in a small, medieval town. As a traveler, your plan is to pack up the few posessions you keep with you before getting back on the road.\nYour only quest? Find treasure. Get rich.\n")
			time.sleep(3)
			while True:
				mode_selection = input("(1) Explore the town\n(2) Explore outside of town\n")
				if mode_selection == "1":
					myBST.rec_insert(7, "You decided to explore the town") ##easy mode (just choices) - town
					print("You make your way to a bustling marketplace. You're busy eyeing some expensive looking fabrics when suddenly you hear shouts of 'Thief! Thief!' as a dark clothed figure streaks by\n")
					time.sleep(3)
					alignment_selection = input("(1) Chase after the thief!\n(2) Use the chaos to steal as much from the market as you can!\n")
					if alignment_selection == "1":
						myBST.rec_insert(3, "You decided to go after the thief.") #good track - chase after thief
						print("Catching the thief would bolster your reputation in this small town. Maybe if you were a celebrated hero, some townsfolk might point you in the direction of treasure.\n")
						time.sleep(3)
						print("You scan the growing croud for the thief. Once you spot the tattered ends of a black cape slipping away, you take off and begin the chase.\n")
						time.sleep(3)
						print("The thief isn't too far ahead, but he hurdles a huge pile of crates!\nHit space on your keyboard and press enter quickly to leap over the crates!\n")
						jumping = timer(8)
						if jumping == " ":
							print("It's a close call, but you make it over the crates and continue your chase.\n")
							time.sleep(3)
							print("You lose sight of the thief just as you both come to an intersection in alleyways. Do you go left or right?")
							correct_dir = random.randint(1, 2)
							usr_dir = input("\n(1) Left\n(2) Right\n\nDo you go left or right? ")
							if int(usr_dir) == correct_dir:
								myBST.rec_insert(1, "You caught the thief!") #happy ending - catch thief, get reward
								time.sleep(3)
								print("After a couple more twists and turns of the alleyways and countless more obstacles to take on, you're finally just barely close enough to reach the thief's cape. After a courageous lunge, you snag a fistful of black fabric and bring both you and the thief tumbling to the ground. Town guards appear and take the thief away.\n\nCongratulations! You caught the thief, and are now the town's hero. Now it's time to start asking around about treasure.\n")
								time.sleep(3)
								break
							else:
								myBST.rec_insert(2, "You didn't catch the thief, but you found a dog friend!") #bad ending - lose thief but find a dog
								time.sleep(3)
								print("You keep running, but the thief still hasn't come back in view. You slow down and turn another corner, only to come face to face with a wall. A dead end. You notice soft whines coming from behind a crate. A quick look behind it reveals a puppy! Maybe today you aren't the village hero, but at least you found a friend.\n")
								time.sleep(3)
								break
						else:
							myBST.rec_insert(2, "You didn't catch the thief, but you found a dog friend!") #bad ending - lose thief but find a dog
							time.sleep(3)
							print("You keep running, but the thief still hasn't come back in view. You slow down and turn another corner, only to come face to face with a wall. A dead end. You notice soft whines coming from behind a crate. A quick look behind it reveals a puppy! Maybe today you aren't the village hero, but at least you found a friend.\n")
							time.sleep(3)
							break
					elif alignment_selection == "2":
						myBST.rec_insert(6, "You decided to steal stuff") #evil track - use the chaos to steal something yourself
						time.sleep(3)
						print("You follow the thief's example and start stuffing goods from every stall you can get to through the crowd into your rucksack. Now there are even more shouts of 'thief!' as townsfolk realise what you're doing and start pointing guards toward you.\n")
						time.sleep(3)
						print("Type ESCAPE and hit enter on your keyboard to flee the scene or wait to keep stealing!\n")
						escaping = timer(12)
						if escaping == "ESCAPE":
							myBST.rec_insert(4, "You escaped, becoming a thief and causing destruction in your wake.") #happy ending - get away causing destruction
							time.sleep(1)
							print("In a small town, you're not taking any chances. Now that people have seen your face, there's no way you're making any progress in your treasure hunt without getting hauled off to jail. You take one last look around before sprinting in the opposite direction as the first thief, knocking crates and barrels aside as they appear in front of you. Looking back, it looks like you caused massive levels of destruction to the marketplace, which is probably why that town's economy dropped off so much. You might not be any closer to treasure, but at least you have a bunch of random goods to trade in the next town over.\n")
							time.sleep(3)
							break
						else:
							myBST.rec_insert(5, "You got too greedy and ended up in jail.") #bad ending - get caught, jail
							time.sleep(3)
							print("Just as you're getting ready to book it, you notice a necklace your mom might fancy. You've been looking for mother's day gift, and this would be perfect! Just as you snatch it from a stall, a foreboding shadow looms over you, and before you can react, your hands are bound together. You're being hauled off to prison. Maybe you can send a carrier pigeon to your mom with a nice note for mothers day.\n")
							time.sleep(3)
							break
					else:
						print("\nChoose 1 or 2\n")
				elif mode_selection == "2":
					myBST.rec_insert(17, "You decided to look for treasure in the dark forest") ##hard mode (choices and items) - dark forest
					print("You head to the wall of trees that surrounds the town. If there's treasure to be found, it's got to be out there.\n")
					time.sleep(3)
					print("Your surroundings dim as sprinkles of light struggle to make their way through the dense canopy of leaves above you.\n")
					time.sleep(3)
					print("A gloom settles around you as you pick through the trees and foliage. You feel as if you are being watched when a sudden bout of crying and yelling pulls you back to reality.\n")
					time.sleep(3)
					print("It sounds like a young boy is crying. You might be dealing with a lost kid, but you've heard stories of malicious entities imitating children's cries to lure in their lunch.\n")
					alignment_selection = input("(1) Help the kid\n(2) Keep looking for treasure\n")
					if alignment_selection == "1":
						myBST.rec_insert(13, "You decided to try and help the crying kid.") #good track - help a scared kid find their way out
						print("You shove branches and bushes aside as you barrel through the forest toward the cries for help.\n")
						time.sleep(3)
						print("Finally, you come to a scared looking little boy. He looks a little pathetic curled up on the ground sucking his thumb. You know you must be close to the treasure now, the air just has a magical feel to it. It can't hurt to have this kid tag along until you can find the treasure and skedaddle.\n")
						time.sleep(3)
						print("Suddenly, the ground starts to shake with the pounding of hoofbeats, and you hear voices with the unmistakable boisterousness of pirates! Type HIDE quickly to find a hiding place with the kid!\n")
						hiding = timer(7)
						if hiding == "HIDE":
							myBST.rec_insert(11, "You avoided the pirates, found treasure, and helped the kid return to town!/") #happy ending - see a cool waterfall and find a way out
							print("The pirates come closer and closer to the bush you and the kid jumped into. Miraculously the boy doesn't make a sound, and the pirates eventually gallop off on their horses.\n")
							time.sleep(3)
							print("You and the kid keep walking until you come across a sparking cove with a waterfall draped over the rocks. Everyone knows treasure chests are hidden behind waterfalls, so it's no surprise when you discover just that. You return to the town with pockets full of gems, gold coins, and a happy kid trailing behind you.\n")
							time.sleep(3)
							print("Congratulations! You found treasure and returned a lost kid safely to his town. Time for your next adventure!")
							time.sleep(3)
							break
						else:
							myBST.rec_insert(12, "The kid's sniffling gave you away. At least no one was hurt.") #bad ending - Try and get treasure but bandits chase you out
							time.sleep(3)
							print("Maybe little kids aren't the best to have with you on a professional treasure finding adventure. The boy's pathetic nature wins out and he starts bawling as soon as the pirates get close. Shouts of 'aargh' and *wooshes* of cutlasses chase you and the kid out of the forest. Hopefully those pesky pirates don't find the treasure before you. At least you rescued the poor lad.\n")
							time.sleep(3)
							break
					elif alignment_selection == "2":
						myBST.rec_insert(14, "Who cares about kids? You ignored the cries for help and decided to spend your strength looking for treasure.") #evil track - look for treasure
						correct_dir = random.randint(1, 2)
						print("You aren't taking your chances with any nefarious monsters playing games with you. Either way, children are menaces and you want nothing to do with them. You continue on your search for treasure. It takes all day, but by nightfall, there are two northern areas you haven't explored yet.\n\n(1) Northeast\n(2) Northwest")
						usr_dir = input("Do you head to the northeast or northwest area? ")
						if int(usr_dir) == correct_dir:
							myBST.rec_insert(15, "You found treasure, but at what cost? Have fun as a wanted criminal.") #happy ending - find treasure, become a wanted criminal
							time.sleep(3)
							print("\nYou head north and come across a small cottage. Cottages aren't exactly known for treasure, but you head inside anyways. Within the home, you notice quite a few carvings. However, you don't come across anything shiny. You decide a couple of the carvings might be worth something, but as you're packing a couple away, the door bursts open and guards fill the cottage. Looks like you're stealing extremely valuable carvings from the local village's favorite wood carver. You take off with your loot. You may be a wanted criminal now, but at least all this artistic wood will fetch you a pretty sum in the neighboring town marketplace.\n")
							time.sleep(3)
							break
						else:
							time.sleep(3)
							myBST.rec_insert(16, "Be careful where you step! You were framed for a crime you didn't commit by bandits after they captured you.") #bad ending - tied up by bandits, framed for stealing
							print("\nYou head north, when suddenly the world flips upside down. Confused and disoriented, you look wildly around as bandits emerge from the trees. you've stumbles right into one of their traps. They bandits make quick workd of tying you up and toss some coins and jewelry around you. It isn't long before a hysteric woman and her family comes across you. 'Thief!!' She shouts. 'You stole my favorite necklace! Thank goodness someone tied you up and left you here! Justice shall be dealt swiftly!' As town guards appear to take you away, you manage to struggle your way out of the ropes binding you and take off into the forest. You found no treasure, and are now a wanted criminal. Good luck!\n")
							time.sleep(3)
							break
					else:
						print("\nChoose 1 or 2\n")
				else:
					print("\nChoose 1 or 2\n")
			end_menu = True
			while end_menu:
				end_selection = input("\nWhat an adventure! What would you like to do now?\n(1) Review choices\n(2) Try again\n(3) Quit\n")
				if end_selection == "1":
					print("\n\nHere are the choices you made:")
					myBST.print_desc()
				if end_selection == "2":
					myBST.clear()
					break
				if end_selection == "3":
					print("\n  |------Quitting------|\n|---Farewell adventurer---|")
					start_menu = False
					break
				else:
					print("\nChoose 1, 2 or 3\n")
		elif start_selection == "2":
			time.sleep(1)
			print("\n  |------Quitting------|\n|---Farewell adventurer---|")
			start_menu = False
		else:
			print("\Choose 1 or 2\n")
	
	
if __name__ == "__main__":
	main()