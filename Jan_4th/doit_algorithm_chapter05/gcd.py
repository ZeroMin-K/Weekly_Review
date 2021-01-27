# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
    # 정수값 x와 y의 최대 공약수 반환
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('두 정수값의 최대 공약수 계산')
    x = int(input('첫 번째 정수값 입력: '))
    y = int(input('두 번째 정수값 입력: '))

    print(f'두 정수값의 최대 공약수는 {gcd(x, y)}')
