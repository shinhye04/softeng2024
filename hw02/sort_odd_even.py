def is_even(n):
    return n % 2 == 0

def main():
    n = int(input("숫자를 입력하세요-> "))

    if is_even(n):
        print("짝수입니다.")
    else:
        print("홀수입니다.")

if __name__ == "__main__":
    main()