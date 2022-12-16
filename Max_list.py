# Program to print maximum number from a given list

l = []
for i in range(5):
    a = int(input("Enter number"))
    l.append(a)
print("List is:",l)
print("Maximum number in the list is:",max(l))