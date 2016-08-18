#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NISHANT
#
# Created:     02-04-2015
# Copyright:   (c) NISHANT 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint
import time
from s1 import RedisQueue
q = RedisQueue('test')
while True:
    input = str(randint(1,1000))
    print 'sent ' + input
    q.put(input)
    time.sleep(randint(1,10))