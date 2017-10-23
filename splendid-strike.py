#!/usr/bin/python

import os
import time
import random
from random import randint

#################### VARIABLES ##############
cities = ["Albany, New York", "Air Force Academy", "Akron, Ohio", "Alameda, California", "Alamo, Texas", "Alamogordo, New Mexico", "Alice, Texas", "Andrew AFB, Maryland", "Angola, Indiana", "Annapolis, Maryland", "Back Mountain, Pennyslavania", "Bailey's Crossroads, Virginia", "Bainbridge, Georgia", "Baker City, Oregon", "Bakersfield, California", "Baltimore, Maryland", "Bangor, Maine", "Bangor Trident Base, Washington", "Banning, California", "Barstow, California", "Barnstaple Town, Massachusets", "Boston, Massachusets", "Barrington, New Hampshire", "Bartlett, Illinois", "Bella Vista, Arkansas", "Bellvue, Kentucky", "Belmont, California", "Brownsville, Tennesee", "Cabot, Arkansas", "Cadillac, Michigan", "Caledonia, Winscosin", "California City, California", "Cambridge, Maryland", "Cambridge, Massachusets", "Camnden, New Jersey", "Campbell, Ohio", "Canby, Oregon", "Canton, Missisipi", "Carmel, Indiana", "Carson City, Nevada", "Carthage, Texas", "Cedar Falls, Iowa", "Chubbuck, Idaho", "Cicero, New York", "Clinton, South Carolina", "Clovis, New Mexico", "Colorado Springs, Colorado", "Concord, Missouri", "Coolidge, Arizona","Damascus, Maryland", "Danville, Virginia", "De Soto, Missouri", "Dearborn, Michigan", "Defiance, Ohio", "Delano, California", "Derby, Colorado", "Des Moines, Iowa", "Dexter, Missouri", "Discovery Bay, California", "Douglas, Arizona", "Duncan, Oklahoma", "Eagle, Idaho", "East Bridgewater, Massachusets", "East Hampton, Conneticut", "East Ridge, Tennesee", "East St. Louis, Illinois", "Easton, Conneticut", "Eglin AFB, Florida", "El Paso, Texas", "El Rio, California", "El Segundo, California", "Elwood, Indiana", "Essex, Vermont", "Exeter, California", "Fair Lawn, New Jersey", "Fairfield, Conneticut", "Fremont, California", "Fallon, Nevada", "Fargo, North Dakota", "Fayetteville, North Carolina", "Ferndale, Maryland", "Five Corners, Washington", "Florence, Alabama", "Forest Hills, Pennyslavania", "Fort Stewart, Georgia", "Foster City, California", "Fox Lake, Illinois", "Franklin, New Hampshire", "Fredonia, New York", "Fresno, California", "Friendly, Maryland", "Fulton, Missouri","Gaffney, South Carolina", "Gallup, New Mexico", "Gary, Indiana", "Gatesville, Texas", "Gladstone, Oregon", "Glasgow, Delaware", "Glenview, Illinois", "Gonzales, Texas", "Grand Island, Nebraska", "Grand Prairie, Texas", "Greater Upper Marlboro, Maryland", "Green Bay, Winscosin", "Greenfield, Indiana", "Greer, South Carolina", "Gresham, Oregon", "Guilford, Conneticut", "Gurnee, Illinois", "Hacienda Heights, California", "Hackensack, New Jersey", "Hannibal, Missouri", "Hanover, New York", "Hartford, Vermont", "Hawaiian Paradise Park, Hawaii", "Henderson, North Carolina", "Hillsboro, Oregon", "Holland, Michigan", "Hollins, Virginia", "Hoover, Alabama", "Hope, Arkansas", "Hudson, Massachusets", "Huntsville, Kentucky", "Huron, California", "Hyrum, Utah", "Idaho Falls, Utah", "Inkster, Michigan", "Inverness, Florida", "Isla Vista, California", "Irvington, New York", "Ives Estates, Florida", "Jacinto City, Texas", "Jackson, Ohio", "Jasper, Alabama", "Jefferson, Winscosin", "Jessup, Maryland", "Junction City, Kansas", "Justice, Illinois", "Katy, Texas", "Kenai, Alaska", "Kendale Lakes, Florida", "Kerrville, Texas", "Kettering, Maryland", "Kingsburg, California", "Kulpsville, Pennyslavania", "Detroit, Michigan", "Flint, Michigan", "La Riviera, California", "La Puente, California", "Lake Arbour, Maryland", "Lysander, New York", "New York, New York", "Dallas, Texas", "Los Angeles, California", "San Francisco, California", "Chicago, Illinois", "Fort Knox, Kentucky", "Fort Lauderdale, Florida", "Washington DC,", "Houston, Texas", "Las Vegas, Nevada"] 



shortlist = [ "New York, New York", "Dallas, Texas", "Los Angeles, California", "San Francisco, California", "Chicago, Illinois", "Fort Knox, Kentucky", "Fort Lauderdale, Florida", "Washington DC", "Houston, Texas", "Las Vegas, Nevada" ]

_ICBM_ratio = 0
number_of_ABMs = 44			# Yes, this is really the number of ABMs the USA has.
number_of_ICBMs = random.randint(1,20)	# Let's generate between 1 and 20 enemy warheads
ICBMs_in_entire_war = number_of_ICBMs
hits = 0
misses = 0
enemy_salvoes = 1
begin = ""
nukeouts = 0
current_target = ""
russian_roulette = random.randint(0,100)

###################### SUBROUTINES #####################################


def pauser(loops):
	loops *= 1000
	while (loops > 0):
		loops -=1
	return




def other_side_effects(nukeouts,ICBMs_in_entire_war):

#	print "nukeouts:", nukeouts
#	print "ICBMS in war:", ICBMs_in_entire_war

	shot_down_ICBMs = (ICBMs_in_entire_war - nukeouts)	
	chance_of_kessler = random.randint(0,shot_down_ICBMs)

#	print "shot down ICBMs:",shot_down_ICBMs
#	print "chance of Kessler:",chance_of_kessler
	if (chance_of_kessler > 6):
		print "\n You have shot down so many ICBMs that they have collided with"
		print " other objects in space to cause the dreaded ABLATION CASCADE"
		print " (AKA Kessler Syndrome), essentially the debris from your little"
		print " war has crashed into orbiting satellites, blowing them to bits."
		print " The bits have in turn smashed into other satellites, a result of "
		print " which is, we can no longer use our satellites or launch new ones."
		print "\n In fact, space will be inaccessible for many decades, perhaps ";
		print " even centuries, to come. That's right, no more Fox News for you!"

	if (shot_down_ICBMs > 0):
		print "\n Also, the plutonium and uranium from the",shot_down_ICBMs,"ICBMs"
		print " you shot down is raining down on Earth, causing "
		print " environmentalists to become upset and slowly giving "
		print " everyone cancer. Fake News!"
	if (nukeouts > 0):
		print "\n Even worse, Twitter have banned you for violating their "
		print " Terms Of Service!"

	
		
def PressEnter():
	try:
		cont = int(input("\n Press ENTER to continue..."))
	except:	
		print "",


def NuclearExplosion():
	print "AAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGGGGHHHHHHHHHHHH!!!!"
#	print ('\033[6;37;47m'+' ');
	print ('\033[0;37;47m'+'                                  ')	
	print "\n\n\n"
	print ('\033[0;37;47m'+'                                  ')
	print ('\033[2;29;97m'+'                ********')
	print ('\033[2;37;47m'+'               **********')
	print ('\033[1;32;47m'+'              ')
	print ('\033[0;31;47m'+'             *************')
	print ('\033[0;31;47m'+'          ********************')
#	print ('\033[0;31;47m'+'       ************************')
	print ('\033[6;31;47m'+'       ***********'+'\033[6;1;47m'+'**'+'\033[6;2;47m'+'***********')
	print ('\033[6;31;47m'+'      ************'+'\033[6;1;47m'+'****'+'\033[6;2;47m'+'**********')
	print ('\033[6;31;47m'+'     ****************************')
	print ('\033[3;37;47m'+'         *********************')
	print ('\033[2;31;47m'+'                 *****')
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
	print ('    ******************************* '+'\033[0m')
	print "      KABOOOOOOOOOOOOOOOOOOOOOOM!"
	print ('\033[0;37;47m'+'                                  ')	
	print ('\033[0;37;47m'+'                                  ')	
	print ('\033[0m')
	



def check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts):
	if (number_of_ABMs < 0 and number_of_ICBMs >0):

		print ('\033[0;30;41m'+'\t   YOU HAVE RUN OUT OF ABMS!            '+'\033[0m')
		print ('\033[1;33;41m'+'\t Unfortunately, the enemy has not...    '+'\033[0m')

		nukeouts += number_of_ICBMs
		loop = 0
		pauser (40000)

		if (number_of_ICBMs > 30):
			while (loop < nukeouts):
				spinner = random.randint (0,(len(cities)))
				spinner -= 1
				city = cities[spinner]
				print "Target #",loop,",",city,":"
				NuclearExplosion()
				loop +=1
				pauser(100)

		else:
			while (loop < nukeouts):
				spinner = random.randint (0,(len(shortlist)))
				spinner -= 1
				city = shortlist[spinner]
				print "Target #",loop,",",city,":"
				NuclearExplosion()
				loop +=1
				pauser(500)			
#		pauser (40000)
#		print "    KABOOOOOOOOOOOOOOOOOOOOOOM!\n\n ";
		print "   ",nukeouts,
		print "American cities have been destroyed!",
		print ('\033[3;33;40m'+' ')
		print "\n MILLIONS of people are dead, many of whom voted for YOU!"
#		print "DEBUG: Before call: Nukeouts;",nukeouts,"ICBMs in war:",ICBMs_in_entire_war
		other_side_effects(nukeouts,ICBMs_in_entire_war)
		print ('\n  Oh, woe, woe, woe is you! It\'s just so UNFAIR and FAKE!'+'\033[0m')
#		print "\n";
		if (nukeouts > 30):
			print ('\033[3;33;40m'+' ')
			print " It gets even worse STILL. Nuclear winter turns the planet into a "
			print " hellish, radioactive iceball. The skies turn black. Nothing can live. "
			print "\n As a result, Mar-A-Lago and your other very fine resorts are completely "
			print " snowed under. Your guests are very cross and demand their money back."
			print " YOU ARE FINANCIALLY RUINED, and because everyone else is dead, there is "
			print " nobody left alive to bail you out."
			print "\n You spend the rest of your life eating baked beans and Spam in a "
			print " very classy nuclear bunker, which very soon smells unbearable. Outside, "
			print " MEXICANS have taken over, cleared all the dead bodies away, and turned"
			print " the USA into a massive ski resort."
			print ('\033[0m')

		print " \t \t GAME OVER \n";
		quit();


############################### main_loop ########################################

def main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits,ICBMs_in_entire_war):
	pauser (100)
	enemy_salvo = random.randint(1,number_of_ICBMs)
	print ('\033[91m'+'\n \t ')
	print "\t *** There are ",enemy_salvo, "ICBMs incoming! ***"
	print (' '+'\033[0m'),
	print "    This is the ",enemy_salvoes,
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

	print "\n   You have ",number_of_ABMs,
	print "ABMs left."
	number_of_ICBMs -= enemy_salvo

	if (number_of_ICBMs > 0):
		print "\n   Intelligence indicates that They will still have another",number_of_ICBMs
		print "   ICBM(s) left in reserve after this attack."
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
		print ('\033[0;30;42m'+'  Firing ABMS... fingers crossed! '+'\033[0m')	# green
		print ('\033[0;30;42m'+'ABMs:'),
		print number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts,
		print ('\033[0m')
#		print ('ABMs:',number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts+'\033[0m')
#		print ('ABMs:',number_of_ABMs,'  ICBMs:',number_of_ICBMs,'  nukeouts:',nukeouts+'\033[0m')
		check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)	

		while (ABM_salvo >0):
			time.sleep(1)
			ABM_salvo -= 1
			number_of_ABMs -= 1
			if (current_target != "HIT"):
				check_if_out_of_ABMs(number_of_ABMs, number_of_ICBMs, nukeouts)
			elif (number_of_ABMs < 0 and current_target == "HIT"): # Obscure bug, gaffa taping it
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

		if (number_of_ABMs < 0):	# Obscure bug, 2nd part of fix
			number_of_ABMs = 0	# 
		number_of_ICBMs -= 1
		enemy_salvo -= 1
		if (current_target != "HIT"):
			time.sleep(1)
			spinner = random.randint (0,(len(shortlist)))
			spinner -= 1
			city = shortlist[spinner]
			print "Target:",city,":"
			NuclearExplosion()
			nukeouts += 1

	time.sleep(1)
	enemy_salvoes +=1
	ABMs_ever = hits+misses
#	hits_this_round = hits
#	misses_this_round = misses
	print "\n\n"
	print ('\033[0;30;47m'),	# white
	print "\n ****************************************"
	print " *         POST BATTLE REPORT:          *"
	print " * Total number of enemy missiles:",ICBMs_in_entire_war,"\t*"
	print " * Enemy missiles fired this round:",enemy_round,"\t*"
	print " * Enemy missiles left:",number_of_ICBMs,"\t\t*"
	print " * ABMS left:",number_of_ABMs,"\t\t\t*"
	print " * Total ABMs fired (ever):",ABMs_ever,"\t\t*"
	print " * Hits: (this round)",hits,"\t\t*"
	print " * Misses: (this round)",misses,"\t\t*"
	print " * Total cities destroyed:",nukeouts,"    \t*"
	print " ****************************************\n"
	print "\n Please note that it is possible for more than one ABM to hit a single enemy missile\n"
	print ('\033[0m')	# back to normal
	print "\n\n\n"
	return (number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts)




############################ MAIN PROGRAM #######################################

print "\n\n\n\n\n\n\n\n\n"
#print "RR:",russian_roulette
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
print ('\033[3;33;40m'+'  It\'s a nice, quiet day. You\'re just discussing the issues of the  '+'\033[0m')
print ('\033[3;33;40m'+'  day with your fans and trolling losers, Commies and Rocket Man on  '+'\033[0m')
print ('\033[3;33;40m'+'  Twitter while fiddling around with your special briefcase, when')
print ('  all of a sudden everyone completely loses it! '+'\033[0m')
print ('\033[3;33;40m'+'\n  An aide pops his head round the door and tells you in a breathless voice\n '+'\033[0m')
print "\t",
print ('\033[7;30;91m'+'   NUKES!!! COMMIE NUKES COMIN\' TO GET US!! '+'\033[0m')
print "";
print ('\033[3;33;40m'+'  You run to the desk of the Oval Office, where you had a computer terminal'+'\033[0m')
print ('\033[3;33;40m'+'  installed that connects you to the missile defence system.'+'\033[0m')
print ('\033[3;33;40m'+'\n  This allows YOU to control America\'s defences. You have the best and'+'\033[0m')
print ('\033[3;33;40m'+'  bigliest defences - and as the smartest, bravest, cleverest person in'+'\033[0m')
print ('\033[3;33;40m'+'  the whole wide world, YOU are the only one who knows how to beat those '+'\033[0m')
print ('\033[3;33;40m'+'  dirty Commies and SAVE AMERICA!'+'\033[0m')
print "";
print ('\033[3;33;40m'+'  Each ABM you fire has a 56% chance of hitting the enemy missiles that are '+'\033[0m')
print ('\033[3;33;40m'+'  raining down on God\'s Country like dollar bills on a stripper in one of '+'\033[0m')
print ('\033[3;33;40m'+'  your very classy entertainment resorts. '+'\033[0m')
print ""
print ('\033[3;33;40m'+'  You can fire these singly or in salvoes, but because the enemy missiles '+'\033[0m')
print ('\033[3;33;40m'+'  come in SO DARNED FAST, you have to tell the computer how many ABMs to'+'\033[0m')
print ('\033[3;33;40m'+'  fire at each enemy ICBM in advance.'+'\033[0m')
print ('\033[3;33;40m'+'\n\t  THE FATE OF THE WORLD IS IN YOUR GIANT, ENORMOUS HANDS!'+'\033[0m')
#print "\n";

try:
	cont = int(input("\n Press ENTER to start the game!"))
except:	
	print "",


print ""
#print "  OK, I hope you're ready... starting in ",
#print "3...",
#Print "2...",


print "\n\n\n"

print "\t\t ******************************"
print "\t\t *",
print ('\033[91m'+' WARNING! MISSILE ALERT!'+'\033[0m'),
#print ('\033[6m'+' WARNING! MISSILE ALERT!'+'\033[0m'),


print " *"
print "\t\t ******************************"
while (number_of_ICBMs > 0):
	(number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts) = main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits, ICBMs_in_entire_war)


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
	print "\n\n      YAAAAAY!! AMERICA HAS SURVIVED!!!"
	print "\n   YOU WIN AND ARE THE BEST PRESIDENT EVER!!!"
	print "\n Now the missile defence system has been proved"
	print " infallible, you can bomb all those OTHER places "
	print " you don't like! Where's your map and pin?"
	other_side_effects(nukeouts,ICBMs_in_entire_war)
	print "\n";

	if (russian_roulette > 15):
		PressEnter()
		print "\n\n\n"
		print "\n\n\n\n"
		print "\t\t\t BUT THEN....\n";
		print "\n Your partying is interrupted by the sound of a "
		print ('\033[7;30;91m'+'               VERY LOUD KLAXON!                '+'\033[0m')
		print ""
		print " The ",
		print ('\033[91m'+'BIG RED PHONE'+'\033[0m'),
		print " is ringing. You scoop it up"
		print "  with your massive hands and who should it "
		print " be but YOUR BOSS, Vladimir Putin!"
		print "\n"
		print " He is extremely distraught and yells at you "
		print ""
		print ('\033[1;37;44m'+'  \"What the f*** do you think you\'re doing you '+'\033[0m')
		print ('\033[7;30;91m'+'   f**ing c*cks*ck*r? I told you - don\'t F*CK  '+'\033[0m')
		print ('\033[0;30;47m'+'         with Mutha Russia!!!!\"                '+'\033[0m'),
		print ""
		print " Putin slams the phone down and you look up into "
		print " the panicked face of yet another aide."
		print ""
		print "  \"Mr. President, sir, it seems the Russians "
		print "    mistook our ABM launches for an attack! "
		print "       We gotta get ya to safety sir! \""
		print " "
		print ('\033[3;33;40m'+' \"No time for that, Boy\"'+'\033[0m')+' you growl,',
		print ('\033[3;33;40m'+'\"I\'ll handle this!\"'+'\033[0m')
		print "\n\n"
		PressEnter()
		print "\n\n\n\n\n"
		print "\t\t ******************************"
		print "\t\t *",
		print ('\033[91m'+' WARNING! MISSILE ALERT!'+'\033[0m'),
		print " *"
		print "\t\t ******************************"
		number_of_ICBMs = random.randint(299,1801)
		ICBMs_in_entire_war = number_of_ICBMs
		enemy_salvoes = 1
		while (number_of_ICBMs > 0):
			(number_of_ICBMs,number_of_ABMs,enemy_salvoes,nukeouts) = main_loop(number_of_ICBMs, enemy_salvoes, number_of_ABMs, nukeouts, misses, hits, ICBMs_in_entire_war)
	else:
		print " Best of all, nobody has observed your missiles flying"
		print " over a certain large Eurasian country and concluded that"
		print " you were attacking them. You were always a winner, now"
		print " even your most ardent critics will have to shut up."
		print "\n Mostly because you will shoot them if they don't."


		


else:
	print "\n\t\t  YOU LOSE!"
	print ""
	print ('\033[3;33;40m'+' Well, I hope you\'re pleased with yourself. Only'), nukeouts
	print " American cities have been blown to smithereens. "
	other_side_effects(nukeouts,ICBMs_in_entire_war)
	print "\n Of course, North Korea has been reduced to its constituent "
	print " atoms, so there's always that."
	print "\n"
	print " Still, you'll be able to build some nice hotels and resorts "
	print " once all the dead bodies have been cleared away! "
	print " "	
	print " BTW, some gentlemen from INTERPOL want to talk to you about "
	print " war crimes charges..."
	print "\n They blame YOU for starting the war, for some reason. "
	print " \n \t \t I know, right? Ingrates!"
	print (''+'\033[0m')



#print "\n"

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
print "\n Also, see this: https://www.thedailybeast.com/how-a-north-korean-missile-could-accidentally-trigger-a-us-russia-nuclear-war"
print "\n If you have any CONSTRUCTIVE opinions to offer, please contact me via Twitter, "
print "where I go by @andywade"
print "\n\n"

try:
	cont = int(input("\n Press ENTER to exit..."))
except:	
	print "",

quit()





