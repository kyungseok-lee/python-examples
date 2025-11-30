"""
05. 테스팅 (Testing)

pytest를 사용한 테스트 작성을 학습합니다.
실제 테스트는 test_*.py 파일에 작성합니다.
"""


def demonstrate_testing_basics():
    """테스팅 기본 개념"""
    print("=" * 50)
    print("1. 테스팅 기본")
    print("=" * 50)
    
    print("pytest 설치:")
    print("  pip install pytest")
    
    print("\n테스트 파일 구조:")
    print("  tests/")
    print("    test_example.py")
    print("    test_user.py")
    
    print("\n테스트 실행:")
    print("  pytest")
    print("  pytest tests/test_example.py")
    print("  pytest -v  # verbose")
    print()


def demonstrate_test_example():
    """테스트 예제 코드"""
    print("=" * 50)
    print("2. 테스트 예제")
    print("=" * 50)
    
    print("# test_example.py 예제:")
    print("""
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_list():
    items = [1, 2, 3]
    assert len(items) == 3
    assert 2 in items
""")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 테스팅".center(50, "="))
    print()
    
    demonstrate_testing_basics()
    demonstrate_test_example()
    
    print("=" * 50)
    print("✅ 테스팅 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

