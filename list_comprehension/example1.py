nums = [54, 22, 15, 48, 332, 1265, 1, 664, 223, 156]

evens= []

for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens) #[54, 22, 48, 332, 664, 156]

#using the list comprehension

evens = [num for num in nums if num % 2 ==0]

print(evens) #[54, 22, 48, 332, 664, 156] 
