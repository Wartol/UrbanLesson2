file = open('products.txt', 'r')
print(file.read())
print(file.seek(0))
line1 = set(file.read().split())
print(line1)
file.close()