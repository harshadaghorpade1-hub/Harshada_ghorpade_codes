#Write a program which accepts one number and check whether it is palindrome or not.
def ChkPalindrome(no):
    rev = 0
    temp = no
    while no > 0:
        result  = no % 10
        rev = (rev * 10) + result
        no = no // 10
    if temp == rev:
        print("palindrome")
    else:
        print("not a palindrome")

def main():
    no = int(input("Enter the number: "))
    ChkPalindrome(no)

if __name__ == "__main__":
    main()