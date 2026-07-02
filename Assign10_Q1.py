#Write a program which accepts one number and prints multiplication table of that number.
def PrintTable(no):
    for i in range(1, 11):
        result = no * i
        #print(no, "x", i, "=", result)
        print(result)

def main():
    no = int(input("Enter number: "))
    print("Display table of ", no, "is: ")
    PrintTable(no)

if __name__ == "__main__":
    main()




