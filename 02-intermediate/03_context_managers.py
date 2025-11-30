"""
03. 컨텍스트 매니저 (Context Managers)

with문과 컨텍스트 매니저를 사용한 리소스 관리를 학습합니다.
"""

from contextlib import contextmanager, suppress, redirect_stdout
import io


def demonstrate_with_statement():
    """with 문 기본"""
    print("=" * 50)
    print("1. with 문 기본")
    print("=" * 50)
    
    # 파일 열기 (자동 닫기)
    print("파일 작성 및 읽기:")
    
    # 쓰기
    with open('/tmp/test.txt', 'w') as f:
        f.write("Hello, World!\n")
        f.write("Python Context Manager")
    # with 블록을 벗어나면 자동으로 f.close() 호출
    
    # 읽기
    with open('/tmp/test.txt', 'r') as f:
        content = f.read()
        print(f"  내용:\n{content}")
    
    print()


def demonstrate_custom_context_manager():
    """커스텀 컨텍스트 매니저 (클래스)"""
    print("=" * 50)
    print("2. 커스텀 컨텍스트 매니저 (클래스)")
    print("=" * 50)
    
    class DatabaseConnection:
        def __init__(self, db_name):
            self.db_name = db_name
            self.connection = None
        
        def __enter__(self):
            print(f"  연결 시작: {self.db_name}")
            self.connection = f"Connection to {self.db_name}"
            return self.connection
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"  연결 종료: {self.db_name}")
            if exc_type:
                print(f"  예외 발생: {exc_type.__name__}: {exc_val}")
            return False  # 예외를 다시 발생시킴
    
    with DatabaseConnection("mydb") as conn:
        print(f"  사용 중: {conn}")
        # 작업 수행
    
    print()


def demonstrate_contextmanager_decorator():
    """@contextmanager 데코레이터"""
    print("=" * 50)
    print("3. @contextmanager 데코레이터")
    print("=" * 50)
    
    @contextmanager
    def temporary_value(obj, attr, value):
        """임시로 속성 값을 변경"""
        original = getattr(obj, attr)
        setattr(obj, attr, value)
        try:
            yield obj
        finally:
            setattr(obj, attr, original)
    
    class Config:
        debug = False
    
    config = Config()
    print(f"원래 debug: {config.debug}")
    
    with temporary_value(config, 'debug', True):
        print(f"임시 debug: {config.debug}")
    
    print(f"복원된 debug: {config.debug}")
    
    print()


def demonstrate_multiple_context_managers():
    """여러 컨텍스트 매니저"""
    print("=" * 50)
    print("4. 여러 컨텍스트 매니저")
    print("=" * 50)
    
    # 방법 1: 중첩
    print("중첩 방식:")
    with open('/tmp/input.txt', 'w') as infile:
        infile.write("Hello")
        with open('/tmp/output.txt', 'w') as outfile:
            outfile.write("World")
    print("  파일 두 개 처리 완료")
    
    # 방법 2: 한 줄에 (Python 2.7+)
    print("\n한 줄 방식:")
    with open('/tmp/input.txt', 'r') as infile, \
         open('/tmp/output.txt', 'r') as outfile:
        print(f"  input: {infile.read()}")
        print(f"  output: {outfile.read()}")
    
    print()


def demonstrate_suppress():
    """contextlib.suppress"""
    print("=" * 50)
    print("5. contextlib.suppress")
    print("=" * 50)
    
    # 예외 무시
    import os
    
    with suppress(FileNotFoundError):
        os.remove('/tmp/nonexistent.txt')
    print("  FileNotFoundError 무시됨")
    
    # 여러 예외 무시
    with suppress(ValueError, TypeError):
        int("not a number")
    print("  ValueError 무시됨")
    
    print()


def demonstrate_redirect_stdout():
    """contextlib.redirect_stdout"""
    print("=" * 50)
    print("6. contextlib.redirect_stdout")
    print("=" * 50)
    
    # stdout을 문자열 버퍼로 리다이렉트
    output = io.StringIO()
    
    with redirect_stdout(output):
        print("이 출력은 캡처됩니다")
        print("화면에 나타나지 않습니다")
    
    captured = output.getvalue()
    print(f"캡처된 출력:\n{captured}")
    
    print()


def demonstrate_timing_context_manager():
    """실행 시간 측정 컨텍스트 매니저"""
    print("=" * 50)
    print("7. 실행 시간 측정")
    print("=" * 50)
    
    import time
    
    @contextmanager
    def timer(name):
        start = time.perf_counter()
        yield
        end = time.perf_counter()
        print(f"  {name}: {end - start:.4f}초")
    
    with timer("작업 A"):
        time.sleep(0.1)
        sum(range(100000))
    
    with timer("작업 B"):
        time.sleep(0.05)
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 컨텍스트 매니저".center(50, "="))
    print()
    
    demonstrate_with_statement()
    demonstrate_custom_context_manager()
    demonstrate_contextmanager_decorator()
    demonstrate_multiple_context_managers()
    demonstrate_suppress()
    demonstrate_redirect_stdout()
    demonstrate_timing_context_manager()
    
    print("=" * 50)
    print("✅ 컨텍스트 매니저 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

