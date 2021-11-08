import os
import time
import random
from dotenv import load_dotenv

while True:
    Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right Answer not found.', 'Keep determined.')
    Randomrep_right = ('DETERMINATION', 'Good job', 'Was it worth it?', 'Mission complete\nRespect +', 'Bigbrain moment')

    load_dotenv()
    Question_1 = os.getenv('Question_1')
    Answer_1 = input('{0}: '.format(Question_1))

    RealAnswer_1 = os.getenv('RealAnswer_1')
    AlsoRealAnswer_1 = os.getenv('AlsoRealAnswer_1')

    if Answer_1.lower() == RealAnswer_1.lower() or Answer_1.lower() == AlsoRealAnswer_1.lower():
        print('{0}'.format(random.choice(Randomrep_right)))
    else: print('{0} The Answer was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_1, AlsoRealAnswer_1))
    time.sleep(2)

    Question_2 = os.getenv('Question_2')
    Answer_2 = input('{0}: '.format(Question_2))

    RealAnswer_2 = os.getenv('RealAnswer_2')
    AlsoRealAnswer_2 = os.getenv('AlsoRealAnswer_2')

    if Answer_2.lower() == RealAnswer_2.lower() or Answer_2.lower() == AlsoRealAnswer_2.lower():
        print('{0}'.format(random.choice(Randomrep_right)))
    else: print('{0} The Answer was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAnswer_2, AlsoRealAnswer_2))
    time.sleep(2)
    if Answer_1 == RealAnswer_1 or Answer_1 == AlsoRealAnswer_1 and Answer_2 == RealAnswer_2 or Answer_2 == AlsoRealAnswer_2:
        break

