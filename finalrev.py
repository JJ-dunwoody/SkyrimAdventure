import random

xpPoints = 0
banditXP = 0
swordEquip = 0
banditSwordEquip = 0

# in future, add resource bars like hp, mana, and corresponding spells that deduct from mana pool, or receive attacks that after a roll determine damage taken to which reduces hp bar value

validChoicesAB = ["a", "b"]
validChoicesYN = ["y", "n"]
keepGoing = [0,1]

def enterToContinue():
    input("Press [Enter] to continue...\n")

def deathEnding():
    input(f"\nYou died! The tale and adventure of {playerName} has come to an abrupt end!")

def dragonbornEnding():
    print("The Dragonborn has overcome all adversaries so far. They will go on to slay Alduin, Eater of Worlds. They will then go on to achieve great things and be cemented in history as a legend.")

def banditEnding():
    print(f"The Bandit has overcome all adversaries so far and even slew The Dragonborn. As a result there was no one who could stop Alduin, Eater of Worlds. In under a years time, Skyrim is plunged into an age of darkness. The Bandit is hunted until the end of his days for his transgression.")

def rollEnter():
    input("\nPress [Enter] to roll for odds!")




# what does f do? Ex: print(f"====")


print("\nWelcome to.........\n \n<<<<<<  A Day In Skyrim  >>>>>>\n")
enterToContinue()

# print("What is your name?\n")
# whatIsName = input()
# playerName = whatIsName

# print(f"Your name is {nameOfPlayer}!")

# in future, add pronouns identifier for player character gender in text, for now just assume all players created male playable character


# when game ends, I want to figure out how to restart game without having to re-input name or without having to press "Run Python File", and give option to end game with an input

def rollDice():
    dice1 = random.randint(1,10)
    dice2 = random.randint(1,10)

    total = dice1 + dice2
    print(f"\nYou rolled a {dice1} and a {dice2}!")
    print(f"You rolled a total of {total}!\n")
    return total


# TEST DICE (change dice values to guarantee a branch)
# def rollDice():
#     dice1 = random.randint(3,2)
#     dice2 = random.randint(2,2)

#     total = dice1 + dice2
#     print(f"\nYou rolled a {dice1} and a {dice2}!")
#     print(f"You rolled a total of {total}!\n")
#     return total

x = rollDice

def diceMessage():
    if x <= 4:
        print("-----Critical Failure!!!-----")
    elif x <= 10:
        print("-----Failure!-----")
    elif x <= 16:
        print("-----Success!-----")
    else:
        print("-----Wow!! Critical Success!!!-----")

# def playerStart():
#     x = rollDice
#     if x < 10:
#         return dragonbornRoute() == True
#     else:
#         return banditRoute() == False

# def dragonbornRoute():
#     print(f"The Nine Divines have decreed you worthy. You will be born as {playerName} the Dragonborn.")

# def banditRoute():
#     print(f"The Nine Divines have decreed you unworthy. You will be born as a {playerName} the Bandit.")

# if dragonbornRoute == True:
#     print("dragonborn")
# else:
#     print("bandit")
locationName = ["dungeon", "area"]

# validChoices = ["y", "n", "a", "b"]

# def tryAgainYN():
#     while userChoice not in validChoices:
#         userChoice = input("Enter Y/N").casefold()
#         if userChoice not in validChoices:
#             print("Stay within the script! Try again.")


print("Roll to determine birthright.")
rollEnter()
# rollDice()
# playerStart

# if banditRoute:
#     print("Bandit mode")
#     deathEnding()

# "sword + Lv2"
# "no sword + Lv2"
# "sword + Lv1"
# "no sword + Lv1"

def levelCheck():
    n = xpPoints
    m = banditXP
    if n == 50:
        print("==================\nYou have reached level 2!\n==================")
    elif m == 50:
        print("==================\nYou have reached level 2!\n==================")
    else:
        print("==================\nYou did not reach level 2.\n==================")

def continueToEnding():
    if swordEquip == 1 or banditSwordEquip == 1:
        print(f"\nYou leave the {locationName} with a sword in your inventory.\n")
    else:
        print(f"\nYou leave the {locationName} without having procured equipment.\n")
    enterToContinue()
    levelCheck()
    n = xpPoints
    m = banditXP
    print("The Dragonborn and a bandit meet at a crossroads. Due to the laws of nature both are instantly hostile toward each other.")
    if dragonbornPath == True:
        if swordEquip == 1 and n >= 50:
            print(f"{playerName} is equipped with a sword due to the choices of his path and The Dragonborn is Level 2! The Dragonborn slays the Bandit with his acquired knowledge and weaponry!\n")
            enterToContinue()
            dragonbornEnding()
        elif swordEquip == 1 and n < 50:
            print(f"{playerName} is equipped with a sword due to the choices of his path but The Dragonborn is not Level 2. The Dragonborn is slain by the Bandit!")
            enterToContinue()
            banditEnding()
        elif swordEquip == 0 and n >= 50:
            print(f"{playerName} is Level 2! But The Dragonborn was not able to arm himself due to the choices of his path. The Dragonborn is slain by the Bandit!")
            enterToContinue()
            banditEnding()
        elif swordEquip == 0 and n < 50:
            print(f"{playerName} was not able to arm himself due to the choices of his path and The Dragonborn is not Level 2. The Dragonborn is slain by the Bandit!")
            enterToContinue()
            banditEnding()
    elif dragonbornPath == False:
        if banditSwordEquip == 1 and m >= 50:
            print("The Bandit is equipped with a sword due to the choices of his path and The Bandit is Level 2! The Bandit slays the Dragonborn with his acquired knowledge and weaponry!\n")
            enterToContinue()
            banditEnding()
        elif banditSwordEquip == 1 and m < 50:
            print("The Bandit is equipped with a sword due to the choices of his path but The Bandit is not Level 2. The Bandit is slain by the Dragonborn!")
            enterToContinue()
            dragonbornEnding()
        elif banditSwordEquip == 0 and m >= 50:
            print("The Bandit is Level 2! But The Bandit was not able to arm himself due to the choices of his path. The Bandit is slain by the Dragonborn!")
            enterToContinue()
            dragonbornEnding()
        elif banditSwordEquip == 0 and m < 50:
            print("The Bandit was not able to arm himself due to the choices of his path and The Bandit is not Level 2. The Bandit is slain by the Dragonborn!")
            enterToContinue()
            dragonbornEnding()


if rollDice() <= 10:
    # ^^^^^^  () makes this function roll twice, why?
    print("The Nine Divines have decreed you unworthy.\n")
    dragonbornPath = False
    print("What is your name?\n")
    whatIsName = input()
    playerName = whatIsName + " The Bandit"
    if playerName == whatIsName + " The Bandit":
        locationName = "area"
    print(f"\nYou will be born as {playerName}.\n")
    print(f"===============\nLEVEL 1\nXP = [{banditXP}/50]\n===============\n")
    print(f"{playerName} wakes up in his crusty sleeping roll in Embershard Mine. {playerName} is part of a bandit group comprising of a bunch of low level individuals with one level 25 marauder in charge. Recent hauls from unsuccessful robberies and tomfoolery has not been enough to sustain the bandit group, so thus tensions are high amongst the savages. The bandit marauder takes a particular dislike to {playerName} and pins the stagnancy of the group's reputation on him. {playerName} doesn't particularly like the marauder either and is debating on whether he should:")
    cavePrompt = (f"\nA Stage a mutiny amongst the group and take over as leader\nB Leave the group and establish his own posse\n\nWhat should {playerName} do?\n")
    caveStart = cavePrompt
    while caveStart.casefold() not in validChoicesAB:
        caveStart = input(cavePrompt)
        if caveStart.casefold() in validChoicesAB:
            break
        else:
            print("\nStay within the script! Try again.\n")
    if caveStart.casefold() == "a":
        speechCheck = ("You gather the bandits to persuade them to rebel against the leader because you're bandits! You're incapable of critical thinking and only know how to pin the blame on others! Its never your fault! Attempt a speech check?\n(Y/N)\n")
        checkSpeechCheck = speechCheck
        while checkSpeechCheck.casefold() not in validChoicesYN:
            checkSpeechCheck = input(speechCheck)
            if checkSpeechCheck.casefold() in validChoicesYN:
                break
            else:
                print("\nStay within the script! Try again.\n")
        if speechCheck.casefold() == "y":
            while checkSpeechCheck.casefold() not in validChoicesYN:
                checkSpeechCheck = input(speechCheck)
                if checkSpeechCheck.casefold() in validChoicesYN:
                    break
                else:
                    print("\nStay within the script! Try again.\n")
        rollEnter()
        x = rollDice()
        if x <= 4:
            diceMessage()
            print("Your speech check fails. You stuttered over every word and couldn't even contain the spit from flying out of your mouth after every syllable. You even managed to insult half of the groups' mothers. How did you manage that? Anyways, the group jumped you and fed you to a nearby frost troll. It seems you really can't negotiate with terrorists.")
            deathEnding()
        elif x <= 10:
            diceMessage()
            print("You try to reason with the bandits through a rousing and elegant speech, but the bandits remember that you drank the last of the Honningbrew Mead from the secret stash. That stuff was to die for! Literally! Because you will die for drinking it. The bandits are going to kill you. Nords are more addicted to that stuff than the Khajits are to skooma! Mmmm... skooma.... Anyways, don't be a mead hogger. Lesson learned. Well you're dead so it doesn't matter really.")
            deathEnding()
        elif x <= 16:
            diceMessage()
            print("You performed well under pressure. Turns out you have a knack for public speaking! You appealed to the bandits' sense of id, ego and superego in a charismatic speech that turned heads and inspired deafeatists.")
            banditXP =0
            print(f"You gained 20 XP!\n===============\nLEVEL 1\nXP = [{banditXP + 20}/50]\n===============")
            print("All of you wait in ambush for the marauder leader to return from his giant's camp excursion so that you may slay him and acquire his mammoth cheese that he is sure to not share. The leader returns and everyone leaps from the shadows to put steel to his hide. Roll for combat effectiveness.")
            rollEnter()
            x = rollDice()
            if x > 11:
                diceMessage()
                print("The group successfully slays the leader. They then turn on you because well, they're bandits. What did you expect? Will you survive this onslaught of betrayal? By the way if you roll anything under a 12 it will be a critical failure. I mean you're fighting like 8 dudes all by yourself. Sorry.")
                rollEnter()
                x = rollDice()
                if x < 12:
                    print("-----Critical Failure!!!-----")
                    print("A cave bear hears all the commotion from the fighting and came to maul everyone. Everyone is mauled to death. The cave is reclaimed by the bear and balance is restored to nature. Yay nature!")
                    deathEnding()
                else:
                    diceMessage()
                    print("You put up a good fight despite being outnumbered. You gain useful combat experience.")
                    banditXP = 20
                    print(f"You gained 30 XP!\n===============\nLEVEL 1\nXP = [{banditXP + 30}/50]\n===============")
                    print("Suddenly, a giant cave bear appears! Sweet divine intervention! As the bear mauls everyone you take the chance to loot the shiny sword from the marauder and run outside of the cave in search for your next poor chum to rob. A bandit's life is never without excitement. And stealing. There's usually lots of stealing.")
                    banditSwordEquip =+ 1
                    m = banditXP
                    continueToEnding()
            else:
                print("-----Failure!!!-----")
                print("The leader still has a fresh coat of battle fervor from his fight with a giant. The momentum from that glorious battle and the Fortify One-Handed potion he drank has yet to wear off.  He easily wipes everyone out with a few swipes using his Elven Sword. You lay on the ground dying, wondering why you couldn't have been born as someone cool. Like a Dragonborn or something. Aw man.")
                deathEnding()
        elif speechCheck.casefold() == "n":
            while checkSpeechCheck.casefold() not in validChoicesYN:
                checkSpeechCheck = input(speechCheck)
                if checkSpeechCheck.casefold() in validChoicesYN:
                    break
                else:
                    print("\nStay within the script! Try again.\n")
            print("You decide against the speech check. You remain complacent and stagnant. The other bandits laugh at your cowardice so you decide to leave anyways. There is nothing left for you here so you take to the roads, hoping to try your luck on the next chump that cross your path.")
            continueToEnding()
    elif caveStart.casefold() == "b":
        print("\nYou decide to leave your old bandit buddies behind to start anew. You leave the cave and encounter a random hunter.")
        robHunter = input("Do you rob the hunter?\n(Y/N)\n")
        robHunterInput = robHunter
        if robHunter.casefold() == "y":
            while robHunterInput.casefold() not in validChoicesYN:
                robHunterInput = input(robHunter)
                if robHunterInput.casefold() in validChoicesYN:
                    break
                else:
                    print("\nStay within the script! Try again.\n")
            rollEnter()
            x = rollDice()
            if x <= 4:
                diceMessage()
                print("You demand the hunter to give you all his pelts and gold. The hunter is a retired Nightingale and plants an arrow between your eyes. The hunter also had a soul trap enchantment on his bow, so your soul will be imprisoned in a soul gem until the end of time. Hopefully you get used to enchant something cool. Skyrim is a weird place.")
                deathEnding()
            elif x <= 10:
                diceMessage()
                print("You demand the hunter to hand you all of his goods. The hunter is a retired Nightingale and thankfully in a good mood. So instead of obliterating you he tries to talk you out of being a bandit. You weren't listening because you had your eye on his cool shiny bow the entire time. You reach for the bow and in turn he exterminates you.")
                deathEnding()
            elif x <= 16:
                diceMessage()
                print("You demand the hunter to hand you his valuables and he cowers and agrees. Other bandits take notice and invite you into their group. You are now a member of a new bandit group! You take a brief rest at your new hideout, content with the progress you've made. You then head out to rob more chumps of their valuables.")
                banditXP = 0
                print(f"You gained 30 XP!\n===============\nLEVEL 1\nXP = [{banditXP + 30}/50]\n===============")
                m = banditXP
                continueToEnding()
            elif x <= 20:
                diceMessage()
                print("You command the fear of death into the hunter. The hunter falls dead from shock. Other bandits notice this and declare that you are not to be messed with. You gain a reputation as the King of Bandits.")
                banditXP = 0
                print(f"You gained 50 XP!\n===============\nLEVEL 1\nXP = [{banditXP + 50}/50]\n===============")
                m = banditXP
                continueToEnding()
        elif robHunter.casefold() == "n":
            print("By sparing the hunter, he notices your kind disposition and believes you can undergo a redemption arc to become something more than just a bandit. He gifts you a sword and urges you to acquire work as a guard at Whiterun. You take the sword and thank him, ready to use it to go rob the next poor fellow.")
            banditSwordEquip =+ 1
            continueToEnding()


else:
    print("The Nine Divines have decreed you worthy.\n")
    dragonbornPath = True
    print("What is your name?\n")
    whatIsName = input()
    playerName = whatIsName + " The Dragonborn"
    if playerName == whatIsName + " The Dragonborn":
        locationName = "dungeon"
    print(f"\nYou will be born as {playerName}.\n")
    print(f"===============\nLEVEL 1\nXP = [{xpPoints}/50]\n===============")
    # why is "print" or "input" not needed here in dungeonPrompt? 
    dungeonPrompt = (f"{playerName} wakes up in a dark and musty dungeon. {playerName} has a vague recollection of a wide skillset suited for a seasoned adventurer but suspect that they are inaccessible until you increase your XP level. {playerName} checks his inventory and sees that he somehow has one rusty lockpick. {playerName} looks at the jail door and determined that he may be able to pick the lock to freedom. Attempt lock? \n(Y/N)\n")
    dungeonStart = dungeonPrompt
    while dungeonStart.casefold() not in validChoicesYN:
        dungeonStart = input(dungeonPrompt)
        if dungeonStart.casefold() in validChoicesYN:
            break
        else:
            print("\nStay within the script! Try again.\n")
    if dungeonStart.casefold() == "y":
        rollEnter()
        x = rollDice()
        if x <= 4:
            diceMessage()
            print("You take the lockpick out of your inventory and it somehow disintegrates into dust! A skeever then comes out of nowhere and gnaws you to death! How did this even happen?!?! The Dragonborn has been slain! By a lowly rat type creature!\n")
            deathEnding()
        elif x <= 10:
            diceMessage()
            print("You take the lockpick out of your inventory and try to jimmy the keyhole. The lock breaks audibly. The guard nearby hears the commotion and throws a level 81 Fireball spell through the bars of the jail door! You get charred to a cinder and your body ragdolls and bounces on the confines of the jail cell's walls like a game of pong from the impact of the spell! How unfortunate as you haven't even learned your first warding spell yet! Whomp whomp! \n")
            deathEnding()
        elif x <= 16:
            diceMessage()
            print("You take the lockpick out of your inventory and try to jimmy the keyhole. Something clicks, metaphorically and physically and now you are free!\n")
            xpPoints = 0
            print(f"You gained 20 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 20}/50]\n===============")
            defendYourself = input("Although you were successful, the sleeping guard nearby was awakened by the sound of your lockpick scraping the mechanism. The guard approaches you, sword in hand. Do you defend yourself? \n(Y/N)\n")
            defendPrompt = defendYourself
            if defendPrompt.casefold() == "y":
                while defendPrompt.casefold() not in validChoicesYN:
                    defendPrompt = input(defendYourself)
                    if defendPrompt.casefold() in validChoicesYN:
                        break
                    else:
                        print("\nStay within the script! Try again.\n")
                rollEnter()
                x = rollDice()
                if x <= 4:
                    diceMessage()
                    print("Though unarmed, you remember you're still the Dragonborn! But sometimes that is not enough. You find yourself impaled on the guard's sword. You lay on the ground dying as you hear what sounds like the Greybeards guffawing at your incompetency as the child of prophecy. Oh well, maybe you'll get to see Sovngarde at least!")
                    deathEnding()
                elif x <= 10:
                    diceMessage()
                    print("You put your dukes up, ready to give the guard the fight of his life. You take a swing and miss! The guard side steps your attack and hacks at you with his sword. Does the attack connect?")
                    rollEnter()
                    x = rollDice()
                    if x <= 10:
                        diceMessage()
                        print("The attack swings clean through you! It was a critical hit. Your life flashes before your eyes as you fall through the ground. Your body clips through the ground because this is Skyrim. The guard starts eating a sweetroll.")
                        deathEnding()
                    else:
                        diceMessage()
                        print("The attack misses! The guard loses his balance mid swing and falls! You take the opportunity to land an uppercut straight into his jaw while he's falling, knocking him unconscious. The guard should have been wearing his helmet. You loot his sword and exit the dungeon.")
                        xpPoints = 20
                        print(f"You gained 10 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 10}/50]\n===============")
                        swordEquip =+ 1
                        print("You gained 1 sword!")
                        n = xpPoints
                        continueToEnding()
                elif x <= 16:
                    diceMessage()
                    print("Though unarmed, you remember you're still the Dragonborn! You successfully brawl the guard into unconsciousness. You retrieve the guard's sword and exit the dungeon unscathed.")
                    xpPoints = 20
                    swordEquip =+ 1
                    print("You gained 1 sword!")
                    print(f"You gained 20 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 20}/50]\n===============")
                    n = xpPoints
                    continueToEnding()
                elif x <= 20:
                    diceMessage()
                    print("You obliterate the guard with your bare fists. You're starting to remember how to do this. You loot the guard's sword and escape the dungeon.")
                    swordEquip =+ 1
                    print("You gained 1 sword!")
                    print(f"You gained 30 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 30}/50]\n===============")
                    n = xpPoints
                    continueToEnding()
            elif defendPrompt.casefold() == "n":
                print("You don't want to defend yourself! You curl up into fetal position! The guard laughs and kills you for being a coward!")
                deathEnding()
        elif x <= 20:
            diceMessage()
            print("You take the lockpick out of your inventory and try to jimmy the keyhole. Something clicks, metaphorically and physically and now you are free! You see a guard sleeping on a chair nearby. Due to how successful the lockpick process was, you virtually made no sound and as a result did not wake the guard up.\n")
            xpPoints = 0
            print(f"You gained 30 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 30}/50]\n===============")
            pickpocketGuard = input("Do you try to pickpocket the guard? \n(Y/N)")
            pickpocketPrompt = pickpocketGuard
            if pickpocketPrompt.casefold() == "y":
                while pickpocketPrompt.casefold() not in validChoicesYN:
                    pickpocketPrompt = input(pickpocketGuard)
                    if pickpocketPrompt.casefold() in validChoicesYN:
                        break
                    else:
                        print("\nStay within the script! Try again.\n")
                rollEnter()
                x = rollDice()
                diceMessage()
                if x >= 11:
                    print("You successfully pickpocketed the guard without waking him up! You retrieve his sword. You then sneak out of the dungeon successfully.")
                    xpPoints = 30
                    print(f"You gained 20 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 20}/50]\n===============")
                    swordEquip =+ 1
                    print("You gained 1 sword!")
                    n = xpPoints
                    continueToEnding()
            elif pickpocketPrompt.casefold() == "n":
                finalPickpocketAttempt = input("You come to the conclusion that you wouldn't be able to retrieve anything without waking him, but you really want that sword fixed on his belt scabbard. Do you proceed with the pickpocket attempt?\n(Y/N)")
                finalPrompt = finalPickpocketAttempt
                if finalPrompt.casefold() == "y":
                    while finalPrompt.casefold() not in validChoicesYN:
                        finalPrompt = input(finalPickpocketAttempt)
                        if finalPrompt.casefold() in validChoicesYN:
                            break
                        else:
                            print("\nStay within the script! Try again.\n")
                    print("You awaken the guard! He is very angry with your kleptomanic tendencies! He takes his sword out and hacks you to death! This ends the somber tale of a Dragonborn who is definitely NOT going to Sovngarde.")
                    deathEnding()
                elif finalPickpocketAttempt.casefold() == "n":
                    print("You decide not to risk your chances. After all escape is right on the precipice! You sneakily exit the dungeon.")
                    xpPoints = 30
                    print(f"You gained 10 XP!\n===============\nLEVEL 1\nXP = [{xpPoints + 10}/50]\n===============")
                    n = xpPoints
                    continueToEnding()
    elif dungeonStart.casefold() == "n":
        print("\nYou stay in the dungeon and rot until the end of days. The Nine Divines sneer at the thought of choosing someone so complacent. Like you could've been out there slaying dragons and collecting loot. What is your problem man?\n")
        deathEnding()               








# practice:
# print(f"{playerName}.You wake up. Your mouth feels filthy but you also need to excrete. What will you do?")
# wakingUp = input("====================\nA. Brush your teeth\n====================\nB. Take a dump\n====================\n\n")


# x = sumOfDice()


# what do the () mean when put in front of functions? What does it change when there is no ()?
    # Ex. diceMessage()   vs   diceMessage


# rollEnter()


# if wakingUp.casefold() == "a":
#     x = rollDice()
#     if x <= 4:
#         diceMessage()
#         print("All your teeth falls out.\n")
#     elif x <= 10:
#         diceMessage()
#         print("You're out of toothpaste!\n")
#     elif x <= 16:
#         diceMessage()
#         print("Wow your breath smells good!\n")
#     elif x <= 20:
#         diceMessage()
#         print("WOWOWOWOWOWWOWOWOW!\n")
# elif wakingUp.casefold() == "b":
#     print("You take a dump.")
