"""
05. 예외 처리 (Error Handling)

try-except, 커스텀 예외, 예외 체인 등을 학습합니다.
"""


def demonstrate_basic_exception():
    """기본 예외 처리"""
    print("=" * 50)
    print("1. 기본 예외 처리")
    print("=" * 50)
    
    # try-except
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"오류 발생: {e}")
    
    # 여러 예외 처리
    try:
        value = int("abc")
    except (ValueError, TypeError) as e:
        print(f"변환 오류: {e}")
    
    # 모든 예외 처리 (권장하지 않음)
    try:
        undefined_variable
    except Exception as e:
        print(f"예외: {type(e).__name__}: {e}")
    
    print()


def demonstrate_finally():
    """finally 절"""
    print("=" * 50)
    print("2. finally 절")
    print("=" * 50)
    
    def divide(a, b):
        try:
            result = a / b
            print(f"  결과: {result}")
            return result
        except ZeroDivisionError:
            print("  0으로 나눌 수 없습니다")
            return None
        finally:
            print("  정리 작업 수행")
    
    divide(10, 2)
    print()
    divide(10, 0)
    
    print()


def demonstrate_custom_exceptions():
    """커스텀 예외"""
    print("=" * 50)
    print("3. 커스텀 예외")
    print("=" * 50)
    
    class InvalidAgeError(Exception):
        """나이가 유효하지 않을 때 발생하는 예외"""
        def __init__(self, age, message="나이가 유효하지 않습니다"):
            self.age = age
            self.message = f"{message}: {age}"
            super().__init__(self.message)
    
    def set_age(age):
        if age < 0:
            raise InvalidAgeError(age, "나이는 0 이상이어야 합니다")
        if age > 150:
            raise InvalidAgeError(age, "나이가 너무 많습니다")
        return age
    
    try:
        set_age(-5)
    except InvalidAgeError as e:
        print(f"예외 발생: {e}")
        print(f"나이 값: {e.age}")
    
    print()


def demonstrate_exception_chaining():
    """예외 체인"""
    print("=" * 50)
    print("4. 예외 체인")
    print("=" * 50)
    
    try:
        try:
            result = 1 / 0
        except ZeroDivisionError as e:
            raise ValueError("계산 오류") from e
    except ValueError as e:
        print(f"오류: {e}")
        print(f"원인: {e.__cause__}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 예외 처리".center(50, "="))
    print()
    
    demonstrate_basic_exception()
    demonstrate_finally()
    demonstrate_custom_exceptions()
    demonstrate_exception_chaining()
    
    print("=" * 50)
    print("✅ 예외 처리 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

