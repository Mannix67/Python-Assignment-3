# Python-Assignment-3
2 questions

![Screenshot (71)](https://user-images.githubusercontent.com/84920516/141844442-cdbde3a1-108c-44a3-9dff-03ea7b648a51.png)
![Screenshot (72)](https://user-images.githubusercontent.com/84920516/141844458-0f5f1b85-c764-4310-9049-d5e840c04eb7.png)
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


![Screenshot (73)](https://user-images.githubusercontent.com/84920516/141844489-c194b848-c831-490a-a358-b86827ea2af2.png)
![Screenshot (74)](https://user-images.githubusercontent.com/84920516/141844523-c33399f5-aeca-4285-811a-3c3d92fddaad.png)

![Screenshot (75)](https://user-images.githubusercontent.com/84920516/141844537-93e7188b-7acf-488c-82d1-bedfd3aaa00b.png)
