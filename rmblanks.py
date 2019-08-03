#-------------------------------------------------------------
#    rmblanks.py
#      Deletes all empty folders under a given path.
#    http://metinsaylan.com
#-------------------------------------------------------------

#    Usage: rmblanks.py "E:/Test"

import sys, os

if len(sys.argv) == 1:
    # Print usage
    print("Usage: rmblanks.py \"E:/TestFolder\"")
else:
    for root, dirs, files in os.walk(sys.argv[1], topdown=False):
        for name in dirs:
            try:
                if len(os.listdir( os.path.join(root, name) )) == 0: #check whether the directory is empty
                    print( "Deleting", os.path.join(root, name) )
                    try:
                        os.rmdir( os.path.join(root, name) )
                    except:
                        print( "FAILED :", os.path.join(root, name) )
                        pass
            except:
                pass
