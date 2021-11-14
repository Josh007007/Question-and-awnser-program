import os
import time
import random
from dotenv import load_dotenv
Score_Total = 0
Score_Max_Total = 0

while True:
    Score = 0
    Score_Max = 0
    Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right Answer not found.', 'Keep determined.')
    Randomrep_right = ('DETERMINATION', 'Good job', 'You won...\nBut at what cost?', 'Mission complete\nRespect +', 'Bigbrain moment')

Tip = input('Do you want tips if you got an answer wrong? (Y or N)')

    load_dotenv()
    Question_1 = os.getenv('Question_1')
    Answer_1 = input('\033[1;33;40m{0}: '.format(Question_1))
    Score_Max += 1

    RealAnswer_1 = os.getenv('RealAnswer_1')
    AlsoRealAnswer_1 = os.getenv('AlsoRealAnswer_1')
    Tip_1 = os.getenv('Tip_1')

    if Answer_1.lower() == RealAnswer_1.lower() or Answer_1.lower() == AlsoRealAnswer_1.lower():
        print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
        Score += 1
        time.sleep(1)
    elif RealAnswer_1 == AlsoRealAnswer_1: 
        print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer_1))
        if Tip.lower() == Y
        	print(Tip_1)
        time.sleep(1.5)
    else: 
        print('\033[1;31;40m{0} The answers were: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_1, AlsoRealAnswer_1))
        time.sleep(1.5)

    Question_2 = os.getenv('Question_2')
    Answer_2 = input('\033[1;33;40m{0}: '.format(Question_2))
    Score_Max += 1

    RealAnswer_2 = os.getenv('RealAnswer_2')
    AlsoRealAnswer_2 = os.getenv('AlsoRealAnswer_2')

    if Answer_2.lower() == RealAnswer_2.lower() or Answer_2.lower() == AlsoRealAnswer_2.lower():
        print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
        Score += 1
        time.sleep(1)
    elif RealAnswer_2 == AlsoRealAnswer_2: 
        print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer_2))
        time.sleep(1.5)
    else:
        print('\033[1;31;40m{0} The answers were: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_2, AlsoRealAnswer_2))
        time.sleep(1.5)

    Question_3 = os.getenv('Question_3')
    RealAnswer_3 = os.getenv('RealAnswer_3')

    AlsoRealAnswer_3 = os.getenv('AlsoRealAnswer_3')
    Answer_3 = input('\033[1;33;40m{0}: '.format(Question_3))
    Score_Max += 1

    if Answer_3.lower() == RealAnswer_3.lower() or Answer_3.lower() == AlsoRealAnswer_3.lower():
        print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
        Score += 1
        time.sleep(1)
    elif RealAnswer_3 == AlsoRealAnswer_3: 
        print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer_3))
        time.sleep(1.5)
    else:
        print('\033[1;31;40m{0} The answers were: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_3, AlsoRealAnswer_3))
        time.sleep(1.5)

    Score_Total += Score
    Score_Max_Total += Score_Max
    Score_Prec = Score_Total / Score_Max_Total * 100

    if Score == Score_Max:
        print("\033[1;32;40mYou got all of the answers right!\n{0}% (In total)".format(Score_Prec))
        time.sleep(0.5)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N): ")
        if Replay.upper() == "N":
            break
    elif Score == 0:
        print("\033[1;31;40mYou got all of the questions wrong, so you're going to get the questions again.\n{0}% (In total)".format(Score_Prec))
        time.sleep(2)
    else:
        print("\033[1;32;40mYou got {0} answer(s) right out of {1} questions.\n{2}% (In total)".format(Score, Score_Max, Score_Prec))
        time.sleep(0.8)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N): ")
        if Replay.upper() == "N":
            break
time.sleep(0.6)
print("\033[3;30;47mSee you next time", "\033[1;37;40m")
time.sleep(1)
