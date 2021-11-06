import os
import time
import random
from dotenv import load_dotenv

Randomrep_wrong = ('I\'m sorry to inform you that you\'re wrong.', 'You almost had it!', 'Try better next time.', 'Error 404: right awnser not found.', 'Keep determined.')
Randomrep_right = ('DETERMINATION', 'Good job', 'Was it worth it?', 'Mission complete\nRespect +', 'Bigbrain moment')

load_dotenv()
Question_1 = os.getenv('Question_1')
Awnser_1 = input('{0}: '.format(Question_1))

RealAwnser_1 = os.getenv('RealAwnser_1')
AlsoRealAwnser_1 = os.getenv('AlsoRealAwnser_1')

if Awnser_1.lower() == RealAwnser_1 or AlsoRealAwnser_1:
    print('{0}'.format(random.choice(Randomrep_right)))
else: print('{0} The awnser was: {1}'.format(random.choice(Randomrep_wrong), RealAwnser_1))
time.sleep(2)

