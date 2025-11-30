"""
02. 연산자 (Operators)

Python의 다양한 연산자를 학습합니다.
"""


def demonstrate_arithmetic_operators():
    """산술 연산자"""
    print("=" * 50)
    print("1. 산술 연산자")
    print("=" * 50)
    
    a, b = 10, 3
    
    print(f"a = {a}, b = {b}")
    print(f"덧셈 (a + b): {a + b}")
    print(f"뺄셈 (a - b): {a - b}")
    print(f"곱셈 (a * b): {a * b}")
    print(f"나눗셈 (a / b): {a / b}")  # float 반환
    print(f"정수 나눗셈 (a // b): {a // b}")  # int 반환
    print(f"나머지 (a % b): {a % b}")
    print(f"거듭제곱 (a ** b): {a ** b}")
    
    # 음수
    print(f"\n단항 마이너스 (-a): {-a}")
    print(f"단항 플러스 (+a): {+a}")
    print()


def demonstrate_comparison_operators():
    """비교 연산자"""
    print("=" * 50)
    print("2. 비교 연산자")
    print("=" * 50)
    
    x, y = 5, 10
    
    print(f"x = {x}, y = {y}")
    print(f"같음 (x == y): {x == y}")
    print(f"다름 (x != y): {x != y}")
    print(f"큼 (x > y): {x > y}")
    print(f"크거나 같음 (x >= y): {x >= y}")
    print(f"작음 (x < y): {x < y}")
    print(f"작거나 같음 (x <= y): {x <= y}")
    
    # 체인 비교
    print(f"\n체인 비교 (0 < x < y): {0 < x < y}")
    print(f"체인 비교 (0 < x < 3): {0 < x < 3}")
    print()


def demonstrate_logical_operators():
    """논리 연산자"""
    print("=" * 50)
    print("3. 논리 연산자")
    print("=" * 50)
    
    a, b = True, False
    
    print(f"a = {a}, b = {b}")
    print(f"AND (a and b): {a and b}")
    print(f"OR (a or b): {a or b}")
    print(f"NOT (!a): {not a}")
    print(f"NOT (!b): {not b}")
    
    # 단락 평가 (Short-circuit evaluation)
    print("\n단락 평가:")
    print(f"True or print('실행 안됨'): {True or 'X'}")
    print(f"False and print('실행 안됨'): {False and 'X'}")
    
    # 논리 연산자는 마지막 평가값을 반환
    print(f"\n'hello' or 'world': {'hello' or 'world'}")  # 'hello'
    print(f"'' or 'world': {'' or 'world'}")  # 'world'
    print(f"'hello' and 'world': {'hello' and 'world'}")  # 'world'
    print(f"'' and 'world': {'' and 'world'}")  # ''
    print()


def demonstrate_bitwise_operators():
    """비트 연산자"""
    print("=" * 50)
    print("4. 비트 연산자")
    print("=" * 50)
    
    a, b = 60, 13  # 60 = 0011 1100, 13 = 0000 1101
    
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    
    print(f"\nBitwise AND (a & b): {a & b} ({bin(a & b)})")
    print(f"Bitwise OR (a | b): {a | b} ({bin(a | b)})")
    print(f"Bitwise XOR (a ^ b): {a ^ b} ({bin(a ^ b)})")
    print(f"Bitwise NOT (~a): {~a} ({bin(~a)})")
    print(f"Left Shift (a << 2): {a << 2} ({bin(a << 2)})")
    print(f"Right Shift (a >> 2): {a >> 2} ({bin(a >> 2)})")
    
    # 실무 활용: 플래그 관리
    print("\n플래그 관리 예제:")
    READ = 1 << 0   # 0b001
    WRITE = 1 << 1  # 0b010
    EXECUTE = 1 << 2  # 0b100
    
    permissions = READ | WRITE  # 읽기 + 쓰기
    print(f"권한: {bin(permissions)}")
    print(f"읽기 권한 있음: {bool(permissions & READ)}")
    print(f"쓰기 권한 있음: {bool(permissions & WRITE)}")
    print(f"실행 권한 있음: {bool(permissions & EXECUTE)}")
    print()


def demonstrate_assignment_operators():
    """할당 연산자"""
    print("=" * 50)
    print("5. 할당 연산자")
    print("=" * 50)
    
    # 기본 할당
    x = 10
    print(f"x = 10: {x}")
    
    # 복합 할당
    x += 5  # x = x + 5
    print(f"x += 5: {x}")
    
    x -= 3  # x = x - 3
    print(f"x -= 3: {x}")
    
    x *= 2  # x = x * 2
    print(f"x *= 2: {x}")
    
    x //= 4  # x = x // 4
    print(f"x //= 4: {x}")
    
    x %= 5  # x = x % 5
    print(f"x %= 5: {x}")
    
    x **= 3  # x = x ** 3
    print(f"x **= 3: {x}")
    
    # 비트 연산 할당
    x = 12
    x &= 10  # x = x & 10
    print(f"\nx = 12, x &= 10: {x}")
    
    x |= 5  # x = x | 5
    print(f"x |= 5: {x}")
    print()


def demonstrate_membership_operators():
    """멤버십 연산자"""
    print("=" * 50)
    print("6. 멤버십 연산자 (in, not in)")
    print("=" * 50)
    
    # 리스트
    fruits = ["apple", "banana", "cherry"]
    print(f"과일 목록: {fruits}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'grape' in fruits: {'grape' in fruits}")
    print(f"'grape' not in fruits: {'grape' not in fruits}")
    
    # 문자열
    text = "Python Programming"
    print(f"\n문자열: '{text}'")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'Java' in text: {'Java' in text}")
    
    # 딕셔너리 (키만 체크)
    user = {"name": "Alice", "age": 30}
    print(f"\n사용자: {user}")
    print(f"'name' in user: {'name' in user}")
    print(f"'email' in user: {'email' in user}")
    print()


def demonstrate_identity_operators():
    """아이덴티티 연산자"""
    print("=" * 50)
    print("7. 아이덴티티 연산자 (is, is not)")
    print("=" * 50)
    
    # is는 객체의 identity(메모리 주소)를 비교
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(f"a = {a}, id: {id(a)}")
    print(f"b = {b}, id: {id(b)}")
    print(f"c = a, id: {id(c)}")
    
    print(f"\na == b (값 비교): {a == b}")
    print(f"a is b (identity 비교): {a is b}")
    print(f"a is c: {a is c}")
    
    # None 체크는 is 사용 권장
    value = None
    print(f"\nvalue is None: {value is None}")
    print(f"value == None: {value == None}  # 권장하지 않음")
    
    # 작은 정수는 캐싱됨 (singleton)
    x = 256
    y = 256
    print(f"\nx = 256, y = 256")
    print(f"x is y: {x is y}  # 작은 정수는 캐싱")
    
    x = 257
    y = 257
    print(f"\nx = 257, y = 257")
    print(f"x is y: {x is y}  # 큰 정수는 다른 객체")
    print()


def demonstrate_operator_precedence():
    """연산자 우선순위"""
    print("=" * 50)
    print("8. 연산자 우선순위")
    print("=" * 50)
    
    # 높음 -> 낮음
    # 1. () 괄호
    # 2. ** 거듭제곱
    # 3. +x, -x, ~x 단항 연산자
    # 4. *, /, //, % 곱셈/나눗셈
    # 5. +, - 덧셈/뺄셈
    # 6. <<, >> 시프트
    # 7. & 비트 AND
    # 8. ^ 비트 XOR
    # 9. | 비트 OR
    # 10. ==, !=, <, <=, >, >=, is, in 비교 연산자
    # 11. not 논리 NOT
    # 12. and 논리 AND
    # 13. or 논리 OR
    
    result1 = 2 + 3 * 4  # 곱셈 먼저
    result2 = (2 + 3) * 4  # 괄호 먼저
    
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    
    result3 = 2 ** 3 ** 2  # 우측부터 (오른쪽 결합)
    result4 = (2 ** 3) ** 2
    
    print(f"\n2 ** 3 ** 2 = {result3}  # 2 ** (3 ** 2)")
    print(f"(2 ** 3) ** 2 = {result4}")
    
    # 복잡한 표현식
    result5 = 10 + 5 * 2 - 3 ** 2
    print(f"\n10 + 5 * 2 - 3 ** 2 = {result5}")
    print("계산 순서: 3**2=9, 5*2=10, 10+10=20, 20-9=11")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 연산자".center(50, "="))
    print()
    
    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_bitwise_operators()
    demonstrate_assignment_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()
    demonstrate_operator_precedence()
    
    print("=" * 50)
    print("✅ 연산자 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

