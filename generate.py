from pathlib import Path,PurePath
import json,time,os
flist=[]
import random

start=time.time()


randList=[random.randrange(1,9000) for _ in range (9000)]
print(randList)

end=time.time()
print("Time taken is ",end-start)

# print([x for x in flist[1:9000]])

os.system("javac splay.java")
# os.system("java test {}".format([x for x in flist[1:2]]))
# print(''.join(str(w) for w in flist))
os.system('java splay {}'.format(' '.join(str(w) for w in randList)))













# if Path("data.json").exists() is False:
# 	result = list(Path(".").rglob("*.*"))

# 	for name in result:
# 		flist.append(PurePath(name).name)
# 		#print(PurePath(name).name)

# 	with open('data.json', 'w') as outfile:
# 		json.dump(' '.join(str(w) for w in flist[1:9000]),outfile)
# else:
# 	with open('data.json') as outfile:
# 		flist=json.load(outfile)
# 		# print(flist)