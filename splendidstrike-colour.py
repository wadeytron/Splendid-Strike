#!/usr/bin/python

import os
import time
import random
from random import randint

#################### VARIABLES ##############
ABM_ICBM_ratio = 0
number_of_ABMs = 44			# Yes, this is really the number of ABMs the USA has.
number_of_ICBMs = random.randint(1,20)	# Let's generate between 1 and 20 enemy warheads

hits = 0
misses = 0
enemy_salvoes = 1
begin = ""
nukeouts = 0
current_target = ""



###################### SUBROUTINES #####################################



def NuclearExplosion():
	print "AAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGGGGHHHHHHHHHHHH!!!!"
	print ('\033[0;37;47m'+'                                  ')
	print ('\033[2;29;47m'+'                ********')
#	print "              ",
	#print ('\033[0;31;41m'+'         '+'\033[0m')
#	print ('\033[2;31;47m'+'         ***********************')
	print ('\033[2;31;47m'+'                   ')
	print "             **************"
	print "          ********************"
#	print ('       **************'+'\033[2;3;47m'+'************')
	print ('       **************'+'\033[1;31;47m'+'************')
	print "      ***************************"
	print "       **************************"
	print "         ************",
	print ('\033[2;31;47m'+'**********\n         *********************')
	print "          *******************"
	print "                 *****"
	print "                ***** "
	print "           ***   *****   *****"
	print "       ****     *****        ***"		
	print "      *          *****          ** "	
	print "     ***         ****         ***"
	print "        ******  ******   ****** "
	print "              ** ***** **"
	print "                 ****  "
	print "                 ****  "
	print "                 ****  "
	print "                ******  "
	print "     *****************************"		
	print ('    *******************************\n\n '+'\033[0m')
	print "      KABOOOOOOOOOOOOOOOOOOOOOOM!"
	time.sleep(1)
	



def check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts):
	if (number_of_ABMs < 0 and number_of_ICBMs >0):

		print ('\033[0;30;41m'+'\t   YOU HAVE RUN OUT OF ABMS!            '+'\033[0m')
		print ('\033[1;33;41m'+'\t Unfortunately, the enemy has not...    '+'\033[0m')

#		print ('\033[7;30;91m'+'\t   YOU HAVE RUN OUT OF ABMS!'+'\033[0m')
#		print ('\033[7;30;91m'+'\t Unfortunately, the enemy has not...'+'\033[0m')
		nukeouts += number_of_ICBMs
		loop = nukeouts
		pauser (40000)
		NuclearExplosion()
#		print "    KABOOOOOOOOOOOOOOOOOOOOOOM!\n\n ";
		print "   ",nukeouts,
		print "American cities have been destroyed!",
		print ('\033[3;33;40m'+' ')
		print " MILLIONS of people are dead, many of whom voted for YOU!"
		print (' Oh, woe, woe, woe is you! It\'s just so UNFAIR and FAKE!'+'\033[0m')
		print "\n \t GAME OVER \n";
		quit();


def pauser(loops):
	loops *= 1000
	while (loops > 0):
		loops -=1
	return

############################ MAIN PROGRAM #######################################

print "\n\n\n\n\n\n\n\n\n"
print ('\033[91m'+'')
print "\n \t\t Splendid Strike",
print (''+'\033[0m')
print " \tA computer game by Andrew Wade."
print " \t(C) Copyright Andrew Wade 2017"
print "\n Please maximise this window for the best possible experience :-)"

try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",

print "\n You are",
print ('\033[3;33;40m'+' President Donald Trump...'+'\033[0m'),
print ' (sorry) '
print " "
print ('\033[3;33;40m'+'  It\'s a nice, quiet day. You\'re just getting down to a bit of light '+'\033[0m')
print ('\033[3;33;40m'+'  entertainment at the expense of libtardz, Commies and Rocket Man on  '+'\033[0m')
print ('\033[3;33;40m'+'  Twitter while fiddling around with all the buttons and things in your ')
print ('  special briefcase, when all of a sudden everyone completely loses it! '+'\033[0m')
print ('\033[3;33;40m'+'  An aide pops his head round the door and tells you in a breathless voice\n '+'\033[0m')
print "\t",
print ('\033[7;30;91m'+'   NUKES!!! COMMIE NUKES COMIN\' TO GET US!! '+'\033[0m')
print "\n";
print ('\033[3;33;40m'+'  You run to the desk of the Oval Office, where you had a computer '+'\033[0m')
print ('\033[3;33;40m'+'  terminal installed that connects you to the missile defence system.'+'\033[0m')
print ('\033[3;33;40m'+'  This allows YOU to control America\'s defences. You have the best '+'\033[0m')
print ('\033[3;33;40m'+'  defences, truly fantastic - and as the most talented bravest cleverest '+'\033[0m')
print ('\033[3;33;40m'+'  person in the world, YOU are the only one who knows how to beat those '+'\033[0m')
print ('\033[3;33;40m'+'  dirty Commies and SAVE AMERICA!'+'\033[0m')
print "\n";
print ('\033[3;33;40m'+'  Each ABM you fire has a 56% chance of hitting the enemy missiles '+'\033[0m')
print ('\033[3;33;40m'+'  that are raining down on God\'s Country like dollar bills in one of '+'\033[0m')
print ('\033[3;33;40m'+'  your very classy entertainment resorts. '+'\033[0m')
print "\n"
print ('\033[3;33;40m'+'  You can fire these singly or in salvoes, but because the enemy missiles '+'\033[0m')
print ('\033[3;33;40m'+'  come in SO DARNED FAST, you have to tell the computer how many ABMs '+'\033[0m')
print ('\033[3;33;40m'+'  to fire at each enemy ICBM in advance.'+'\033[0m')
print "\n";

try:
	cont = int(input("\n Press ENTER to start the game!"))
except:	
	print "",


print ""
print "OK, I hope you're ready... starting in ",


print "3...",

print "2...",

print "1...",


print "\n\n\n"

print "\t\t ******************************"
print "\t\t *",
print ('\033[91m'+' WARNING! MISSILE ALERT!'+'\033[0m'),
#print ('\033[6m'+' WARNING! MISSILE ALERT!'+'\033[0m'),


print " *"
print "\t\t ******************************"
while (number_of_ICBMs > 0):
	pauser (100)
	enemy_salvo = random.randint(1,number_of_ICBMs)
	print ('\033[91m'+'\n \t ')
	print " *** There are ",enemy_salvo, "ICBMs incoming! ***"
	print (' '+'\033[0m'),
	print "This is the ",enemy_salvoes,
	if (enemy_salvoes == 1):
		print "st",
	elif (enemy_salvoes == 2):
		print "nd",
	elif (enemy_salvoes == 3):
		print "rd",
	else:
		print "th",	
	print "salvo."
	check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

	print "You have ",number_of_ABMs,
	print "ABMs left."
	number_of_ICBMs -= enemy_salvo

	print "Intelligence indicates that They still have another",number_of_ICBMs
	print "left in reserve."
	try:
		ABM_ICBM_ratio = int(input("\n How many ABMs to each ICBM?  >"))
	except:
		print " Numerals ONLY, please! (sorry Trump, I know you don't like Arabic things, but" 
		print "we really, REALLY need Arabic numerals!)"
		ABM_ICBM_ratio = int(input("\n How many ABMs to each ICBM?  >"))

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
		print ('\033[7;30;91m'+'                                         ')
		print "     Missiles left to shoot down:",enemy_salvo,"   ",
		if (enemy_salvo)<10:
			print " "
		else:
			print ""
		print ('                                         '+'\033[0m')
		ABM_salvo = ABM_ICBM_ratio
		print ('\033[0;30;42m')	,	# green
		print "  Firing ABMS... fingers crossed! "
		print "ABMs:",number_of_ABMs,"  ICBMs:",number_of_ICBMs,"  nukeouts:",nukeouts,
		print ('\033[0m')
		check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

		while (ABM_salvo >0):
			time.sleep(1)
			ABM_salvo -= 1
			number_of_ABMs -= 1
			if (current_target != "HIT"):
				check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)
			elif (number_of_ABMs <1 and current_target == "HIT"):
				print ('\033[7;30;91m'+'\t YOU HAVE RUN OUT OF ABMS AND CANNOT FIRE!'+'\033[0m')
				pauser(200)
				break
			your_ABM = random.randint(0,100)	 
			if (your_ABM in range (0,56)):
				print ('\033[44m'),
				if (current_target == "HIT"):
					pauser (200)
					print "\t* ANOTHER HIT! * Well done! You hit the same missile more than once!",
				else:
					pauser (500)
					print "\t \t ******   A HIT!  ******\t\t\t\t    ",

				print ('\033[0m')	# back to normal
				hits += 1
				abm_salvo = 0
				current_target = "HIT"
			else:
				print ('\033[0;30;47m'),	# white
				if (current_target == "HIT"):
					pauser (200)
					print "\t Your missile screams past the cloud of debris!!",
				else:
					pauser (500)
					print "\t ***** AAAARGH YOU MISSED! ABMS LEFT IN SALVO:",ABM_salvo,
				print ('\033[0m')	# back to normal
				misses += 1
		number_of_ICBMs -= 1
		enemy_salvo -= 1
		if (current_target != "HIT"):
			time.sleep(1)
			NuclearExplosion()
			nukeouts += 1

	time.sleep(1)
	enemy_salvoes +=1
	ABMs_ever = hits+misses
	print "\n\n"
	print ('\033[0;30;47m'),	# white
	print "\n ****************************************"
	print " *         POST BATTLE REPORT:          *"
	print " * Enemy missiles fired this round:",enemy_round,"\t*"
	print " * Total ABMs fired (ever):",ABMs_ever,"\t*"
	print " * Hits: (ever)",hits,"                   \t*"
	print " * Misses: (ever)",misses,"                \t*"
	print " * Total cities destroyed:",nukeouts,"    \t*"
	print " ****************************************\n"
	print "\n Please note that it is possible for more than one ABM to hit a single enemy missile\n"
	print ('\033[0m')	# back to normal
	print "\n\n\n"



try:
	cont = int(input("\n Press ENTER to continue"))
except:	
	print "",

if (nukeouts == 0):
	print "\n"
	print "\n"
	print ('\033[1;37;44m'+'\t\t YOU WIN - BIGLY! \t\t')
	print (''+'\033[0m')

	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+'  * * * * * * '+'\033[2;37;47m'+'                    '+'\033[0m')
	print ('\033[1;37;44m'+' * * * * * *  '+'\033[0;31;41m'+'                    '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print ('\033[2;37;47m'+'                                  '+'\033[0m')
	print ('\033[0;31;41m'+'                                  '+'\033[0m')
	print "\n\n YAAAAAY!! AMERICA HAS SURVIVED!!!"
	print "\n  YOU WIN AND ARE THE BEST PRESIDENT EVER!!!"
	print "\n Now the missile defence system has been proved"
	print "infallible, you can bomb all those OTHER places "
	print "you don't like! Where's your map and pin?"


else:
	print "\n\t\t  YOU LOSE!"
	print "\n"
	print ('\033[3;33;40m'+' Well, I hope you\'re pleased with yourself. Only'), nukeouts
	print " American cities have been blown to smithereens. "
	print "\n\n Of course, North Korea has been reduced to its constituent "
	print " atoms, so there's always that."
	print "\n"
	print " Still, you'll be able to build some nice hotels and resorts "
	print " once all the dead bodies have been cleared up! "
	print " "	
	print " BTW, some gentlemen from INTERPOL want to talk to you about "
	print " war crimes charges..."
	print "\n They blame YOU for starting the war, for some reason. "
	print " \n \t \t I know, right? Ingrates!"
	print ('\n'+'\033[0m')



print "\n\n"

try:
	cont = int(input("\n Press ENTER for the sleeve notes..."))
except:	
	print "",

print "\n \n    This game was inspired by Ankit Panda and Vipin Narang's article in"
print "  War On The Rocks and Carnegie Endowment For International Peace, "
print " \"Deadly Overconfidence: Trump Thinks Missile Defenses Work Against North Korea,"
print " and That Should Scare You"
print "\n Read it here:\n https://warontherocks.com/2017/10/deadly-overconfidence-trump-thinks-missile-defenses-work-against-north-korea-and-that-should-scare-you/"
print "\n Or here: \n http://carnegieendowment.org/2017/10/17/deadly-overconfidence-trump-thinks-missile-defenses-work-against-north-korea-and-that-should-scare-you-pub-73451"
print "\n\n"
print "\n If you have any CONSTRUCTIVE opinions to offer, please contact me via Twitter, "
print "where I go by @andywade"
print "\n\n"

try:
	cont = int(input("\n Press ENTER to exit..."))
except:	
	print "",

quit()





