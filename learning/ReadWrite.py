#   ReadWrite.py    -   Reading and Writing to files (Uncompressed)
#   READ WRITE Process - Open File (File Object) / Read or Write / Close

import os, shelve

#   1-  OPEN / CREATE a file for reading text from

currdir = os.getcwd()

if not os.path.exists('data'):
    print ('No data folder: Creating folder')
    os.makedirs('data')

filename = 'rwdata.txt'
filepath = os.path.join(currdir, 'data', filename)

#   OVERWRITE file if exists

fc = ['Hello Read/Write', 'This file was created by code and is maintained by code','Please do not edit outside of the code']
out = '\n'.join(fc)

newfile = open(filepath, 'w')
newfile.write(out)
newfile.close()

#   2-  READ content from the file

file = open(filepath)   #   OPENED in read mode
raw = file.read()
content = raw.split('\n')
for line in content:
    print (line)

file.close()    #   Finished with file

#   NOW Create a shelf file and store some data

sname = 'rwshelve'
spath = os.path.join(currdir, 'data', sname)

quickvar = ['simple', 'data', 'file'];

shelf = shelve.open(spath)
shelf['saved'] = quickvar;
shelf.close()
