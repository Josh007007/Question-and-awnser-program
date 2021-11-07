import os
import time
import random
from dotenv import load_dotenv

while True:
    Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right awnser not found.', 'Keep determined.')
    Randomrep_right = ('DETERMINATION', 'Good job', 'Was it worth it?', 'Mission complete\nRespect +', 'Bigbrain moment')

    load_dotenv()
    Question_1 = os.getenv('Question_1')
    Awnser_1 = input('{0}: '.format(Question_1))

    RealAwnser_1 = os.getenv('RealAwnser_1')
    AlsoRealAwnser_1 = os.getenv('AlsoRealAwnser_1')

    if Awnser_1.lower() == RealAwnser_1.lower() or Awnser_1.lower() == AlsoRealAwnser_1.lower():
        print('{0}'.format(random.choice(Randomrep_right)))
    else: print('{0} The awnser was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAwnser_1, AlsoRealAwnser_1))
    time.sleep(2)

    Question_2 = os.getenv('Question_2')
    Awnser_2 = input('{0}: '.format(Question_2))

    RealAwnser_2 = os.getenv('RealAwnser_2')
    AlsoRealAwnser_2 = os.getenv('AlsoRealAwnser_2')

    if Awnser_2.lower() == RealAwnser_2.lower() or Awnser_2.lower() == AlsoRealAwnser_2.lower():
        print('{0}'.format(random.choice(Randomrep_right)))
    else: print('{0} The awnser was: {1} or {2}'.format(random.choice(Randomrep_wrong), RealAwnser_2, AlsoRealAwnser_2))
    time.sleep(2)
    if Awnser_1 == RealAwnser_1 or Awnser_1 == AlsoRealAwnser_1 and Awnser_2 == RealAwnser_2 or Awnser_2 == AlsoRealAwnser_2:
        break

