"""
05. 함수 (Functions)

함수 정의, 인자, 반환값, 람다 함수 등을 학습합니다.
"""


def demonstrate_basic_functions():
    """기본 함수 정의"""
    print("=" * 50)
    print("1. 기본 함수 정의")
    print("=" * 50)
    
    # 매개변수 없는 함수
    def greet():
        return "안녕하세요!"
    
    print(greet())
    
    # 매개변수 있는 함수
    def greet_person(name):
        return f"안녕하세요, {name}님!"
    
    print(greet_person("Alice"))
    
    # 여러 매개변수
    def add(a, b):
        return a + b
    
    print(f"10 + 20 = {add(10, 20)}")
    
    # 반환값 없는 함수 (암묵적으로 None 반환)
    def print_message(msg):
        print(f"  메시지: {msg}")
    
    result = print_message("테스트")
    print(f"반환값: {result}")
    
    print()


def demonstrate_default_arguments():
    """기본 인자 (Default Arguments)"""
    print("=" * 50)
    print("2. 기본 인자")
    print("=" * 50)
    
    def greet(name, greeting="안녕하세요"):
        return f"{greeting}, {name}님!"
    
    print(greet("Alice"))
    print(greet("Bob", "반갑습니다"))
    
    # 기본값은 함수 정의 시 한 번만 평가 (주의!)
    def append_to_list(value, lst=[]):  # ❌ 나쁜 예
        lst.append(value)
        return lst
    
    print(f"\n나쁜 예 - 가변 기본값:")
    print(append_to_list(1))  # [1]
    print(append_to_list(2))  # [1, 2] - 예상과 다름!
    
    # 올바른 방법
    def append_to_list_correct(value, lst=None):  # ✅ 좋은 예
        if lst is None:
            lst = []
        lst.append(value)
        return lst
    
    print(f"\n좋은 예 - None 사용:")
    print(append_to_list_correct(1))  # [1]
    print(append_to_list_correct(2))  # [2]
    
    print()


def demonstrate_keyword_arguments():
    """키워드 인자 (Keyword Arguments)"""
    print("=" * 50)
    print("3. 키워드 인자")
    print("=" * 50)
    
    def create_user(name, age, city="Seoul", active=True):
        return {
            "name": name,
            "age": age,
            "city": city,
            "active": active
        }
    
    # 위치 인자
    user1 = create_user("Alice", 25)
    print(f"위치 인자: {user1}")
    
    # 키워드 인자
    user2 = create_user(name="Bob", age=30, city="Busan")
    print(f"키워드 인자: {user2}")
    
    # 혼합 (위치 인자는 키워드 인자보다 앞에)
    user3 = create_user("Charlie", age=35, active=False)
    print(f"혼합: {user3}")
    
    print()


def demonstrate_args_kwargs():
    """*args와 **kwargs"""
    print("=" * 50)
    print("4. *args와 **kwargs")
    print("=" * 50)
    
    # *args: 가변 위치 인자
    def sum_all(*args):
        print(f"  args 타입: {type(args)}")  # tuple
        print(f"  args 값: {args}")
        return sum(args)
    
    print("*args 예제:")
    print(f"결과: {sum_all(1, 2, 3, 4, 5)}\n")
    
    # **kwargs: 가변 키워드 인자
    def print_info(**kwargs):
        print(f"  kwargs 타입: {type(kwargs)}")  # dict
        print(f"  kwargs 값: {kwargs}")
        for key, value in kwargs.items():
            print(f"    {key}: {value}")
    
    print("**kwargs 예제:")
    print_info(name="Alice", age=25, city="Seoul")
    print()
    
    # 혼합 사용
    def create_person(name, *hobbies, **details):
        print(f"이름: {name}")
        print(f"취미: {hobbies}")
        print(f"상세정보: {details}")
    
    print("혼합 예제:")
    create_person("Bob", "독서", "영화", "코딩", age=30, city="Busan")
    
    print()


def demonstrate_unpacking():
    """인자 언패킹"""
    print("=" * 50)
    print("5. 인자 언패킹")
    print("=" * 50)
    
    def calculate(a, b, c):
        return a + b + c
    
    # 리스트/튜플 언패킹
    numbers = [10, 20, 30]
    result = calculate(*numbers)
    print(f"리스트 언패킹: {numbers} -> {result}")
    
    # 딕셔너리 언패킹
    def create_user(name, age, city):
        return f"{name} ({age}세) - {city}"
    
    user_data = {"name": "Alice", "age": 25, "city": "Seoul"}
    user = create_user(**user_data)
    print(f"딕셔너리 언패킹: {user}")
    
    print()


def demonstrate_return_values():
    """반환값"""
    print("=" * 50)
    print("6. 반환값")
    print("=" * 50)
    
    # 단일 반환값
    def square(x):
        return x ** 2
    
    print(f"square(5) = {square(5)}")
    
    # 여러 반환값 (튜플로 반환)
    def divide(a, b):
        quotient = a // b
        remainder = a % b
        return quotient, remainder
    
    q, r = divide(17, 5)
    print(f"17 ÷ 5 = {q} ... {r}")
    
    # 조건부 반환
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "F"
    
    print(f"점수 85 -> 학점 {get_grade(85)}")
    
    # 조기 반환 (early return)
    def validate_age(age):
        if age < 0:
            return "나이는 0 이상이어야 합니다"
        if age > 150:
            return "나이가 너무 많습니다"
        return "정상"
    
    print(f"나이 -5 검증: {validate_age(-5)}")
    print(f"나이 25 검증: {validate_age(25)}")
    
    print()


def demonstrate_lambda():
    """람다 함수"""
    print("=" * 50)
    print("7. 람다 함수")
    print("=" * 50)
    
    # 기본 람다
    square = lambda x: x ** 2
    print(f"lambda x: x ** 2")
    print(f"square(5) = {square(5)}")
    
    # 여러 인자
    add = lambda a, b: a + b
    print(f"\nlambda a, b: a + b")
    print(f"add(10, 20) = {add(10, 20)}")
    
    # 정렬에 사용
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    
    sorted_by_age = sorted(users, key=lambda u: u["age"])
    print(f"\n나이순 정렬:")
    for user in sorted_by_age:
        print(f"  {user['name']}: {user['age']}세")
    
    # map, filter와 함께 사용
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    
    print(f"\nmap - 제곱: {squares}")
    print(f"filter - 짝수: {evens}")
    
    print()


def demonstrate_scope():
    """변수 스코프"""
    print("=" * 50)
    print("8. 변수 스코프 (LEGB)")
    print("=" * 50)
    
    # LEGB: Local, Enclosing, Global, Built-in
    
    global_var = "전역"
    
    def outer():
        enclosing_var = "외부 함수"
        
        def inner():
            local_var = "지역"
            print(f"  Local: {local_var}")
            print(f"  Enclosing: {enclosing_var}")
            print(f"  Global: {global_var}")
            print(f"  Built-in: {len([1, 2, 3])}")  # len은 내장 함수
        
        inner()
    
    outer()
    
    # global 키워드
    counter = 0
    
    def increment():
        global counter
        counter += 1
        return counter
    
    print(f"\n글로벌 카운터:")
    print(f"  {increment()}")
    print(f"  {increment()}")
    print(f"  {increment()}")
    
    # nonlocal 키워드
    def outer_counter():
        count = 0
        
        def increment():
            nonlocal count
            count += 1
            return count
        
        return increment
    
    counter_func = outer_counter()
    print(f"\nnonlocal 카운터:")
    print(f"  {counter_func()}")
    print(f"  {counter_func()}")
    print(f"  {counter_func()}")
    
    print()


def demonstrate_closures():
    """클로저 (Closures)"""
    print("=" * 50)
    print("9. 클로저")
    print("=" * 50)
    
    # 클로저: 외부 함수의 변수를 기억하는 내부 함수
    def make_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier
    
    times_2 = make_multiplier(2)
    times_5 = make_multiplier(5)
    
    print(f"times_2(10) = {times_2(10)}")
    print(f"times_5(10) = {times_5(10)}")
    
    # 실무 활용: 설정 저장
    def create_greeter(greeting):
        def greet(name):
            return f"{greeting}, {name}!"
        return greet
    
    korean_greeter = create_greeter("안녕하세요")
    english_greeter = create_greeter("Hello")
    
    print(f"\n{korean_greeter('철수')}")
    print(f"{english_greeter('John')}")
    
    # 클로저로 private 변수 구현
    def create_account(initial_balance):
        balance = initial_balance
        
        def deposit(amount):
            nonlocal balance
            balance += amount
            return balance
        
        def withdraw(amount):
            nonlocal balance
            if balance >= amount:
                balance -= amount
                return balance
            return "잔액 부족"
        
        def get_balance():
            return balance
        
        return deposit, withdraw, get_balance
    
    deposit, withdraw, get_balance = create_account(1000)
    print(f"\n초기 잔액: {get_balance()}")
    print(f"입금 500: {deposit(500)}")
    print(f"출금 300: {withdraw(300)}")
    print(f"현재 잔액: {get_balance()}")
    
    print()


def demonstrate_decorators_intro():
    """데코레이터 소개 (간단)"""
    print("=" * 50)
    print("10. 데코레이터 소개")
    print("=" * 50)
    
    # 함수도 객체 (First-class citizen)
    def hello():
        return "Hello!"
    
    func = hello  # 함수를 변수에 할당
    print(f"함수 객체: {func()}")
    
    # 고차 함수 (Higher-order function)
    def execute_twice(func):
        func()
        func()
    
    def say_hi():
        print("  Hi!")
    
    print("\n함수를 인자로 전달:")
    execute_twice(say_hi)
    
    # 간단한 데코레이터
    def uppercase_decorator(func):
        def wrapper():
            result = func()
            return result.upper()
        return wrapper
    
    @uppercase_decorator
    def greet():
        return "hello, world"
    
    print(f"\n데코레이터 적용: {greet()}")
    
    print("(상세한 데코레이터는 중급 과정에서 학습)")
    print()


def demonstrate_recursion():
    """재귀 함수"""
    print("=" * 50)
    print("11. 재귀 함수")
    print("=" * 50)
    
    # 팩토리얼
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    print(f"5! = {factorial(5)}")
    
    # 피보나치
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"\n피보나치 수열 (0-7):")
    fib_sequence = [fibonacci(i) for i in range(8)]
    print(f"  {fib_sequence}")
    
    # 리스트 합계 (재귀)
    def sum_list(lst):
        if not lst:
            return 0
        return lst[0] + sum_list(lst[1:])
    
    numbers = [1, 2, 3, 4, 5]
    print(f"\n재귀로 합계: {numbers} = {sum_list(numbers)}")
    
    print()


def demonstrate_docstrings():
    """문서화 문자열 (Docstrings)"""
    print("=" * 50)
    print("12. Docstrings")
    print("=" * 50)
    
    def calculate_area(width, height):
        """
        사각형의 넓이를 계산합니다.
        
        Args:
            width (float): 너비
            height (float): 높이
        
        Returns:
            float: 사각형의 넓이
        
        Examples:
            >>> calculate_area(5, 10)
            50.0
        """
        return width * height
    
    print(f"함수: {calculate_area.__name__}")
    print(f"Docstring:\n{calculate_area.__doc__}")
    
    # help() 함수로 확인
    print("\nhelp(calculate_area):")
    help(calculate_area)
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 함수".center(50, "="))
    print()
    
    demonstrate_basic_functions()
    demonstrate_default_arguments()
    demonstrate_keyword_arguments()
    demonstrate_args_kwargs()
    demonstrate_unpacking()
    demonstrate_return_values()
    demonstrate_lambda()
    demonstrate_scope()
    demonstrate_closures()
    demonstrate_decorators_intro()
    demonstrate_recursion()
    demonstrate_docstrings()
    
    print("=" * 50)
    print("✅ 함수 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

