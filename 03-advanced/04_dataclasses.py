"""
04. 데이터클래스 (Dataclasses)

@dataclass 데코레이터를 사용한 데이터 클래스를 학습합니다.
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List


def demonstrate_basic_dataclass():
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


def demonstrate_dataclass_features():
    """데이터클래스 기능"""
    print("=" * 50)
    print("2. 데이터클래스 기능")
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


def demonstrate_field():
    """field() 함수"""
    print("=" * 50)
    print("3. field() 함수")
    print("=" * 50)
    
    @dataclass
    class User:
        name: str
        age: int
        skills: List[str] = field(default_factory=list)
        _internal: int = field(default=0, repr=False)  # repr에서 제외
    
    user = User("Alice", 25, ["Python", "Go"])
    print(f"  {user}")
    print(f"  딕셔너리: {asdict(user)}")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 데이터클래스".center(50, "="))
    print()
    
    demonstrate_basic_dataclass()
    demonstrate_dataclass_features()
    demonstrate_field()
    
    print("=" * 50)
    print("✅ 데이터클래스 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

