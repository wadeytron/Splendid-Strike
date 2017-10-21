#!/usr/bin/python

import os
import time
import random
from random import randint

#################### VARIABLES ##############
ABM_ICBM_ratio = 0
number_of_ABMs = 41
number_of_ICBMs = random.randint(5,20)

hits = 0
misses = 0
enemy_salvoes = 1
begin = ""
nukeouts = 0
current_target = ""



###################### SUBROUTINES #####################################





def check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts):
	if (number_of_ABMs < 1):
		print "YOU HAVE RUN OUT OF ABMS!"
		print "Unfortunately, the enemy has not..."
		nukeouts += number_of_ICBMs
		loop = nukeouts
		pauser (2000)
		print "AAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGGGGHHHHHHHHHHHH!!!!"
		print " \n"
		print "          ********************"
		print "         *********************"
		print "       **************************"
		print "      ***************************"
		print "       **************************"
		print "         **********************"
		print "         *********************"
		print "          *******************"
		print "          ********************"
		print "         **********************"
		print "      **************************"		
		print "    ******************************"	
		print "                ****** "
		print "               ********"
		print "                ****** "
		print "                 ****  "
		print "                 ****  "
		print "                ******  "
		print "     *****************************"		
		print "    *******************************"	
		print "    KABOOOOOOOOOOOOOOOOOOOOOOM!\n\n ";
		print nukeouts,
		print "American cities have been destroyed!"
		print "MILLIONS of people are dead, many of whom voted for YOU!"
		print " Oh, woe, woe, woe is you! It's just so UNFAIR and FAKE!"
		print "\n\n \t GAME OVER \n \n";
		quit();


def pauser(loops):
	loops *= 1000
	while (loops > 0):
		loops -=1
	return

print "\n\n\n\n\n\n\n\n\n"
print "\n \t\t Splendid Strike"
print "\n \tA computer game by Andrew Wade."
print "\n\n \t(C) Copyright Andrew Wade 2017"
print "\n Please maximise this window for the best possible experience :-)"

try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",

print "\n You are President Donald Trump... (sorry) \n"
print " It's a nice, quiet day. You're just getting down to a bit of light "
print "entertainment at the expense of libtardz, Commies and Rocket Man on "
print "Twitter, when all of a sudden someone tells you..."

print "\n\t NUKES!!! COMMIE NUKES COMIN' TO GET US!!"
print "\n You run to the desk of the Oval Office, where you had a computer "
print "terminal installed that connects you to the missile defence system."
print "This allows YOU to control America's defences. You have the best "
print "defences, truly fantastic - and as the most talented bravest cleverest "
print "person in the world, YOU are the only one who knows how to beat those "
print "dirty Commies and SAVE AMERICA!"
print "\n";
print " Each ABM you fire has a 56% chance of hitting the enemy missiles "
print "that are raining down on God's Country like dollar bills in one of "
print "your very classy entertainment resorts. "
print "\n"
print "You can fire these singly or in salvoes, but because the enemy missiles "
print "come in SO DARNED FAST, you have to tell the computer how many ABMs "
print "to fire at each enemy ICBM in advance."
print "\n";

try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",


print ""
print "OK, I hope you're ready... starting in ",


print "3...",

print "2...",

print "1...",


print "\n\n\n"

print "\t\t ***************************"
print "\t\t * WARNING! MISSILE ALERT! *"
print "\t\t ***************************"
while (number_of_ICBMs > 0):
	pauser (100)
	enemy_salvo = random.randint(1,number_of_ICBMs)
	print "\n \t *** There are ",enemy_salvo,
	print "ICBMs incoming! ***"
	
	print "This is the ",enemy_salvoes,
	print "st salvo."
	check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

	print "You have ",number_of_ABMs,
	print "ABMs left."
	number_of_ICBMs -= enemy_salvo

	print "Intelligence indicates that They still have another",number_of_ICBMs
	print "left."
	try:
		ABM_ICBM_ratio = int(input("\n How many ABMs to each ICBM?  >"))
	except:
		print " Numerals ONLY, please! (sorry Trump, I know you don't like Arabic things, but" 
		print "we really, REALLY need Arabic numerals!)"

	number_of_ICBMs += enemy_salvo   	# Bit of a bodge this

	ABMs_spent = (ABM_ICBM_ratio * enemy_salvo)
#	number_of_ABMs -= ABMs_spent

	enemy_round = enemy_salvo;



	print "\n\n"

	print "*****************************"
	print "*ENEMY MISSILE SALVO BEGINS!*"
	print "*****************************"

	time.sleep(1)
	while (enemy_salvo > 0):
		time.sleep(1)
		current_target = ""
		print "\n\n"
		print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print " !!! Missiles left to shoot down:",enemy_salvo,"!!!"
		print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		number_of_ICBMs -= 1
		enemy_salvo -= 1
		ABM_salvo = ABM_ICBM_ratio
		print "\n Firing ABMS... fingers crossed!"
		print "ABMs:",number_of_ABMs,"  ICBMs:",number_of_ICBMs,"  nukeouts:",nukeouts
		check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

		while (ABM_salvo >0):
			time.sleep(1)
			ABM_salvo -= 1
			number_of_ABMs -= 1
			check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	
			enemy_ICBM = random.randint(0,100)
			your_ABM = random.randint(0,56)
#			print "\n Enemy ICBM value:",enemy_ICBM
#			print " Your ABM value:",your_ABM

			if ((your_ABM - enemy_ICBM) > 0):
				if (current_target == "HIT"):
					pauser (200)
					print "\t* ANOTHER HIT! * Well done! You hit the same missile more than once!"
				else:
					pauser (500)
					print "\t * A HIT! *"

				hits += 1
				abm_salvo = 0
				current_target = "HIT"
				
			else:
				if (current_target == "HIT"):
					pauser (200)
					print "\t Your missile screams past the cloud of debris!!"
				else:
					pauser (500)
					print "\t ***** AAAARGH YOU MISSED! ABMS LEFT IN SALVO:",ABM_salvo
				misses += 1
		if (current_target != "HIT"):
			time.sleep(1)
#			print "       ***** "
#			print "      *******"
#			print "       ***** "
#			print "     ********"
#			print "      ****** "
#			print "        **  "
#			print "        **  "
#			print "        **  "
#
			print "AAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGGGGHHHHHHHHHHHH!!!!"
			print " \n"
			print "          ********************"
			print "         *********************"
			print "       **************************"
			print "      ***************************"
			print "       **************************"
			print "         **********************"
			print "         *********************"
			print "          *******************"
			print "          ********************"
			print "         **********************"
			print "      **************************"		
			print "    ******************************"	
			print "                ****** "
			print "               ********"
			print "                ****** "
			print "                 ****  "
			print "                 ****  "
			print "                ******  "
			print "     *****************************"		
			print "    *******************************"	
			print "    KABOOOOOOOOOOOOOOOOOOOOOOM!\n\n ";
			print "  NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!! ";
			nukeouts += 1

	time.sleep(1)
	enemy_salvoes +=1
	ABMs_ever = hits+misses
	print "\n\n"
	print "\n ****************************************"
	print " *         POST BATTLE REPORT:          *"
	print " * Enemy missiles fired this round:",enemy_round,"\t*"
	print " * Total ABMs fired (ever):",ABMs_ever,"\t*"
	print " * Hits: (ever)",hits,"                   \t*"
	print " * Misses: (ever)",misses,"                \t*"
	print " * Total cities destroyed:",nukeouts,"    \t*"
	print " ****************************************\n"
	print "\n \n Please note that it is possible for more than one ABM to hit a single enemy missile"
	print "\n\n\n"



try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",# I don't give a shit

if (nukeouts == 0):
	time.sleep(1)
	print "__________________________"
	print "* * * * * ----------------"
	print "* * * * * ----------------"
	print "* * * * * ----------------"
	print "* * * * * ----------------"
	print "--------------------------"
	print "--------------------------"
	print "--------------------------"
	print "__________________________"
	print "\n\n YAAAAAY!! AMERICA HAS SURVIVED!!!"
	print "\n  YOU WIN AND ARE THE BEST PRESIDENT EVER!!!"


else:
	time.sleep(1)
	print "\n YOU LOSE!"
	print "\n Well, I hope you're pleased with yourself. Only ", nukeouts
	print "American cities have been blown to smithereens. "
	print "\n\n Of course, Korea has been reduced to its constituent "
	print "atoms, so there's always that."
	print "\n"
	print " Still, when the British clear up all the dead bodies, America "
	print "will probably make a great holiday resort for fat, stupid European "
	print "businessmen! (assuming Russia allows Europe to continue to exist)"
	print "\n BTW, some gentlemen from INTERPOL want to talk to you about war "
	print " crimes charges..."
	print "\n They blame YOU for starting the war, for some reason. I know, right?"
	print "\n Ingrates!"


print "\n\n"

try:
	cont = int(input("\n Press ENTER for the sleeve notes..."))
except:	
	print "",

print "This game was inspired by Ankit Panda and Vipin Narang's article in "
print "War On The Rocks, called \"Deadly Overconfidence:  Trump Thinks "
print "Missile Defenses Work Against North Korea, and That Should Scare You"
print "\n Read it here:\n https://warontherocks.com/2017/10/deadly-overconfidence-trump-thinks-missile-defenses-work-against-north-korea-and-that-should-scare-you/"

print "\n\n"

try:
	cont = int(input("\n Press ENTER to exit..."))
except:	
	print "",

quit()
