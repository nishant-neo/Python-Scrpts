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
from s1 import RedisQueue
q = RedisQueue('test')
while True:
    print 'recieved ' + str(q.get())
