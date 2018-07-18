## to get latest Opera version by directory name

general_opera_dir = '/win7share1/test123/Opera'

from os import listdir
out1 = listdir(general_opera_dir)
out2 = [x for x in out1 if x[0].isdigit() and x[-1].isdigit()]
out2.sort()
print('LATEST = ' + str(out2[-1]))
