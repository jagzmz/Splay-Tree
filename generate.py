from pathlib import Path,PurePath
import json,time,os
flist=[]
import random

start=time.time()


randList=[random.randrange(1,9000) for _ in range (9000)]
print(randList)

end=time.time()
print("Time taken is ",end-start)

os.system("javac splay.java")

os.system('java splay {}'.format(' '.join(str(w) for w in randList)))
