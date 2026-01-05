"""
04. 데이터클래스 (Dataclasses)

@dataclass 데코레이터를 사용한 데이터 클래스를 학습합니다.

Python 3.10+: slots=True 옵션
Python 3.10+: match_args, kw_only 옵션
"""

from __future__ import annotations

from dataclasses import asdict, astuple, dataclass, field, replace
from typing import ClassVar


def demonstrate_basic_dataclass() -> None:
    """기본 데이터클래스"""
    print("=" * 50)
    print("1. 기본 데이터클래스")
    print("=" * 50)

    @dataclass
    class Person:
        name: str
        age: int
        city: str = "Seoul"  # 기본값

    person = Person("Alice", 25)
    print(f"  {person}")
    print(f"  이름: {person.name}, 나이: {person.age}")
    print()


def demonstrate_dataclass_features() -> None:
    """데이터클래스 기능"""
    print("=" * 50)
    print("2. 데이터클래스 옵션")
    print("=" * 50)

    @dataclass(frozen=True)  # 불변
    class Point:
        x: int
        y: int

    @dataclass(order=True)  # 비교 가능
    class Person:
        name: str
        age: int

    point = Point(10, 20)
    print(f"  포인트: {point}")

    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    print(f"  {person1.name} < {person2.name}: {person1 < person2}")
    print()


def demonstrate_slots() -> None:
    """slots 옵션 (메모리 최적화)"""
    print("=" * 50)
    print("3. slots 옵션 (메모리 최적화)")
    print("=" * 50)

    import sys

    # slots 없음 (기본)
    @dataclass
    class PersonWithDict:
        name: str
        age: int

    # slots 사용 (Python 3.10+)
    @dataclass(slots=True)
    class PersonWithSlots:
        name: str
        age: int

    p_dict = PersonWithDict("Alice", 25)
    p_slots = PersonWithSlots("Bob", 30)

    # __dict__ vs __slots__
    print(f"  PersonWithDict has __dict__: {hasattr(p_dict, '__dict__')}")
    print(f"  PersonWithSlots has __dict__: {hasattr(p_slots, '__dict__')}")
    print(f"  PersonWithSlots has __slots__: {hasattr(p_slots, '__slots__')}")

    # 메모리 비교
    size_dict = sys.getsizeof(p_dict) + sys.getsizeof(p_dict.__dict__)
    size_slots = sys.getsizeof(p_slots)
    print(f"\n  PersonWithDict 크기: ~{size_dict} bytes")
    print(f"  PersonWithSlots 크기: ~{size_slots} bytes")
    print(f"  절약: ~{size_dict - size_slots} bytes/객체")
    print()


def demonstrate_field() -> None:
    """field() 함수"""
    print("=" * 50)
    print("4. field() 함수")
    print("=" * 50)

    @dataclass(slots=True)
    class User:
        name: str
        age: int
        skills: list[str] = field(default_factory=list)
        _internal: int = field(default=0, repr=False)  # repr에서 제외
        created: str = field(default="", compare=False)  # 비교에서 제외

        # 클래스 변수 (인스턴스 변수 아님)
        total_users: ClassVar[int] = 0

        def __post_init__(self) -> None:
            User.total_users += 1

    user = User("Alice", 25, ["Python", "Go"])
    print(f"  {user}")
    print(f"  딕셔너리: {asdict(user)}")
    print(f"  튜플: {astuple(user)}")
    print()


def demonstrate_inheritance() -> None:
    """데이터클래스 상속"""
    print("=" * 50)
    print("5. 데이터클래스 상속")
    print("=" * 50)

    @dataclass
    class Animal:
        name: str
        age: int

    @dataclass
    class Dog(Animal):
        breed: str

    dog = Dog("Buddy", 3, "Labrador")
    print(f"  {dog}")
    print()


def demonstrate_kw_only() -> None:
    """kw_only 옵션 (Python 3.10+)"""
    print("=" * 50)
    print("6. kw_only 옵션")
    print("=" * 50)

    @dataclass(kw_only=True, slots=True)
    class Config:
        host: str
        port: int = 8080
        debug: bool = False

    # 키워드 인자만 허용
    config = Config(host="localhost", debug=True)
    print(f"  {config}")

    # 특정 필드만 kw_only
    @dataclass(slots=True)
    class Server:
        name: str  # 위치 인자 가능
        host: str = field(kw_only=True, default="localhost")
        port: int = field(kw_only=True, default=8080)

    server = Server("main", host="0.0.0.0", port=9000)
    print(f"  {server}")
    print()


def demonstrate_replace() -> None:
    """replace 함수 (불변 업데이트)"""
    print("=" * 50)
    print("7. replace 함수")
    print("=" * 50)

    @dataclass(frozen=True, slots=True)
    class Point:
        x: int
        y: int

    p1 = Point(1, 2)
    p2 = replace(p1, x=10)  # x만 변경한 새 객체

    print(f"  원본: {p1}")
    print(f"  변경: {p2}")
    print(f"  같은 객체? {p1 is p2}")
    print()


def demonstrate_gc_optimization() -> None:
    """GC 최적화 관점"""
    print("=" * 50)
    print("8. GC 최적화 관점")
    print("=" * 50)

    import gc
    import time

    @dataclass
    class RegularUser:
        name: str
        age: int
        email: str

    @dataclass(slots=True)
    class OptimizedUser:
        name: str
        age: int
        email: str

    n = 10000

    # Regular (with __dict__)
    gc.disable()
    start = time.perf_counter()
    regular_users = [RegularUser(f"user{i}", i % 100, f"u{i}@x.com") for i in range(n)]
    regular_time = time.perf_counter() - start
    gc.enable()

    # Optimized (with __slots__)
    gc.disable()
    start = time.perf_counter()
    optimized_users = [OptimizedUser(f"user{i}", i % 100, f"u{i}@x.com") for i in range(n)]
    optimized_time = time.perf_counter() - start
    gc.enable()

    print(f"  Regular 생성 ({n}개): {regular_time:.4f}초")
    print(f"  Optimized 생성 ({n}개): {optimized_time:.4f}초")
    print(f"  성능 향상: {regular_time / optimized_time:.2f}x")

    # 메모리 정리
    del regular_users, optimized_users
    gc.collect()

    print()


def main() -> None:
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 데이터클래스".center(50, "="))
    print()

    demonstrate_basic_dataclass()
    demonstrate_dataclass_features()
    demonstrate_slots()
    demonstrate_field()
    demonstrate_inheritance()
    demonstrate_kw_only()
    demonstrate_replace()
    demonstrate_gc_optimization()

    print("=" * 50)
    print("✅ 데이터클래스 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()
