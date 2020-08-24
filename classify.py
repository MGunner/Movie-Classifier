import os
import shutil
import re

with os.scandir() as entries:
    for entry in entries:
      n1=os.path.splitext(entry.name)[0].replace("."," ")
      n2 = os.path.splitext(entry.name)[0]
      n3=str(n1 + os.path.splitext(entry.name)[1])
      final=(n2,n3)
      os.rename(entry.name,n3)
      os.mkdir(n1)
      shutil.move(n3, n1 + "/" + n3)
	  