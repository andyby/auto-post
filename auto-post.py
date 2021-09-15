#python -V
#Python 2.7.12

import os
import time

# get the forturn command output
adage = os.popen('/usr/games/fortune').read()

# create content path and name base on timestamp
content_path = 'adage/' + str(time.time()) + '.md'

# didn't find a better way to pass forturn output while use hugo new
cmd = './hugo new ' + content_path

os.system(cmd)

# use file writer instead
with open('./content/' + content_path, 'a') as f:
    f.write(adage)

os.system('git add .')
os.system("git commit -m " + str(time.time()) + '.md')
os.system('git push origin master')

