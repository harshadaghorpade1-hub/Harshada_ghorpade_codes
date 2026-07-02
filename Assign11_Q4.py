#Write a program which accepts one number and prints reverse of that number.
def ReverseDigits(no):
    rev = 0
    while no > 0:
        result  = no % 10
        rev = (rev * 10) + result
        no = no // 10
    print(rev)

def main():
    no = int(input("Enter the number: "))
    ReverseDigits(no)

if __name__ == "__main__":
    main()  










    