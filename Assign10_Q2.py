#Write a program which accepts one number and prints sum of first N natural numbers.
def SumNatural(N):
    total = 0
    for i in range(1, N + 1):
        total += i

    print(f"Sum of first {N} natural numbers is: {total}")

def main():
    num = int(input("Enter a number: "))
    SumNatural(num)

if __name__ == "__main__":
    main()
