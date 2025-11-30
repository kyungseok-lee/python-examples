"""
01. 변수와 자료형 (Variables and Types)

Python의 기본 자료형과 변수 사용법을 학습합니다.
"""


def demonstrate_variables():
    """변수 선언과 할당"""
    print("=" * 50)
    print("1. 변수 선언과 할당")
    print("=" * 50)
    
    # Python은 동적 타이핑 언어 - 타입 선언 불필요
    name = "Python"
    version = 3.11
    is_awesome = True
    
    print(f"언어: {name}")
    print(f"버전: {version}")
    print(f"멋진가요? {is_awesome}")
    
    # 변수 재할당 가능 (타입도 변경 가능)
    version = "3.11.0"  # int -> str
    print(f"버전 (문자열): {version}")
    print()


def demonstrate_numeric_types():
    """숫자 자료형: int, float, complex"""
    print("=" * 50)
    print("2. 숫자 자료형")
    print("=" * 50)
    
    # Integer (정수)
    age = 30
    year = 2025
    big_number = 1_000_000_000  # 언더스코어로 가독성 향상
    
    print(f"나이: {age}, 타입: {type(age)}")
    print(f"10억: {big_number:,}")
    
    # Float (실수)
    pi = 3.14159
    scientific = 1.5e-4  # 과학적 표기법
    
    print(f"원주율: {pi}")
    print(f"과학적 표기: {scientific}")
    
    # Complex (복소수)
    complex_num = 3 + 4j
    print(f"복소수: {complex_num}")
    print(f"실수부: {complex_num.real}, 허수부: {complex_num.imag}")
    print()


def demonstrate_string_type():
    """문자열 자료형"""
    print("=" * 50)
    print("3. 문자열 자료형")
    print("=" * 50)
    
    # 다양한 문자열 선언 방법
    single_quote = 'Hello'
    double_quote = "World"
    triple_quote = """여러 줄
    문자열을
    작성할 수 있습니다."""
    
    print(f"단일 따옴표: {single_quote}")
    print(f"이중 따옴표: {double_quote}")
    print(f"삼중 따옴표:\n{triple_quote}")
    
    # 문자열 연산
    full_name = single_quote + " " + double_quote
    repeated = "Ha" * 3
    
    print(f"연결: {full_name}")
    print(f"반복: {repeated}")
    
    # 인덱싱과 슬라이싱
    text = "Python Programming"
    print(f"첫 글자: {text[0]}")
    print(f"마지막 글자: {text[-1]}")
    print(f"슬라이싱 [0:6]: {text[0:6]}")
    print(f"슬라이싱 [7:]: {text[7:]}")
    print()


def demonstrate_boolean_type():
    """불린 자료형"""
    print("=" * 50)
    print("4. 불린 자료형")
    print("=" * 50)
    
    is_active = True
    is_deleted = False
    
    print(f"활성화: {is_active}")
    print(f"삭제됨: {is_deleted}")
    
    # Truthy/Falsy 값
    print("\nTruthy/Falsy 체크:")
    print(f"bool(0) = {bool(0)}")  # False
    print(f"bool(1) = {bool(1)}")  # True
    print(f"bool('') = {bool('')}")  # False
    print(f"bool('text') = {bool('text')}")  # True
    print(f"bool([]) = {bool([])}")  # False
    print(f"bool([1, 2]) = {bool([1, 2])}")  # True
    print()


def demonstrate_none_type():
    """None 타입"""
    print("=" * 50)
    print("5. None 타입")
    print("=" * 50)
    
    # None은 값이 없음을 나타내는 특수 상수
    result = None
    
    print(f"result: {result}")
    print(f"type: {type(result)}")
    print(f"is None: {result is None}")
    print(f"bool(None): {bool(None)}")  # False
    
    # None 체크는 'is' 연산자 사용 권장
    if result is None:
        print("result는 None입니다")
    print()


def demonstrate_type_conversion():
    """타입 변환 (Type Conversion)"""
    print("=" * 50)
    print("6. 타입 변환")
    print("=" * 50)
    
    # 명시적 변환
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    
    print(f"문자열 '{num_str}' -> int: {num_int}, type: {type(num_int)}")
    print(f"문자열 '{num_str}' -> float: {num_float}, type: {type(num_float)}")
    
    # 숫자를 문자열로
    number = 456
    str_number = str(number)
    print(f"숫자 {number} -> 문자열: '{str_number}', type: {type(str_number)}")
    
    # 불린 변환
    print(f"\nint(True): {int(True)}")  # 1
    print(f"int(False): {int(False)}")  # 0
    print(f"bool(0): {bool(0)}")  # False
    print(f"bool(42): {bool(42)}")  # True
    
    # 변환 실패 시 예외 발생
    try:
        invalid = int("abc")
    except ValueError as e:
        print(f"\n오류 발생: {e}")
    print()


def demonstrate_type_checking():
    """타입 체크"""
    print("=" * 50)
    print("7. 타입 체크")
    print("=" * 50)
    
    value = 42
    
    # type() 함수
    print(f"type(42): {type(value)}")
    print(f"type(42) == int: {type(value) == int}")
    
    # isinstance() 함수 (권장)
    print(f"\nisinstance(42, int): {isinstance(value, int)}")
    print(f"isinstance(42, (int, float)): {isinstance(value, (int, float))}")
    
    # 여러 타입 체크
    values = [42, 3.14, "text", True, None, [1, 2, 3]]
    for val in values:
        print(f"{val!r:15} -> {type(val).__name__}")
    print()


def demonstrate_variable_scope():
    """변수 스코프 (심화)"""
    print("=" * 50)
    print("8. 변수 스코프")
    print("=" * 50)
    
    # 전역 변수
    global_var = "전역 변수"
    
    def outer_function():
        # 외부 함수의 로컬 변수
        outer_var = "외부 함수 변수"
        
        def inner_function():
            # 내부 함수의 로컬 변수
            inner_var = "내부 함수 변수"
            print(f"  내부 함수에서: {global_var}")
            print(f"  내부 함수에서: {outer_var}")
            print(f"  내부 함수에서: {inner_var}")
        
        inner_function()
        print(f"외부 함수에서: {outer_var}")
    
    outer_function()
    print(f"전역 스코프에서: {global_var}")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 변수와 자료형".center(50, "="))
    print()
    
    demonstrate_variables()
    demonstrate_numeric_types()
    demonstrate_string_type()
    demonstrate_boolean_type()
    demonstrate_none_type()
    demonstrate_type_conversion()
    demonstrate_type_checking()
    demonstrate_variable_scope()
    
    print("=" * 50)
    print("✅ 변수와 자료형 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

