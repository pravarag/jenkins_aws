
row_num=input("Enter the coordinate a: ")
col_num=input("Enter the coordinate b: ")



def calc_value(a, b):
	file_1=open('hello.txt','r')
	read_lines=file_1.readlines()
	file_1.close()
	for i, j in enumerate(read_lines):
		if i==a:
			print j[b]
		else: pass
	

calc_value(row_num, col_num)