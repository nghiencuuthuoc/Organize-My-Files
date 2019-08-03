# 
import glob
import shutil

vendors = ("*April*.*", "*August*.*", "*December*.*", "*February*.*")
paths = (".\\April\\", ".\\August\\",".\\December\\", ".\\February\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# 
import glob
import shutil

vendors = ("*January*.*", "*July*.*", "*June*.*", "*March*.*")
paths = (".\\January\\", ".\\July\\",".\\June\\", ".\\March\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])

# 
import glob
import shutil

vendors = ("*May*.*", "*November*.*", "*October*.*", "*September*.*")
paths = (".\\May\\", ".\\November\\",".\\October\\", ".\\September\\")
for idx in range(len(vendors)):
    for matches in glob.glob(vendors[idx]):
        shutil.move(matches, paths[idx])
