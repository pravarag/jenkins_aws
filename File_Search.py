import os
import glob
import fnmatch

Dir_root=os.chdir('/')
Current_Dir=str(os.getcwd())
print Current_Dir

list_dir=os.listdir(Current_Dir)

list_dir.sort()

#print list_dir

next_val=prev_val=None

Files=[]
Dirs=[]

for i, j in enumerate(list_dir):
	if os.path.isfile(j):
		Files.append(j)
	else:
		Dirs.append(j)

#print Files
#print Dirs

Dirs.sort()
print Dirs

file_name=raw_input('Enter the name of the file: ')
file_ext=[x for x in file_name.split('.')]
file_ext='.'+file_ext[1]

#print file_ext

flag=0

print file_name

for i in Files:
	if i==file_name:
		print "file found"
		print os.getcwd()
	else:
		print "file not found, directing towards directory search"
		flag=1

#Directory search

if flag==1:
	for i in Dirs:
		new_path=os.getcwd()+i
		os.chdir(new_path)
		print glob.glob(file_name)



# for root,dir,files in os.walk(Current_Dir):
# 	for file_name in files:
# 		if file_name.endswith(file_ext):
# 			print file_name
# 			print os.getcwd()
# 		else: pass 


#result=(file_name for file_name in files for root, dir, files in os.walk(Current_Dir))
