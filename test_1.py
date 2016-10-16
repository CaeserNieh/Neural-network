import numpy as np
'''
dataset = np.array([
([-1,0,0],1),
([-1,0,1],1),
([-1,1,0],-1),
([-1,1,1],1) ])
'''
file = open("/home/caeser/dataset/2class.txt",'r')

row2 = []
expect = []
data = []
for line in file:
	row = []
	e = [-1.0]
	input_data = line.split("\t")
	for x in range(len(input_data) - 1):
		row.append(float(input_data[x]))

	e.extend(row)
	row2.append(e)
	expect.append(float(input_data[-1]))

for i in range(len(row2)):
	arr = []
	arr.append(row2[i])
	arr.append(expect[i])
	data.append(arr)

dataset = np.array(data)
print(dataset)




def mul(li,n):
	ans = []
	for x in range(len(li)):
		temp = li[x]*n
		ans.append(temp)
	return ans
def minus(li1,li2):
	ans = []
	#print(li1)
	#print(li2)
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

def PLA(dataset):
	a = [-1,0,1]
	para = 1
	weight = np.array(a)
	found = False
	for i in range(10):
		found = False
		for x,s in dataset:
			print("Node :")
			print(x)
			if int(weight.T.dot(x)) == 0:
				continue
			elif int(np.sign(weight.T.dot(x))) != s:
				found = True
				print("Weight first : ")
				print(weight)
				if s == -1:
					a = np.ndarray.tolist(weight)
					#a = a - mul(a,para)
					a =  minus(a,mul(x,para))
					weight = np.array(a)
				else :
					a = np.ndarray.tolist(weight)
					# = a + mul(a,para)
					a = add(a,mul(x,para))
					weight = np.array(a)
				print("Weight later: ")
				print(weight)
		if found == False:
			break
	print("ANSWER :")
	print(weight)

PLA(dataset)