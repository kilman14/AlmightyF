my_number = [1,2,3,4,5]
some_num = []
for num in my_number:
    if (num % 2 != 0 or num % 3!=0):
        continue
    some_num.append(num)
   
print(some_num)