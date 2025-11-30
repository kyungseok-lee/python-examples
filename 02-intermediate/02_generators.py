"""
02. 제너레이터 (Generators)

yield를 사용한 제너레이터와 이터레이터를 학습합니다.
"""


def demonstrate_basic_generator():
    """기본 제너레이터"""
    print("=" * 50)
    print("1. 기본 제너레이터")
    print("=" * 50)
    
    def count_up_to(n):
        count = 1
        while count <= n:
            yield count
            count += 1
    
    print("제너레이터 함수 호출:")
    gen = count_up_to(5)
    print(f"  타입: {type(gen)}")
    
    print("\n값 생성:")
    for num in gen:
        print(f"  {num}")
    
    print()


def demonstrate_generator_vs_list():
    """제너레이터 vs 리스트"""
    print("=" * 50)
    print("2. 제너레이터 vs 리스트")
    print("=" * 50)
    
    import sys
    
    # 리스트
    list_comp = [x ** 2 for x in range(10000)]
    
    # 제너레이터
    gen_exp = (x ** 2 for x in range(10000))
    
    print(f"리스트 크기: {sys.getsizeof(list_comp):,} bytes")
    print(f"제너레이터 크기: {sys.getsizeof(gen_exp):,} bytes")
    print(f"메모리 효율: 약 {sys.getsizeof(list_comp) / sys.getsizeof(gen_exp):.0f}배")
    
    print()


def demonstrate_yield_examples():
    """yield 예제"""
    print("=" * 50)
    print("3. yield 예제")
    print("=" * 50)
    
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    print("피보나치 수열 (처음 10개):")
    for num in fibonacci(10):
        print(f"  {num}", end=" ")
    print("\n")
    
    # 파일 읽기 (청크 단위)
    def read_chunks(file_path, chunk_size=1024):
        """파일을 청크 단위로 읽기"""
        with open(file_path, 'r') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    
    print("파일 청크 읽기 예제 (시뮬레이션)")
    print("  (실제로는 큰 파일을 메모리 효율적으로 처리)")
    
    print()


def demonstrate_send_method():
    """send() 메서드"""
    print("=" * 50)
    print("4. send() 메서드")
    print("=" * 50)
    
    def echo_generator():
        value = None
        while True:
            value = yield value
            if value is not None:
                print(f"  받은 값: {value}")
    
    gen = echo_generator()
    next(gen)  # 제너레이터 초기화
    
    gen.send(10)
    gen.send(20)
    gen.send(30)
    
    print()


def demonstrate_generator_pipeline():
    """제너레이터 파이프라인"""
    print("=" * 50)
    print("5. 제너레이터 파이프라인")
    print("=" * 50)
    
    def numbers(n):
        for i in range(n):
            yield i
    
    def square(nums):
        for num in nums:
            yield num ** 2
    
    def add_one(nums):
        for num in nums:
            yield num + 1
    
    # 파이프라인 구성
    pipeline = add_one(square(numbers(10)))
    
    print("(n^2 + 1) for n in range(10):")
    for value in pipeline:
        print(f"  {value}", end=" ")
    print("\n")


def demonstrate_itertools_with_generators():
    """itertools + 제너레이터"""
    print("=" * 50)
    print("6. itertools + 제너레이터")
    print("=" * 50)
    
    import itertools
    
    def squares():
        n = 0
        while True:
            yield n ** 2
            n += 1
    
    # 처음 10개만 가져오기
    print("제곱수 (처음 10개):")
    for value in itertools.islice(squares(), 10):
        print(f"  {value}", end=" ")
    print("\n")
    
    # takewhile: 조건이 참인 동안만
    print("\n100 미만의 제곱수:")
    for value in itertools.takewhile(lambda x: x < 100, squares()):
        print(f"  {value}", end=" ")
    print("\n")


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 제너레이터".center(50, "="))
    print()
    
    demonstrate_basic_generator()
    demonstrate_generator_vs_list()
    demonstrate_yield_examples()
    demonstrate_send_method()
    demonstrate_generator_pipeline()
    demonstrate_itertools_with_generators()
    
    print("=" * 50)
    print("✅ 제너레이터 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

