# 2020-10-06 -- 2020-10-09
# Casino Games Assinment
# purpose of program: To create a set of casino games in python
import time
import random
import sys
superHardStartJackpot = 1200
line = "------------------------------"
levels ="-----------levels------------"
line2 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
line3 = "=============================="
win2 = "---------------$2-------------"
win1 = "--------------$50-------------"
win3 = "~~~~~~~~~~~~~$100~~~~~~~~~~~~~"
win4 = "#############$200#############"
greetings = ["Good day", "Howdy", "Hey", "Hi", "Whats up", "Good to see you"]
# generate greeating
randomGreeting = random.choice(greetings)
print("~~~~Casino Games.TRM~~~~")
time.sleep(1)
print("~~~~Hello and thank you for coming to casino.TRM, please pick from the menu below~~~~\n")
print("~~~~Menu~~~~\n1.Slot Machine\n2.Roulette\n3.Fortune Teller")
time.sleep(1)
menuChoice = int(input("\nEnter your choice (#): "))
time.sleep(1)
name = input("Before we start my name is Danny, what is yours: ")
name = name.capitalize()

# chioce 1 -- slot machine
if menuChoice == 1: 
  print(randomGreeting,name,", thank you for choosing the slot machine, I will be your host for today.")
  time.sleep(1)
  print("Please pick a level below: (psst I hope to see you pick super hard)\n")
  for x in levels:
    print(x, end= '')
    sys.stdout.flush()
    time.sleep(0.1)
  levelChoice = int(input("\n1.Easy (Jackpot: $50)\n2.Medium (Jackpot: $100)\n3.Hard (Jackpot: $200)\n4.Super Hard (Jackpot: $1200 Starting) (#) : "))
  # slot level choice 1 - easy
  if levelChoice == 1:
    time.sleep(1)
    print("\nWelcome to the easy slots, the goal is to get at least 2 symbols matched")
    input("Ok I am ready, are you? Press enter to spin...")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    spinChoice = ["#", "@"]
    # generate wheel symbols
    wheel1 = random.choice(spinChoice)
    wheel2 = random.choice(spinChoice)
    wheel3 = random.choice(spinChoice)
    print("\n\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\n\t---\t---\t---")

    # if all the wheels match
    if wheel1 == wheel2 == wheel3:
      for x in win1:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nGreat job if I dont say so myself, you won the jackpot $50.\nHope to see you around here soon, bye :)")
    # if only two match
    elif wheel1 == wheel2 or wheel1 == wheel3 or wheel2 == wheel1 or wheel2 == wheel3 or wheel3 == wheel1 or wheel3 == wheel2:
      for x in win2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nWow, you won $2 for matching 2 symbols, thanks for playing hope to see you around soon!")
    # if program dosent work
    else:
      print("Sorry we could not prosess your request")

  # slot level choice 2 - medium
  elif levelChoice == 2:
    time.sleep(1)
    print("\nWelcome to the medium slots, the goal is to get at least 2 symbols matched")
    input("Ok I am ready, are you? Press enter to spin...")
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    spinChoice = ["$", "%", "&"]
    # generate wheel symbols
    wheel1 = random.choice(spinChoice)
    wheel2 = random.choice(spinChoice)
    wheel3 = random.choice(spinChoice)
    print("\n\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\n\t---\t---\t---")

    # if all the wheels match
    if wheel1 == wheel2 == wheel3:
      for x in win3:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nGreat job if I dont say so myself, you won the jackpot $100.\nHope to see you around here soon, bye :)\n")
    # if only two wheels match
    elif wheel1 == wheel2 or wheel1 == wheel3 or wheel2 == wheel1 or wheel2 == wheel3 or wheel3 == wheel1 or wheel3 == wheel2:
      for x in win2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nWow, you won $2 for matching 2 symbols, thanks for playing hope to see you around soon!")
    # if program dosent work / dosent match anything
    else:
      print("Oh no, you matched none, you lost! bye :(")

  # slot level choice 3 - hard
  elif levelChoice == 3:
    time.sleep(1)
    print("\nWelcome to the hard slots, the goal is to get at least 2 symbols matched")
    input("Ok I am ready, are you? Press enter to spin...")
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    spinChoice = ["$", "%", "&", "@"]
    # generate wheel symbols
    wheel1 = random.choice(spinChoice)
    wheel2 = random.choice(spinChoice)
    wheel3 = random.choice(spinChoice)
    print("\n\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\n\t---\t---\t---")

    # if all the wheels match
    if wheel1 == wheel2 == wheel3:
      for x in win3:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nGreat job if I dont say so myself, you won the jackpot $200.\nHope to see you around here soon, bye :)\n")
    # if only two wheel match
    elif wheel1 == wheel2 or wheel1 == wheel3 or wheel2 == wheel1 or wheel2 == wheel3 or wheel3 == wheel1 or wheel3 == wheel2:
      for x in win2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nWow, you won $2 for matching 2 symbols, thanks for playing hope to see you around soon!")
    # if program dosent work / match none 
    else:
      print("Oh no, you matched none, you lost! bye :(")

  # slot level choice 4 bonus - super hard
  elif levelChoice == 4:
    spinChoice = ["$", "%", "&", "@", "�", "!", "?"]
    humanBet = 0
    dannyBet = 0
    time.sleep(1)
    print("\nWelcome to the Super hard slots, nice too see you here. I love this version of slots, oh and did I forget to tell you this is a betting game.\nThere are 5 wheels, and 7 symbols on each, First we place our bet (You have to atleast bet on the first spin, otherwise put 0) on top of the entry jackpot, then one wheel spins and we repeat the process until the last wheel.\nGood luck!!\nThe jackpot is at $",superHardStartJackpot,"\n\n- If you get all 5 wheels to match you get jackpot\n- If you get the first 4 wheels to match then you get half of the jackpot\n- If you get wheel 1, wheel 3 and wheel 5 matching you win $200\n- If you get anything else you solve a question, if you get it right you get $50 if you get it wrong you get $0")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    bet1 = float(input("\nOk now that you know the starting jackpot what would you like to bet: $"))
    jackpot = superHardStartJackpot + bet1
    time.sleep(1)
    # if bet is less than 50
    if bet1 < 50:
      jackpot = jackpot + 10
      humanBet = humanBet + bet1
      dannyBet = dannyBet + 10
      print("Ok... Good bet, I am going to start off with $10 that brings the total jackpot to $",jackpot)
    # else bet
    else:
      humanBet = humanBet + bet1
      dannyBet = dannyBet + 105
      jackpot = jackpot + 105
      print("Great bet! I am going to start us off with $105 that brings the total jackpot to $",jackpot)
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    time.sleep(1)
    # generate wheel 1 symbol
    wheel1 = random.choice(spinChoice)
    print("\n\t---\n\t",wheel1,"\n\t---")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)

    bet2 = float(input("\nNow that we know what the first wheel is, place your bet for the second bet $"))
    jackpot = jackpot + bet2
    # if bet is 0
    if bet2 == 0:
      print("Oh.... I won't bet anything either")
    # if bet is less than 100
    elif bet2 < 100:
      humanBet = humanBet + bet2
      dannyBet = dannyBet + 200
      jackpot = jackpot + 200
      print("Ok... I will bet $200, that brings the total jackpot to $",jackpot)
    # else bet
    else:
      humanBet = humanBet + bet2
      dannyBet = dannyBet + 130
      jackpot = jackpot + 130
      print("Thats a great bet!! I am betting $130, that brings the total jackpot to $",jackpot)
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    time.sleep(1)
    # generate wheel 2 symbol
    wheel2 = random.choice(spinChoice)
    print("\n\t---\t---\n\t",wheel1,"\t",wheel2,"\n\t---\t---")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)

    bet3 = float(input("\nOk... Time to bet agian, this game is so instance I love it. What do you want to bet $"))
    jackpot = jackpot + bet3
    # if bet is 0
    if bet3 == 0:
      print("Oh.... I won't bet anything either")
    # if bet is less than 100
    elif bet3 < 100:
      humanBet = humanBet + bet3
      dannyBet = dannyBet + 100
      jackpot = jackpot + 100
      print("Ok... I will bet $100, that brings the total jackpot to $",jackpot)
    # else bet
    else:
      humanBet = humanBet + bet3
      dannyBet = dannyBet + 300
      jackpot = jackpot + 300
      print("Thats a great bet!! I Am betting $300, that brings the total jackpot to $",jackpot)
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    time.sleep(1)
    # generate wheel 3 symbol
    wheel3 = random.choice(spinChoice)
    print("\n\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\n\t---\t---\t---")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)

    bet4 = float(input("\nOk... Time to bet agian, what do you want to bet $"))
    jackpot = jackpot + bet4
    # if bet is 0
    if bet4 == 0:
      print("Oh.... I won't bet anything either")
    # if bet is less than 100
    elif bet4 < 200:
      humanBet = humanBet + bet4
      dannyBet = dannyBet + 300
      jackpot = jackpot + 300
      print("Ok... I will bet $300, that brings the total jackpot to $",jackpot)
    # else bet
    else:
      humanBet = humanBet + bet4
      dannyBet = dannyBet + 500
      jackpot = jackpot + 500
      print("Thats a great bet!! I Am betting $500, that brings the total jackpot to $",jackpot)
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    time.sleep(1)
    # generate wheel 4 symbol
    wheel4 = random.choice(spinChoice)
    print("\n\t---\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\t",wheel4,"\n\t---\t---\t---\t---")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)

    bet5 = float(input("\nOk... Time to bet agian, what do you want to bet $"))
    jackpot = jackpot + bet4
    # if bet is 0
    if bet5 == 0:
      print("Oh.... I won't bet anything either")
    # if bet is less than 100
    elif bet5 < 100:
      humanBet = humanBet + bet5
      dannyBet = dannyBet + 100
      jackpot = jackpot + 100
      print("Ok... I will bet $500, that brings the total jackpot to $",jackpot)
    # else bet
    else:
      jackpot = jackpot + 200
      humanBet = humanBet + bet5
      dannyBet = dannyBet + 200
      print("Thats a great bet!! I Am betting $200, that brings the total jackpot to $",jackpot)
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    time.sleep(1)
    # generate wheel 5 symbol
    wheel5 = random.choice(spinChoice)
    print("\n\t---\t---\t---\t---\t---\n\t",wheel1,"\t",wheel2,"\t",wheel3,"\t",wheel4,"\t",wheel5,"\n\t---\t---\t---\t---\t---")
    for x in line:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)

    # if all the wheels match
    if wheel1 == wheel2 == wheel3 == wheel4 == wheel5:
      lineJackpot = "~~~~~~~~~~~~~~~$",jackpot,"~~~~~~~~~~~~~~"
      for x in lineJackpot:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nWow Wow Wow, you won the jackpot $",jackpot,"\nYou won my $",dannyBet,"I put in this game")
    # if only the first 4 wheeels match
    elif wheel1 == wheel2 == wheel3 == wheel4:
      for x in line2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      jackpot = jackpot / 2
      dannyBet = dannyBet / 2
      print("\nWow, you won $",jackpot,"for matching the first 4 symbols,You won",dannyBet,"half of what i put in to this game, thanks for playing hope to see you around soon!")
    # if 1, 3, 5 match
    elif wheel1 == wheel3 == wheel5:
      for x in line2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      print("\nWow, you won $200 for matching wheel 1, 3 and 5, thanks for playing hope to see you around soon!")
    # if no wheels match 
    else:
      print("\nWelcome to the last step, the riddle, here is an example (Question: What is always in front of you but can’t be seen, Answer: Future) not a question :)")
      question = ["What has to be broken before you can use it?", "I’m tall when I’m young, and I’m short when I’m old. What am I?", "What is full of holes but still holds water?", "What gets wet while drying?", "I shave every day, but my beard stays the same. What am I?"]
      question1Answer = "egg"
      question2Answer = "candle"
      question3Answer = "sponge"
      question4Answer = "towel"
      question5Answer = "barber"
      for x in line2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      # generate user question
      askQuestion = random.choice(question)

      # question 1
      if askQuestion == "What has to be broken before you can use it?":
        print("\n",askQuestion)
        choiceAnswer = input("Answer: ")
        choiceAnswer = choiceAnswer.lower()
        # if question is right
        if choiceAnswer == question1Answer:
          print("Wow you got it right, you get $50")
        # else question answer 
        else:
          print("Sorry.... Well I get my pay check today, the answer was",question1Answer,". I win all $",humanBet,"you put in to this game, hope to see you soon")
      # question 2
      elif askQuestion == "I’m tall when I’m young, and I’m short when I’m old. What am I?":
        print("\n",askQuestion)
        choiceAnswer = input("Answer: ")
        choiceAnswer = choiceAnswer.lower()
        # if question is right
        if choiceAnswer == question2Answer:
          print("Oh you got it right, you won $50")
        # else question answer
        else:
          print("Omg... Well I have money now the answer was",question2Answer,". I win all $",humanBet,"you put in to this game, can we play agian soon")
      # question 3
      elif askQuestion == "What is full of holes but still holds water?":
        print("\n",askQuestion)
        choiceAnswer = input("Answer: ")
        choiceAnswer = choiceAnswer.lower()
        # if question is right
        if choiceAnswer == question3Answer:
          print("Oh yay, you got it right, take your $50")
        # else question answer
        else:
          print("Sorry.... See you soon I win all $",humanBet,"you put in to this game, the answer was",question3Answer)
      # question 4
      elif question == "What gets wet while drying?":
        print("\n",askQuestion)
        choiceAnswer = input("Answer: ")
        choiceAnswer = choiceAnswer.lower()
        # if question is right
        if choiceAnswer == question4Answer:
          print("Yes, you got it right, take your $50")
        # else question answer
        else:
          print("Sorry.... See you soon I win all $",humanBet,"you put in to this game, the answer was",question4Answer)
      # question 5 
      else:
        question == "I shave every day, but my beard stays the same. What am I?"
        print("\n",askQuestion)
        choiceAnswer = input("Answer: ")
        choiceAnswer = choiceAnswer.lower()
        # if question is right
        if choiceAnswer == question5Answer:
          print("You will be seeing $50 in your future")
        # else question answer
        else:
          print("Yay, I get $",humanBet,"that you just gave me! The answer was",question5Answer)
  # else no choice was made 
  else: 
    print("No choice was made!!")

# choice 2 -- roulette
elif menuChoice == 2:
  print("\n",randomGreeting,name,", thank you for choosing roulette, I will be your host for today. Please pick a level below")
  time.sleep(1)
  for x in levels:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.1)
  levelChoice = int(input("\n1.Easy (2x bet)\n2.Medium (3x bet)\n3.Hard (10x bet) (#) : "))
  # level 1
  if levelChoice == 1:
    colorChoice = ["red", "black"]
    bet = float(input("Enter your bet $"))
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    color = input("\nEnter your choice\nRed or Black: ")
    color = color.lower()
    print("Ok you have $",bet,"on the line, and you picked",color)
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    # generate color wheel choice 
    colorChoice = random.choice(colorChoice)
    print("\nWheel:",colorChoice)
    # if right pick
    if colorChoice == color:
      prize = bet * 2
      print("You won, you get $",prize)
    # else pick
    else: 
      print("You lose, you get nothing")
  # level 2
  elif levelChoice == 2:
    oddOrEvanChoice = ["odd", "evan"]
    bet = float(input("Enter your bet $"))
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    choice = input("\nEnter your choice\nOdd or Evan: ")
    choice = choice.lower()
    print("Ok you have $",bet,"on the line, and you picked",choice)
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    # generate odd or evan wheel choice
    oddOrEvanChoice = random.choice(oddOrEvanChoice)
    print("\nWheel:",oddOrEvanChoice)
    # if right pick
    if oddOrEvanChoice == choice:
      prize = bet * 3
      print("You won, you get $",prize)
    # else pick
    else:
      print("Sorry, you lose")
  # level 3
  elif levelChoice == 3:
    bet = float(input("Enter your bet $"))
    for x in line2:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
    num = int(input("\nEnter your number between 1-36: "))
    # if number is between 1 and 36
    if num >= 1 and num <= 36:
      print("Ok you have $",bet,"on the line, and you picked number",num)
      for x in line2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
      # generate wheel number pick
      numGen = random.randint(1, 36)
      print("\nWheel:",numGen)
      # if right pick
      if num == numGen:
        prize = bet * 10
        print("You won, you get $",prize)
      # else pick
      else:
        print("You picked",num,"and the answer was",numGen,", you lose")
    # else 
    else:
      print("Please pick a number between 1-36")

# choice 3 -- fortune teller
elif menuChoice == 3:
  print("\n",randomGreeting,name,", thank you for coming to the fortune teller. Let me look into your future, but first pick your card below.")
  time.sleep(1)
  for x in line3:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.1)
  card = int(input("\n1. ~~Water~~\n2. ~~Fire~~\n3. ~~Earth~~\n4. ~~Air~~ (#): "))
  waterResponse = ["A dream you have will come true... Not now but soon.", "Fortune favours the brave.", "You cannot love life until you live the life you love.", "Wouldn't it be ironic... to die in the living room?"]
  fireResponce = ["The man or woman you desire feels the same about you.", "A stranger will soon enter your life with blessings to share.", "A very attractive person has a message for you.", "You will die alone and poorly dressed."]
  earthResponce = ["You are very talented in many ways.", "You must try or hate yourself for not trying.", "Your ability for accomplishment will follow with success.", "Pick another card, this one is out of order."]
  airResponce = ["Serious trouble will bypass you.", "Wealth awaits you very soon.", "You can make your own happiness.", "I see money in your future, it is not yours though!"]
  print("\nLet's see what the card has revealed...")
  for x in line3:
    print(x, end='')
    sys.stdout.flush()
    time.sleep(0.1)
  # fortune card 1
  if card == 1:
    # generate card 1 responce 
    print("\n",random.choice(waterResponse))
  # Fortune card 2
  elif card == 2:
    # generate card 2 responce 
    print("\n",random.choice(fireResponce))
  # Fortune card 3
  elif card == 3:
    # generate card 3 responce 
    print("\n",random.choice(earthResponce))
  # Fortune card 4
  elif card == 4:
    # generate card 4 responce 
    print("\n",random.choice(airResponce))
  # Fortune card else
  else:
    print("\nWe could not prosess your request")
# else
else:
  print("No choice was recognized, please try again and have a good day")