import os
import time
import random
from dotenv import load_dotenv

while True:
    Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right Answer not found.', 'Keep determined.')
    Randomrep_right = ('DETERMINATION', 'Good job', 'You won...\nBut at what cost?', 'Mission complete\nRespect +', 'Bigbrain moment')

    load_dotenv()
    Question_1 = os.getenv('Question_1')
    Answer_1 = input('\033[1;33;40m{0}: '.format(Question_1))

    RealAnswer_1 = os.getenv('RealAnswer_1')
    AlsoRealAnswer_1 = os.getenv('AlsoRealAnswer_1')

    if Answer_1.lower() == RealAnswer_1.lower() or Answer_1.lower() == AlsoRealAnswer_1.lower():
        print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
    elif RealAnswer_1 == AlsoRealAnswer_1: 
        print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer_1))
    else: print('\033[1;31;40m{0} The answer was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_1, AlsoRealAnswer_1))
    time.sleep(1.5)

    Question_2 = os.getenv('Question_2')
    Answer_2 = input('\033[1;33;40m{0}: '.format(Question_2))

    RealAnswer_2 = os.getenv('RealAnswer_2')
    AlsoRealAnswer_2 = os.getenv('AlsoRealAnswer_2')

    if Answer_2.lower() == RealAnswer_2.lower() or Answer_2.lower() == AlsoRealAnswer_2.lower():
        print('\033[1;32;40m{0}'.format(random.choice(Randomrep_right)))
    elif RealAnswer_2 == AlsoRealAnswer_2: 
        print('\033[1;31;40m{0} The only answer was: {1}'.format(random.choice(Randomrep_wrong), RealAnswer_2))
    else:
        print('\033[1;31;40m{0} The answer was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_2, AlsoRealAnswer_2))
        time.sleep(1.5)

    Ans_1RealAns_1 = 'Answer_1.lower() == RealAnswer_1.lower()'
    Ans_1AlsoRealAns_1 = 'Answer_1.lower() == AlsoRealAnswer_1.lower()'
    Ans_2RealAns_2 = 'Answer_2.lower() == RealAnswer_2.lower()'
    Ans_2AlsoRealAns_2 = 'Answer_2.lower() == AlsoRealAnswer_2.lower()'

    Ans_all = 'eval(Ans_1RealAns_1) or eval(Ans_1AlsoRealAns_1) or eval(Ans_2RealAns_2) or eval(Ans_2AlsoRealAns_2)'

    Ans_1RealAns_1Ans_2RealAns_2 = 'Answer_1.lower() == RealAnswer_1.lower() and Answer_2.lower() == RealAnswer_2.lower()'
    Ans_1AlsoRealAns_1Ans_2RealAns_2 = 'Answer_1.lower() == AlsoRealAnswer_1.lower() and Answer_2.lower() == RealAnswer_2.lower()'
    Ans_1RealAns_1Ans_2AlsoRealAns_2 = 'Answer_1.lower() == RealAnswer_1.lower() and Answer_2.lower() == AlsoRealAnswer_2.lower()'
    Ans_1AlsoRealAns_1Ans_2AlsoRealAns_2 = 'Answer_1.lower() == AlsoRealAnswer_1.lower() and Answer_2.lower() == AlsoRealAnswer_2.lower()'

    if eval(Ans_1RealAns_1Ans_2RealAns_2) or eval(Ans_1AlsoRealAns_1Ans_2RealAns_2) or eval(Ans_1RealAns_1Ans_2AlsoRealAns_2) or eval(Ans_1AlsoRealAns_1Ans_2AlsoRealAns_2):
        print("\033[1;32;40mYou got all of the answers right!")
        time.sleep(0.5)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N): ")
        if Replay.upper() == "N":
            break
    elif eval(Ans_all):
        print("\033[1;32;40mYou got 1 answer right.")
        time.sleep(0.5)
        Replay = input("\033[1;33;40mDo you want to continue? (Y or N): ")
        if Replay.upper() == "N":
            break
    else:
        print("\033[1;31;40mYou got all of the questions wrong, so you're going to get the questions again.")
        time.sleep(2)
time.sleep(0.6)
print("\033[3;30;47mSee you next time", "\033[1;37;40m")
time.sleep(1)
