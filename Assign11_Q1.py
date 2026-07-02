#Write a program which accepts one number and check whether it is prime or not.
def ChkPrime(no):
    if no <= 1:
        print("Not a prime number")
        return

    for i in range(2, no):
        if(no % i == 0):
            print("Not a prime number")
            return
    
    print("Prime number")

def main():
    no = int(input("Enter the number: "))
    ChkPrime(no)

if __name__ == "__main__":
    main()