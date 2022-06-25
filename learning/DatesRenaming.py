#   DatesRenaming.py
#   Looks through files and changes dates from American (MM-DD-YYYY) to Euro (DD-MM-YYYY)

import shutil, os, re

#   CREATE a regex that matches files with American date style
#   All text / 1 or 2 digits month / 1 or 2 digits day / four digits year / all text

pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

#   LOOP over the files in the working directory

for amerFile in os.listdir("datefiles"):

    mat = pattern.search(amerFile)
    if mat == None:
        continue

    #   MATCH: seperate the name parts

    before = mat.group(1)
    month = mat.group(2)
    day = mat.group(4)
    year = mat.group(6)
    after = mat.group(8)

    #   CREATE new file name for Euro style

    euroName = before + day + '-' + month + '-' + year + after

    #   WORKING directory and paths

    dir = os.path.abspath('datefiles')
    aName = os.path.join(dir, amerFile)
    eName = os.path.join(dir, euroName)

    #   RENAME the file

    print ('Renaming %s to %s ...' %(aName, eName))
    #shutil.move(aName, eName)

inn = input()
