#list methods
basket = [1, 2, 3, 4, 5]
#adding
basket.append(6)
new_list = basket[:]  #points to not assigns
print(basket.append(6))  #produces none does not return list, only changes list
print(new_list)
print(basket)

#matrix
matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]

print(matrix[0][1])

#List slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'  #lists are mutible
new_cart = amazon_cart  #points to memory location
new_cart = amazon_cart[:]  #copies each item
new_cart = new_cart[:]  #copies each item preserves amazon cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#list slicing
stringslice = '[start:stop:step]'
#print(stringslice[::])
#print(stringslice[:])
#print(stringslice)

items = ['notebooks', 'sunglasses']
print(items[1])

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]
print(li3)
#data structure
