"""
04. 반복문 (Loops)

for, while 반복문과 컴프리헨션을 학습합니다.
"""


def demonstrate_for_loop():
    """for 반복문"""
    print("=" * 50)
    print("1. for 반복문")
    print("=" * 50)
    
    # 리스트 순회
    fruits = ["apple", "banana", "cherry"]
    print("과일 목록:")
    for fruit in fruits:
        print(f"  - {fruit}")
    
    # range() 사용
    print("\nrange(5):")
    for i in range(5):
        print(f"  {i}", end=" ")
    print()
    
    print("\nrange(1, 6):")
    for i in range(1, 6):
        print(f"  {i}", end=" ")
    print()
    
    print("\nrange(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  {i}", end=" ")
    print("\n")
    
    # 문자열 순회
    text = "Python"
    print(f"'{text}' 순회:")
    for char in text:
        print(f"  {char}", end=" ")
    print("\n")


def demonstrate_enumerate():
    """enumerate() - 인덱스와 함께 순회"""
    print("=" * 50)
    print("2. enumerate()")
    print("=" * 50)
    
    languages = ["Python", "Java", "Go", "Rust"]
    
    # 기본 사용
    print("프로그래밍 언어:")
    for index, lang in enumerate(languages):
        print(f"  {index}: {lang}")
    
    # 시작 인덱스 지정
    print("\n시작 인덱스 1:")
    for index, lang in enumerate(languages, start=1):
        print(f"  {index}. {lang}")
    
    print()


def demonstrate_zip():
    """zip() - 여러 시퀀스 동시 순회"""
    print("=" * 50)
    print("3. zip()")
    print("=" * 50)
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["Seoul", "Busan", "Incheon"]
    
    print("사용자 정보:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name} ({age}세) - {city}")
    
    # 길이가 다른 경우: 가장 짧은 것에 맞춤
    scores = [90, 85]
    print("\n점수 (짧은 리스트):")
    for name, score in zip(names, scores):
        print(f"  {name}: {score}점")
    
    # zip으로 딕셔너리 생성
    user_dict = dict(zip(names, ages))
    print(f"\n딕셔너리 생성: {user_dict}")
    
    print()


def demonstrate_while_loop():
    """while 반복문"""
    print("=" * 50)
    print("4. while 반복문")
    print("=" * 50)
    
    # 기본 while 문
    count = 0
    print("0부터 4까지:")
    while count < 5:
        print(f"  count = {count}")
        count += 1
    
    # 무한 루프 + break
    print("\n무한 루프 + break:")
    total = 0
    while True:
        total += 1
        if total >= 3:
            break
        print(f"  total = {total}")
    print(f"  최종 total = {total}")
    
    print()


def demonstrate_break_continue():
    """break, continue, pass"""
    print("=" * 50)
    print("5. break, continue, pass")
    print("=" * 50)
    
    # break: 반복문 종료
    print("break - 5를 찾으면 중단:")
    for i in range(10):
        if i == 5:
            print(f"  {i}를 찾았습니다. 중단!")
            break
        print(f"  {i}", end=" ")
    print()
    
    # continue: 현재 반복 건너뛰기
    print("\ncontinue - 짝수만 출력:")
    for i in range(10):
        if i % 2 != 0:
            continue
        print(f"  {i}", end=" ")
    print()
    
    # pass: 아무것도 하지 않음 (자리 표시자)
    print("\npass - 자리 표시자:")
    for i in range(3):
        if i == 1:
            pass  # 나중에 구현 예정
        else:
            print(f"  {i}", end=" ")
    print("\n")


def demonstrate_for_else():
    """for-else, while-else"""
    print("=" * 50)
    print("6. for-else, while-else")
    print("=" * 50)
    
    # for-else: break 없이 정상 종료 시 else 실행
    def find_number(numbers, target):
        for num in numbers:
            if num == target:
                print(f"  {target}을 찾았습니다!")
                break
        else:
            print(f"  {target}을 찾지 못했습니다.")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"숫자 목록: {numbers}")
    find_number(numbers, 3)
    find_number(numbers, 10)
    
    # while-else
    print("\nwhile-else:")
    count = 0
    while count < 3:
        print(f"  count = {count}")
        count += 1
    else:
        print("  while 루프가 정상 종료되었습니다")
    
    print()


def demonstrate_nested_loops():
    """중첩 반복문"""
    print("=" * 50)
    print("7. 중첩 반복문")
    print("=" * 50)
    
    # 구구단
    print("구구단 2단, 3단:")
    for i in [2, 3]:
        for j in range(1, 6):
            print(f"  {i} x {j} = {i * j}")
        print()
    
    # 2차원 리스트 순회
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("행렬 출력:")
    for row in matrix:
        for col in row:
            print(f"  {col}", end=" ")
        print()
    
    print()


def demonstrate_list_comprehension():
    """리스트 컴프리헨션"""
    print("=" * 50)
    print("8. 리스트 컴프리헨션")
    print("=" * 50)
    
    # 기본 형태
    squares = [x ** 2 for x in range(6)]
    print(f"제곱수: {squares}")
    
    # 조건문 포함
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(f"짝수의 제곱: {even_squares}")
    
    # if-else 포함
    labels = ["짝수" if x % 2 == 0 else "홀수" for x in range(6)]
    print(f"라벨: {labels}")
    
    # 중첩 컴프리헨션
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"행렬:\n{matrix}")
    
    # 2차원 리스트 평탄화
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [num for row in nested for num in row]
    print(f"\n중첩 리스트: {nested}")
    print(f"평탄화: {flattened}")
    
    print()


def demonstrate_dict_comprehension():
    """딕셔너리 컴프리헨션"""
    print("=" * 50)
    print("9. 딕셔너리 컴프리헨션")
    print("=" * 50)
    
    # 기본 형태
    squares_dict = {x: x ** 2 for x in range(6)}
    print(f"제곱수 딕셔너리: {squares_dict}")
    
    # 조건문 포함
    even_squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
    print(f"짝수의 제곱: {even_squares_dict}")
    
    # 키-값 스왑
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(f"\n원본: {original}")
    print(f"스왑: {swapped}")
    
    # 필터링
    users = {"alice": 25, "bob": 17, "charlie": 30, "david": 16}
    adults = {name: age for name, age in users.items() if age >= 18}
    print(f"\n전체 사용자: {users}")
    print(f"성인만: {adults}")
    
    print()


def demonstrate_set_comprehension():
    """셋 컴프리헨션"""
    print("=" * 50)
    print("10. 셋 컴프리헨션")
    print("=" * 50)
    
    # 기본 형태
    squares_set = {x ** 2 for x in range(-5, 6)}
    print(f"제곱수 집합: {squares_set}")
    
    # 중복 제거
    text = "hello world"
    unique_chars = {char for char in text if char != ' '}
    print(f"고유 문자: {unique_chars}")
    
    # 조건문 포함
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_evens = {x for x in numbers if x % 2 == 0}
    print(f"숫자 목록: {numbers}")
    print(f"고유 짝수: {unique_evens}")
    
    print()


def demonstrate_generator_expression():
    """제너레이터 표현식"""
    print("=" * 50)
    print("11. 제너레이터 표현식")
    print("=" * 50)
    
    # 리스트 vs 제너레이터
    list_comp = [x ** 2 for x in range(5)]
    gen_exp = (x ** 2 for x in range(5))
    
    print(f"리스트 컴프리헨션: {list_comp}")
    print(f"제너레이터 표현식: {gen_exp}")
    print(f"제너레이터 타입: {type(gen_exp)}")
    
    # 제너레이터는 한 번만 순회 가능
    print("\n제너레이터 순회:")
    for value in gen_exp:
        print(f"  {value}", end=" ")
    print()
    
    # 메모리 효율적 - 큰 데이터셋 처리
    print("\n메모리 효율성:")
    import sys
    list_obj = [x for x in range(1000)]
    gen_obj = (x for x in range(1000))
    
    print(f"리스트 크기: {sys.getsizeof(list_obj):,} bytes")
    print(f"제너레이터 크기: {sys.getsizeof(gen_obj):,} bytes")
    
    # sum(), max(), any() 등과 함께 사용
    total = sum(x ** 2 for x in range(10))
    print(f"\n0-9 제곱의 합: {total}")
    
    print()


def demonstrate_itertools():
    """itertools 모듈"""
    print("=" * 50)
    print("12. itertools 모듈")
    print("=" * 50)
    
    import itertools
    
    # count: 무한 카운터
    print("count(10, 2) - 처음 5개:")
    for i, value in enumerate(itertools.count(10, 2)):
        if i >= 5:
            break
        print(f"  {value}", end=" ")
    print()
    
    # cycle: 무한 반복
    print("\ncycle(['A', 'B', 'C']) - 처음 7개:")
    for i, value in enumerate(itertools.cycle(['A', 'B', 'C'])):
        if i >= 7:
            break
        print(f"  {value}", end=" ")
    print()
    
    # repeat: 반복
    print("\nrepeat('X', 3):")
    for value in itertools.repeat('X', 3):
        print(f"  {value}", end=" ")
    print()
    
    # chain: 여러 이터러블 연결
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print(f"\nchain({list1}, {list2}):")
    for value in itertools.chain(list1, list2):
        print(f"  {value}", end=" ")
    print()
    
    # combinations: 조합
    print("\ncombinations(['A', 'B', 'C'], 2):")
    for combo in itertools.combinations(['A', 'B', 'C'], 2):
        print(f"  {combo}")
    
    # permutations: 순열
    print("\npermutations(['A', 'B', 'C'], 2):")
    for perm in itertools.permutations(['A', 'B', 'C'], 2):
        print(f"  {perm}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 반복문".center(50, "="))
    print()
    
    demonstrate_for_loop()
    demonstrate_enumerate()
    demonstrate_zip()
    demonstrate_while_loop()
    demonstrate_break_continue()
    demonstrate_for_else()
    demonstrate_nested_loops()
    demonstrate_list_comprehension()
    demonstrate_dict_comprehension()
    demonstrate_set_comprehension()
    demonstrate_generator_expression()
    demonstrate_itertools()
    
    print("=" * 50)
    print("✅ 반복문 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

