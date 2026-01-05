#!/usr/bin/env python3
"""
02_quick_tour.py - Python 핵심 기능 5분 투어

📌 핵심 개념:
   Python만의 강력한 기능들을 빠르게 체험

🔄 다른 언어에 없는 Python 특징:
   - 리스트/딕셔너리 컴프리헨션
   - 제너레이터와 yield
   - 컨텍스트 매니저 (with)
   - 데코레이터 (@)
   - 언패킹 (*args, **kwargs)

⚠️ 주의사항:
   - 이 기능들은 Python에서 매우 자주 사용됨
   - 다른 언어 습관으로 작성하면 "Pythonic하지 않다"는 리뷰를 받음

📚 참고: https://docs.python.org/3/tutorial/
"""

from __future__ import annotations

import contextlib
import functools
import time
from typing import Any, Callable, Generator


# =============================================================================
# 1️⃣ 리스트 컴프리헨션 - Python의 가장 강력한 기능
# =============================================================================

def comprehensions_tour() -> None:
    """
    컴프리헨션 (Comprehension) - Python의 킬러 기능.
    
    💡 Java 개발자를 위한 팁:
        - Stream API의 map, filter를 한 줄로
        - 훨씬 빠르고 가독성 좋음 (Python 관용구)
    
    💡 Go 개발자를 위한 팁:
        - Go에서는 for loop 필수
        - Python에서 for loop 쓰면 "Pythonic하지 않다"는 피드백 받음
    """
    print("\n📌 리스트 컴프리헨션")
    print("-" * 50)
    
    # 기본: [표현식 for 변수 in 이터러블]
    numbers = [1, 2, 3, 4, 5]
    
    # Java: numbers.stream().map(x -> x * 2).collect(Collectors.toList())
    # Go:   for _, n := range numbers { result = append(result, n*2) }
    # Python:
    doubled = [x * 2 for x in numbers]
    print(f"Doubled: {doubled}")
    
    # 필터링: [표현식 for 변수 in 이터러블 if 조건]
    # Java: numbers.stream().filter(x -> x % 2 == 0).collect(...)
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Evens: {evens}")
    
    # 조건 표현식 포함
    labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print(f"Labels: {labels}")
    
    # 딕셔너리 컴프리헨션
    squares = {x: x**2 for x in range(5)}
    print(f"Squares dict: {squares}")
    
    # 셋 컴프리헨션
    unique_mods = {x % 3 for x in range(10)}
    print(f"Unique mods: {unique_mods}")
    
    # 중첩 컴프리헨션 (2D 리스트 평탄화)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened: {flattened}")


# =============================================================================
# 2️⃣ 제너레이터 - 메모리 효율적인 이터레이션
# =============================================================================

def generators_tour() -> None:
    """
    제너레이터 (Generator) - 지연 평가와 메모리 효율.
    
    💡 Java 개발자를 위한 팁:
        - Stream의 lazy evaluation과 유사
        - 하지만 훨씬 더 직관적인 문법
    
    💡 Go 개발자를 위한 팁:
        - Go의 channel과 비슷한 개념
        - yield가 데이터를 하나씩 반환
    """
    print("\n📌 제너레이터")
    print("-" * 50)
    
    # 제너레이터 표현식 (리스트 컴프리헨션과 비슷하지만 () 사용)
    # 리스트: 모든 값을 메모리에 저장
    # 제너레이터: 필요할 때마다 값 생성
    list_comp = [x**2 for x in range(1000)]
    gen_exp = (x**2 for x in range(1000))
    
    import sys
    print(f"List size: {sys.getsizeof(list_comp):,} bytes")
    print(f"Generator size: {sys.getsizeof(gen_exp):,} bytes")
    
    # 제너레이터 함수 (yield 사용)
    def countdown(n: int) -> Generator[int, None, None]:
        """yield로 값을 하나씩 반환."""
        while n > 0:
            yield n  # return과 달리 함수가 일시 정지
            n -= 1
    
    print("\nCountdown:")
    for num in countdown(5):
        print(f"  {num}", end=" ")
    print()
    
    # 무한 시퀀스도 가능!
    def infinite_counter() -> Generator[int, None, None]:
        n = 0
        while True:
            yield n
            n += 1
    
    print("\nInfinite counter (first 5):")
    counter = infinite_counter()
    for _ in range(5):
        print(f"  {next(counter)}", end=" ")
    print()


# =============================================================================
# 3️⃣ 컨텍스트 매니저 - 리소스 자동 관리
# =============================================================================

def context_managers_tour() -> None:
    """
    컨텍스트 매니저 (Context Manager) - with문으로 리소스 관리.
    
    💡 Java 개발자를 위한 팁:
        - try-with-resources와 유사
        - 하지만 더 유연하고 직접 만들기 쉬움
    
    💡 Go 개발자를 위한 팁:
        - defer와 비슷하지만 더 구조적
        - 에러 처리와 cleanup을 깔끔하게
    """
    print("\n📌 컨텍스트 매니저 (with)")
    print("-" * 50)
    
    # 파일 처리 - 자동으로 close() 호출
    # Java: try (BufferedReader reader = new BufferedReader(...)) { ... }
    # Go:   defer file.Close()
    # Python:
    print("File handling with 'with':")
    
    # 시뮬레이션 (실제 파일 없이)
    class FakeFile:
        def __init__(self, name: str) -> None:
            self.name = name
        def __enter__(self) -> "FakeFile":
            print(f"  Opening {self.name}")
            return self
        def __exit__(self, *args: Any) -> None:
            print(f"  Closing {self.name}")
        def read(self) -> str:
            return "file content"
    
    with FakeFile("data.txt") as f:
        content = f.read()
        print(f"  Content: {content}")
    print("  (파일이 자동으로 닫힘)")
    
    # contextlib으로 간단하게 만들기
    @contextlib.contextmanager
    def timer(label: str) -> Generator[None, None, None]:
        """실행 시간 측정 컨텍스트 매니저."""
        start = time.perf_counter()
        print(f"\n  [{label}] 시작")
        yield  # 여기서 with 블록 실행
        end = time.perf_counter()
        print(f"  [{label}] 완료: {end - start:.4f}초")
    
    with timer("작업"):
        # 실제 작업
        total = sum(range(100000))
        print(f"  계산 결과: {total}")


# =============================================================================
# 4️⃣ 데코레이터 - 함수 확장의 강력한 도구
# =============================================================================

def decorators_tour() -> None:
    """
    데코레이터 (Decorator) - 함수/클래스 확장.
    
    💡 Java 개발자를 위한 팁:
        - AOP (Aspect-Oriented Programming)와 유사
        - 애노테이션(@)처럼 생겼지만 실제로 함수를 감싸는 것
    
    💡 Go 개발자를 위한 팁:
        - Go에서는 미들웨어 패턴으로 구현
        - Python은 언어 차원에서 지원
    """
    print("\n📌 데코레이터")
    print("-" * 50)
    
    # 간단한 데코레이터
    def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
        """함수 호출을 로깅하는 데코레이터."""
        @functools.wraps(func)  # 원본 함수 메타데이터 보존
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"  ➡️ Calling {func.__name__}{args}")
            result = func(*args, **kwargs)
            print(f"  ⬅️ {func.__name__} returned {result}")
            return result
        return wrapper
    
    @log_calls
    def add(a: int, b: int) -> int:
        return a + b
    
    result = add(10, 20)
    
    # 인자가 있는 데코레이터
    def repeat(times: int) -> Callable:
        """함수를 여러 번 실행하는 데코레이터."""
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(times=3)
    def say_hello() -> str:
        print("  Hello!")
        return "done"
    
    print("\n@repeat(times=3):")
    say_hello()
    
    # 실무에서 자주 사용: 캐싱
    @functools.lru_cache(maxsize=128)
    def fibonacci(n: int) -> int:
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"\nfibonacci(30) with cache: {fibonacci(30)}")
    print(f"Cache info: {fibonacci.cache_info()}")


# =============================================================================
# 5️⃣ 언패킹 - 우아한 데이터 추출
# =============================================================================

def unpacking_tour() -> None:
    """
    언패킹 (Unpacking) - 데이터 추출의 예술.
    
    💡 다른 언어 개발자를 위한 팁:
        - JavaScript의 destructuring과 유사
        - Java/Go에는 이런 문법 없음 (부러워할 기능!)
    """
    print("\n📌 언패킹")
    print("-" * 50)
    
    # 튜플 언패킹
    point = (10, 20, 30)
    x, y, z = point
    print(f"Tuple unpacking: x={x}, y={y}, z={z}")
    
    # 스왑 (임시 변수 불필요!)
    a, b = 1, 2
    a, b = b, a  # Java/Go에서는 temp 변수 필요
    print(f"Swap: a={a}, b={b}")
    
    # * 연산자로 나머지 캡처
    first, *rest = [1, 2, 3, 4, 5]
    print(f"First and rest: first={first}, rest={rest}")
    
    head, *middle, tail = [1, 2, 3, 4, 5]
    print(f"Head, middle, tail: {head}, {middle}, {tail}")
    
    # 딕셔너리 언패킹 (**)
    defaults = {"host": "localhost", "port": 8080}
    custom = {"port": 3000, "debug": True}
    config = {**defaults, **custom}  # 병합 (뒤가 우선)
    print(f"Merged config: {config}")
    
    # 함수 인자 언패킹
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"
    
    kwargs = {"name": "Alice", "greeting": "Hi"}
    print(f"Function call with **: {greet(**kwargs)}")
    
    # *args, **kwargs
    def flexible_func(*args: Any, **kwargs: Any) -> None:
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
    
    print("\nflexible_func(1, 2, 3, x=10, y=20):")
    flexible_func(1, 2, 3, x=10, y=20)


# =============================================================================
# 6️⃣ 덕 타이핑 - Python의 철학
# =============================================================================

def duck_typing_tour() -> None:
    """
    덕 타이핑 (Duck Typing) - "오리처럼 걷고 꽥꽥거리면 오리다".
    
    💡 Java/Kotlin 개발자를 위한 팁:
        - 인터페이스 구현 선언 불필요
        - 메서드만 있으면 동작
    
    💡 Go 개발자를 위한 팁:
        - Go의 암묵적 인터페이스와 유사
        - 하지만 런타임에 체크
    """
    print("\n📌 덕 타이핑")
    print("-" * 50)
    
    # 인터페이스 선언 없이 동작
    class Dog:
        def speak(self) -> str:
            return "Woof!"
    
    class Cat:
        def speak(self) -> str:
            return "Meow!"
    
    class Robot:
        def speak(self) -> str:
            return "Beep boop!"
    
    # 어떤 타입이든 speak() 메서드만 있으면 동작
    def make_speak(animal: Any) -> None:
        print(f"  {type(animal).__name__} says: {animal.speak()}")
    
    animals = [Dog(), Cat(), Robot()]
    for animal in animals:
        make_speak(animal)
    
    # Python 3.8+: Protocol로 타입 힌트와 덕 타이핑 결합
    from typing import Protocol
    
    class Speakable(Protocol):
        def speak(self) -> str: ...
    
    def make_speak_typed(animal: Speakable) -> None:
        """타입 체커가 speak() 메서드 확인."""
        print(f"  {animal.speak()}")
    
    print("\nWith Protocol (타입 힌트):")
    make_speak_typed(Dog())  # 타입 체커 통과!


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    print("=" * 60)
    print("🚀 Python 핵심 기능 5분 투어")
    print("=" * 60)
    
    comprehensions_tour()
    generators_tour()
    context_managers_tour()
    decorators_tour()
    unpacking_tour()
    duck_typing_tour()
    
    print("\n" + "=" * 60)
    print("✅ Python 핵심 기능 투어 완료!")
    print("=" * 60)
    print("\n💡 핵심 정리:")
    print("  1. 컴프리헨션으로 for loop 대체 (더 Pythonic)")
    print("  2. 제너레이터로 메모리 효율적 처리")
    print("  3. with문으로 리소스 자동 관리")
    print("  4. 데코레이터로 함수 확장 (AOP)")
    print("  5. 언패킹으로 우아한 데이터 처리")
    print("  6. 덕 타이핑으로 유연한 다형성")


if __name__ == "__main__":
    main()

