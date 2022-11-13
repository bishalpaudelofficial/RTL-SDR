import shutil
import datetime
from time import gmtime, strftime

newname = strftime("%d %b %Y", gmtime())
dst = '/home/pi/data/%s.csv' % newname
shutil.move('/home/pi/signal.csv', dst)