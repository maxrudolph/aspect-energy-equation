#!/bin/python3
import os
import subprocess

basefile = 'velo_ZZ+S200_'
for i in range(458,0,-1):
  filename = basefile + '{:03d}'.format(i) + '.gpml'
  exists = os.path.isfile(filename)
  if exists:
    last_file = filename
  else:
    subprocess.run(["ln","-s",last_file,filename])
