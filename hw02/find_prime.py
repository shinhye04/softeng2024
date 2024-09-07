# from hw02.prime_dist import is_prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        if is_prime(i):
            count += 1
    return count

def main():
    n = int(input("숫자를 입력하세요-> "))

    prime_count = count_prime(n)
    print(f"1부터 {n}까지의 소수는 {prime_count}개 입니다. ")

if __name__ == '__main__':
    main()