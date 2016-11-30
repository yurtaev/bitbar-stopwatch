#!/usr/bin/env python
# coding: utf-8

# <bitbar.title>Stopwatch</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Egor Yurtaev</bitbar.author>
# <bitbar.author.github>yurtaev</bitbar.author.github>
# <bitbar.desc>Stopwatch</bitbar.desc>
# <bitbar.image>https://cloud.githubusercontent.com/assets/7404532/12356787/ae62636c-bba4-11e5-8ff8-6a1eaffcbfc2.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

from datetime import datetime
import time
import sys
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, '.stopwatch')

if 'reset' in sys.argv:
	os.remove(FILE_PATH)

begin = None

if not os.path.exists(FILE_PATH):
	with open(FILE_PATH, 'w') as f:
		begin = datetime.now()
		f.write("%s" % time.mktime(begin.timetuple()))
else:
	with open(FILE_PATH, 'r+') as f:
		data = f.read()
		begin = datetime.fromtimestamp(float(data))

now = datetime.now()
diff = now - begin

out = str(diff).split('.')[0]

print '%s|dropdown=false' % out
print '---'
print "Reset | bash='%s' param1=reset terminal=false" % __file__

