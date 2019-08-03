# from 2016 - 2019
import glob
import shutil

vendors = ("*2016*.*", "*2017*.*", "*2018*.*", "*2019*.*")
paths = (".\\2016\\", ".\\2017\\",".\\2018\\", ".\\2019\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# from 2000 - 2003
import glob
import shutil

vendors = ("*2000*.*", "*2001*.*", "*2002*.*", "*2003*.*")
paths = (".\\2000\\", ".\\2001\\",".\\2002\\", ".\\2003\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# from 2004 - 2007
import glob
import shutil

vendors = ("*2004*.*", "*2005*.*", "*2006*.*", "*2007*.*")
paths = (".\\2004\\", ".\\2005\\",".\\2006\\", ".\\2007\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# from 2008 - 2011
import glob
import shutil

vendors = ("*2008*.*", "*2009*.*", "*2010*.*", "*2011*.*")
paths = (".\\2008\\", ".\\2009\\",".\\2010\\", ".\\2011\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])


# from 2012 - 2015
import glob
import shutil

vendors = ("*2012*.*", "*2013*.*", "*2014*.*", "*2015*.*")
paths = (".\\2012\\", ".\\2013\\",".\\2014\\", ".\\2015\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])


# from 1997 - 1999, 2016

import glob
import shutil

vendors = ("*1999*.*", "*1998*.*", "*1997*.*", "*2016*.*")
paths = (".\\1999\\", ".\\1998\\",".\\1997\\", ".\\2016\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# from 1993 - 1996
import glob
import shutil

vendors = ("*1993*.*", "*1994*.*", "*1995*.*", "*1996*.*")
paths = (".\\1993\\", ".\\1994\\",".\\1995\\", ".\\1996\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])