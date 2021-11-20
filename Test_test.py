import os
import time
import random
from dotenv import load_dotenv
Score_Total = 0
Score_Max_Total = 0
Num = int(0)
while True:
    Num = int(input("How many questions are there in the .env file? (Default is 3): "))
    if Num <= 0:
        print("Error 404 Questions not found.\nPlease import a number higher than 0.")
        time.sleep(1)
    else: 
        break

Num_list = []
Num_Counting = 0
Num_list_Counting = 1

while True:
    Num_list.append(Num_Counting)
    if Num_Counting == Num:
        break
    Num_Counting += 1


while True:
    Score = 0
    Score_Max = 0
    Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right Answer not found.', 'Keep determined.')
    Randomrep_right = ('DETERMINATION', 'Good job', 'You won...\nBut at what cost?', 'Mission complete\nRespect +', 'Bigbrain moment')
    Num_list_Counting = 1
    while True:
        Question = 'Question_{0}'.format(Num_list[Num_list_Counting])
        RealAnswer = 'RealAnswer_{0}'.format(Num_list[Num_list_Counting])
        AlsoRealAnswer = 'AlsoRealAnswer_{0}'.format(Num_list[Num_list_Counting])
        #Tip = 0!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        load_dotenv()
        Question = os.getenv(Question)
        Answer = input('\033[1;33;40m{0}:\033[1;37;40m '.format(Question))
        Score_Max += 1

        RealAnswer = os.getenv(RealAnswer)
        AlsoRealAnswer = os.getenv(AlsoRealAnswer)

        if Answer.lower() == RealAnswer.lower() or Answer.lower() == AlsoRealAnswer.lower():
            print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
            Score += 1
            time.sleep(1)
        elif RealAnswer == AlsoRealAnswer: 
            print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer))
            time.sleep(1.5)
        else: 
            print('\033[1;31;40m{0} The answers were: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer, AlsoRealAnswer))
            time.sleep(1.5)
        if Num == Num_list[Num_list_Counting]:
            break
        Num_list_Counting += 1

    Score_Total += Score
    Score_Max_Total += Score_Max
    Score_Prec = Score_Total / Score_Max_Total * 100

    if Score == Score_Max:
        print("\033[1;32;40mYou got all of the answers right!\n{0}% (In total)".format(Score_Prec))
        time.sleep(0.5)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N):\033[1;37;40m ")
        if Replay.upper() == "N":
            break
    elif Score == 0:
        print("\033[1;31;40mYou got all of the questions wrong, so you're going to get the questions again.\n{0}% (In total)".format(Score_Prec))
        time.sleep(2)
    else:
        print("\033[1;32;40mYou got {0} answer(s) right out of {1} questions.\n{2}% (In total)".format(Score, Score_Max, Score_Prec))
        time.sleep(0.8)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N):\033[1;37;40m ")
        if Replay.upper() == "N":
            break
time.sleep(0.6)
print("\033[3;30;47mSee you next time\033[1;37;40m")
time.sleep(1)
