import random



def main():

   # a main() function to check if the module has been launched in the main scope below:
    print("This program accepts a sequence of random inputs")

def items_as_str():
    print("items")

print("Your output in random order:")
a = int(input(print("How many items you want to shuffle?, enter 0 if none "))) #allows user to enter items and press 0 when done
b = []
for i in range(0, a):      #for loop which enables items to be entered and printed in original order.
    n = input('Please enter a item: ')
    b.append(n)
print("your items in orginal order", b)
random.shuffle(b)
#
print("your items in random order", b)

#module includes a main() function to check if the module has been launched in the main scope below:
if __name__ == "__main__":
    main()


#didn't have time to finish this question 