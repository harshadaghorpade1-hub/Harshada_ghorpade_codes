#Write a program which accepts one number and prints factorial of that number.
def PrintFactorial(no):
    f = 1
    for i in range(1, no + 1):
        f *= i
    print(f)

def main():
    no = int(input("Enter number: "))
    print("Factorial of", no, "is:")
    PrintFactorial(no)

if __name__ == "__main__":
    main()
