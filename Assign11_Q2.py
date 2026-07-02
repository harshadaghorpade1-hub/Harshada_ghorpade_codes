#Write a program which accepts one number and print count of digits in that number.
def CountDigits(no):
    count = 0
    while no > 0:
        no = no // 10
        count += 1
    print(count)

def main():
    no = int(input("Enter the number: "))
    CountDigits(no)

if __name__ == "__main__":
    main()