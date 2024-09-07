def facto(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)


def main():
    n = int(input("숫자를 입력하세요-> "))

    print(f"{n}! = {facto(n)}")

if __name__ == "__main__":
    main()