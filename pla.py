import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Tkinter import Tk

from tkFileDialog import askopenfilename
from tkFileDialog import askopenfile

'''
dataset = np.array([
([-1,0,0],1),
([-1,0,1],1),
([-1,1,0],-1),
([-1,1,1],1) ])
'''
#file = open("/home/caeser/dataset_new/perceptron3.txt",'r')




Tk().withdraw()
file = askopenfile(mode='r')



row2 = []
expect = []
data = []

answer = []

for line in file:
	row = []
	e = [-1.0]
	print(line)
	if line == "\n" :
		continue
	input_data = line.split(" ")

	print(input_data)

	for x in range(len(input_data) - 1):   #len(input_data)-1
		row.append(float(input_data[x]))  #input_data[x]

	e.extend(row)
	row2.append(e)
	expect.append(float(input_data[-1]))

print(expect)	

for i in range(len(row2)):
	arr = []
	arr.append(row2[i])
	arr.append(expect[i])
	data.append(arr)

dataset = np.array(data)
print(dataset)
#print(expect)
group_set = []
for i in range(len(expect)):
	if expect[i] not in group_set :
		#print(expect[i])
		group_set.append(expect[i])		
print(group_set)



def mul(li,n):
	ans = []
	for x in range(len(li)):
		temp = li[x]*n
		ans.append(temp)
	return ans
def minus(li1,li2):
	ans = []
	for x in range(len(li1)):
		temp = li1[x] - li2[x]
		ans.append(temp)
	return ans

def add(li1,li2):
	ans = []
	for x in range(len(li1)):
		temp = li1[x] +li2[x]
		ans.append(temp)
	return ans


def PLA(dataset,group_set):
	for i in range(len(group_set)):
		group = group_set[i]

		temp_x,temp_y = dataset[0]
		#print(len(temp_x))
		initial_size = len(temp_x)
		initial_arr_head = [-1.0]
		initial_arr_end = [1.0]

		for z in range(initial_size-2):
			initial_arr_head.extend([0.0])

		initial_arr_head.extend(initial_arr_end)
		print(initial_arr_head)

		a = initial_arr_head
		#a = [-1.0,0,0,1]
		para = 0.8

		weight = np.array(a)
		found = False

		while True:
			found = False
			for x,s in dataset:
				#group = 
				print("Node :")
				print(x)

				if  group != s :
					print("Right Now Group  : ")
					print(group)

					print("Node Group  : ")
					print(s)
					
					
					if int(np.sign(weight.T.dot(x))) >=0:
						print("Weight first : ")
						print(weight)

						found = True
						a = np.ndarray.tolist(weight)
						a =  minus(a,mul(x,para))
						weight = np.array(a)
						
						print("Weight later: ")
						print(weight)
					
					else  :
						continue
					
				else :
					if int(np.sign(weight.T.dot(x))) >=0:
						continue
					
					else  :
						print("Weight first : ")
						print(weight)

						found = True
						a = np.ndarray.tolist(weight)
						a =  add(a,mul(x,para))
						weight = np.array(a)
						
						print("Weight later: ")
						print(weight)	

			if found == False:
				break
		print("ANSWER :")
		print(weight)
		answer.append(weight)

PLA(dataset,group_set)
print(answer)




# ---------------------------------

fig = plt.figure()
#ax1 = fig.add_subplot(111) #subplot(111)
ax1 = fig.add_subplot(111, projection='3d')

sym = ['o',"x","*","+","1"]
color = ["orange","purple","gold","gray","red","green","yellow","white","blue","black",""]


temp_x,temp_s = dataset[0]
if len(temp_x) == 3:
	#fig = plt.figure()
	#ax1 = fig.add_subplot(111) #subplot(111)
	#ax1 = fig.add_subplot(111, projection='3d')

	print("len 3")
	for i in range(len(group_set)): #len(group_set)
		temp_set = []
		for x,s in dataset:
			if s == group_set[i]:
				temp_set.append(x)
		#print(temp_set)
		x = [v[1] for v in temp_set]
		y = [v[2] for v in temp_set]
		#z = [v[3] for v in temp_set]
		print(x)
		print(y)
		#print(z)
		ax1.scatter( x, y,s = 100,c=color[i%10], marker= sym[i%5], label='O')
		
	for i in range(len(answer)):
		temp = np.ndarray.tolist(answer[i])
		l = np.linspace(-1,1)
		a,b = -temp[1]/temp[2], temp[0]/temp[2]
		ax1.plot(l, a*l + b, 'b-')

	plt.show()

elif len(temp_x) == 4 :
	print("len 4")
	plt3d = plt.figure().gca(projection='3d')
	for i in range(len(group_set)): #len(group_set)
		temp_set = []
		for x,s in dataset:
			if s == group_set[i]:
				temp_set.append(x)
		#print(temp_set)
		x = [v[1] for v in temp_set]
		y = [v[2] for v in temp_set]
		z = [v[3] for v in temp_set]
		print(x)
		print(y)
		print(z)
		plt3d.scatter( x, y,z,s = 100,c=color[i%10], marker= sym[i%5], label='O')
		
	
	for i in range(len(answer)):
		temp = np.ndarray.tolist(answer[i])
		xx,yy = np.meshgrid(range(5),range(5))
		a,b,c = -(temp[1]*xx)/temp[3] ,- (temp[2]*yy)/temp[3] , (temp[0])/temp[3]
		z =  a+b+c
		plt3d.plot_surface(xx,yy,z)
	
	
	plt.show()
else :
	print ("Can't draw !!")

#plt.show()
