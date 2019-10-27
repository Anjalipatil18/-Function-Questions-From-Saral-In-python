def list_change(list1, list2):
	new_list=[]
	i=0
	while i<len(list1):
		if i<list1[i] :
			multiply=list1[i]*list2[i]
			new_list.append(multiply)
		i=i+1
	return new_list
multiple_list=list_change([5, 10, 50, 20], [2, 20, 3, 5])
print multiple_list



			
			
			
