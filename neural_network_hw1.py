import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Tkinter import Tk

from tkFileDialog import askopenfilename
from tkFileDialog import askopenfile



def python_get_input():
	learning = input("Please input your learning Rate 0 ~ 1 : ")
	loop_times = input("Please input your loop times 1 ~ 100000000: ")
	
	return learning,loop_times

def reading_file():
	#Tk().withdraw()
	#file = askopenfile(mode='r')
	file = open("/home/caeser/dataset_new/perceptron4.txt")

	return file

def test_reading_file(file_name):
	file = open("/home/caeser/dataset_new/%s" %file_name)

	return file

def process_data(file_reading):
	expect = []
	row2 = []

	for line in file_reading:
		row = []
		e = [-1.0]
		#print("read_line")
		print(line)
		#print("after")
		if line == "\r\n"  or line == "\n":
			#print("test")
			continue
		input_data = line.split(" ")

		#print("data")
		print(input_data)

		for x in range(len(input_data) - 1):   #len(input_data)-1
			row.append(float(input_data[x]))  #input_data[x]

		e.extend(row)
		row2.append(e)
		expect.append(float(input_data[-1]))

	print("Ans expect")
	print(expect)
	print("Ans row data")
	print(row2)

	return row2,expect

def divide_data(row2,expect):
	data = []
	group_set = []

	num = ((len(row2)*2)/ 3)+1
	#num = len(row2)
	training_data = []
	test_data = []
	
	for i in range(num):
		arr = []
		arr.append(row2[i])
		arr.append(expect[i])
		training_data.append(arr)

	training_dataset = np.array(training_data)

	for i in range(len(row2) - num):
		arr = []
		arr.append(row2[i+num])
		arr.append(expect[i+num])
		test_data .append(arr)

	test_dataset = np.array(test_data)

	for i in range(num):
		if expect[i] not in group_set :
			group_set.append(expect[i])

	# total group set
	total_group_set = []
	for i in range(len(expect)):
		if expect[i] not in total_group_set :
			total_group_set.append(expect[i])

	return  training_dataset,test_dataset,group_set,total_group_set

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

def PLA(dataset,group_set,para,loop):
	answer = []

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
		#initial_arr_head = [-1.0,0,0,1]

		weight = np.array(initial_arr_head)
		found = False

		times = 0

		while True:
			found = False
			for x,s in dataset:

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

			times = times+1

		print("ANSWER :")
		print(weight)
		answer.append(weight)

	return answer


def judge(training_dataset,test_dataset,weight,total):
	dataset = [training_dataset,test_dataset]
	ans = []
	wrong_train = []
	wrong_test = []
	for i in range(len(total)):
		yes = 0
		group = total[i]
		for i in range(len(dataset)):
			yes = 0	
			for x,s in dataset[i]:
				if  group != s :	
					if int(np.sign(weight[0].T.dot(x))) >=0:
						continue					
					else  :
						yes = yes+1
				else :
					if int(np.sign(weight[0].T.dot(x))) >=0:						
						yes = yes+1
					else  :
						continue
			yes = yes * 1.0
			print(yes)
			print(dataset[i])
			temp = yes / len(dataset[i])
			ans.append(temp)
	return ans
'''
	print("correct rate in training data : %f and %f" %(ans[0],ans[2]))
	print("correct rate in testing data : %f and %f" %(ans[1],ans[3]))			
'''

if __name__ == "__main__":
	learning_rate,loop = python_get_input()
	print("Learning Rate : %s" %learning_rate)

	reading = reading_file()   
	
	row_data,expect = process_data(reading)

	traing_dataset,testing_dataset,group_set,total = divide_data(row_data,expect)

	print(traing_dataset)
	print(testing_dataset)
	print(group_set)
	#print(len(dataset)*2%3)

	weight = PLA(traing_dataset,group_set,learning_rate,loop)
	print(weight)

	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')
	sym = ['o',"x","*","+","1"]
	color = ["orange","purple","gold","gray","red","green","yellow","white","blue","black",""]
	color_train = ["green","red"]
	color_test = ["orange","blue"]

	temp_x,temp_s = traing_dataset[0]

	if len(temp_x) == 3:
		#fig = plt.figure()
		#ax1 = fig.add_subplot(111) #subplot(111)
		#ax1 = fig.add_subplot(111, projection='3d')

		print("len 3")
		for i in range(len(total)): #len(group_set)
			temp_set = []
			for x,s in traing_dataset:
				if s == total[i]:
					temp_set.append(x)
			#print(temp_set)
			x = [v[1] for v in temp_set]
			y = [v[2] for v in temp_set]
			#z = [v[3] for v in temp_set]
			print(x)
			print(y)
			#print(z)
			ax1.scatter( x, y,s = 100,c=color_train[i%2], marker= sym[i%5], label='O')
		
		for i in range(len(total)): #len(group_set)
			temp_set = []
			for x,s in testing_dataset:
				if s == total[i]:
					temp_set.append(x)
			#print(temp_set)
			x = [v[1] for v in temp_set]
			y = [v[2] for v in temp_set]
			#z = [v[3] for v in temp_set]
			print(x)
			print(y)
			#print(z)
			ax1.scatter( x, y,s = 100,c=color_test[i%2], marker= sym[i%5], label='O')


		for i in range(len(weight)):
			temp = np.ndarray.tolist(weight[i])
			l = np.linspace(-1,1)
			a,b = -temp[1]/temp[2], temp[0]/temp[2]
			ax1.plot(l, a*l + b, 'b-')

		plt.show()
'''
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
'''

'''
	ans_rate  = judge(traing_dataset,testing_dataset,weight,total)
	print(ans_rate)
'''


