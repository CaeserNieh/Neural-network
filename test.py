import numpy as np

file = open("/home/caeser/dataset/2class.txt",'r')


data_set = []
expect_set = []

##  exp = weight  

def PLA(data_set,expect_set):
	length = len(data_set[0])
	exp = [-1.0]
	train = [-1.0]
	weight = np.ndarray.tolist(np.zeros(length))
	exp.extend(weight)
	print("weight : ")
	print(exp)
	#print(data_set[1][1])

	train.extend(data_set[0])
	print("train_data")
	for x in range(100) : 
		for y in range(length  ):
			train[y+1] = data_set[x%len(data_set)][y]
		print(train)
		


	








# read data  and process

for line in file : 
	row_set = []

	input_data = line.split("\t")
	temp = len(input_data)
	for x in range(temp - 1 ):
		row_set.append(float(input_data[x]))
	e = [-1.0]
	e.extend(row_set)
	print(e)

	#data_set.append(row_set)
	data_set.append(e)
	expect_set.append(float(input_data[-1]))

#  finish reading and already process data



print(data_set)
print("expect_set")
print(expect_set)
#print(data_set[1].append([-1.0]))
#print(data_set[1])

lar_ar = []
#mid_ar = []
for i in range(len(data_set)):
	mid_ar = []
	mid_ar.append(data_set[i])
	mid_ar.append(expect_set[i])
	lar_ar.append(mid_ar)



final_dataset = np.array(lar_ar)

print(final_dataset)


#PLA(data_set,expect_set)




