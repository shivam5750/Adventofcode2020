#Reaing Input from file
with open('input6.txt', 'r') as file:
	ques = file.read().split('\n\n')                                      
	
map1 = [''.join(char.split('\n')) for char in ques ]   #here input will [[a,b,c]]
map2 = [' '.join(char.split('\n')).split(' ') for char in ques ] # [[abc]]
# print(map)
# print(map2)

#Part1
def anyoneAnswered(map1):
	valid = 0
	for question in map1:
		my_set = set(question)
		valid += len(my_set)
	return valid

print(anyoneAnswered(map1))
	

#Part-2
def everyoneAnswered(map2):
	ans=0
	group_of_person ={}
	for ques in map2:
		if len(ques) == 1:
			ans +=len(ques[0])
			

		else:
			group_of_person ={}

			for person in ques:
			 	for answer in person:
			 		
			 		if answer in group_of_person:
			 			group_of_person[answer] +=1
			 		else:
			 			group_of_person[answer] = 1
			for item in group_of_person.items():
			 	if item[1] == len(ques):
			 		ans +=1
	return ans

print(everyoneAnswered(map2))

	
