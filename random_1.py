import random

# choice(seq) - This function returns a random element from the non-empty sequence

list1 = ['Apple','Mango','Banana','Watermelon']
print(random.choice(list1))
print('')

# shuffle(list) - This functions returns shuffled list.

random.shuffle(list1)
print(list1)
print('')

# randint(a, b) - This function returns a random integer between a and b inclusive

print(random.randint(1,8))
print('')

# seed() - This function always returns the same random value.

for i in range(4):
    random.seed(8)
    print(random.randint(1,82))
print('')

# random() -using random() get the next random number in the range (0.0, 1.0) means a random float value f, such that 0 is less than or equal to f and f is less than 1.

a = random.random()
print(a)
print('')

# randrange(start, stop, step) - This function returns random values in the given sequence based on step.

for i in range(3):
    print(random.randrange(10,100,5))