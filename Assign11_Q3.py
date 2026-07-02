#Write a program which accepts one number and prints sum of digits in that number.
def SumDigits(no):
    sum = 0
    while no > 0:
        result  = no % 10
        sum += result
        no = no // 10
    print(sum)

def main():
    no = int(input("Enter the number: "))
    SumDigits(no)   

if __name__ == "__main__":
    main()