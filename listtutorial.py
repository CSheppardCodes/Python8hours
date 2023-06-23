#list methods
basket = [1, 2, 3, 4, 5]
# print(len(basket))

# basket.append(6)  #no return, in place
# new_list = basket
# print(new_list)
# basket.insert(0, 100)
# print(new_list)
# print(basket)
# basket.extend([101, 102])  #hover to see it returns none
# print(new_list)
# print(basket)
# basket.pop(4)
# basket.pop()
# basket.pop()
# justreturned = basket.pop()  #returns popped value
# basket.remove(100)  #in place
# basket.insert(3, 4)
# print(new_list)
# print(basket)
# basket.insert(0, basket.pop(-1))  #cool
# print(new_list)
# print(basket)
# print(justreturned)

#list methods 2
print(basket.index(2, 0, 2))  #return index
print(1 in basket)  #in is a keyword
print('i' in 'I like icecream')
print('Ilikeicecream'.count('i'))

#list methods 3
alpha = ['a', 'b', 'c', 'd', 'e', 'd', 'a', 'c']
#alpha.sort() #changes original

print(sorted(alpha))  #makes a copy
#same as
new_al = alpha.copy()
new_al.sort()
print(alpha)
print(new_al)
print(alpha.reverse())
#https://youtu.be/4uBbCUjJ_G8?t=12391