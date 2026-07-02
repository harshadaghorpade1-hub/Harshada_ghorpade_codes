#Write a program which accepts one number and prints all odd numbers till that number.
def PrintOdd(no):
    for i in range(1, no + 1):   
        if i % 2 != 0:           
            print(i)    

def main():
    no = int(input("Enter a number: "))
    PrintOdd(no)

if __name__ == "__main__":
    main()