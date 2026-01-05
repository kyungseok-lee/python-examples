#!/usr/bin/env python3
"""
02_class_vs_instance_vars.py - 클래스 변수 vs 인스턴스 변수 (🔴 치명적)

📌 핵심 개념:
   Python에서 클래스 본문에 선언된 변수는 "클래스 변수"로,
   모든 인스턴스가 공유합니다. 특히 가변 객체(list, dict)일 때 문제가 됩니다.

🔄 다른 언어 비교:
   - Java: 클래스 변수는 명시적으로 static 선언 필요
   - Kotlin: 클래스 변수는 companion object 안에 선언
   - Go: 패키지 레벨 변수와 struct 필드가 명확히 구분됨
   - Python: 클래스 본문의 변수가 자동으로 "공유"됨

⚠️ 주의사항:
   - 클래스 본문의 가변 객체는 거의 항상 버그!
   - Java의 static List와 비슷하지만 더 쉽게 실수함

📚 참고: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
"""

from __future__ import annotations


# =============================================================================
# 1️⃣ ❌ 문제가 있는 코드
# =============================================================================

class DogBad:
    """
    ❌ 잘못된 패턴: 클래스 레벨에 가변 객체 선언.
    
    Java 개발자가 흔히 하는 실수:
    "인스턴스 필드처럼 보이지만 실제로는 static 필드처럼 동작"
    """
    
    tricks: list[str] = []  # 모든 인스턴스가 공유!
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


def demonstrate_problem() -> None:
    """문제 상황 재현."""
    print("=" * 60)
    print("❌ 문제: 클래스 변수 공유")
    print("=" * 60)
    
    dog1 = DogBad("Buddy")
    dog2 = DogBad("Max")
    
    print(f"\n초기 상태:")
    print(f"dog1.tricks = {dog1.tricks}")
    print(f"dog2.tricks = {dog2.tricks}")
    
    dog1.add_trick("roll over")
    print(f"\ndog1.add_trick('roll over') 후:")
    print(f"dog1.tricks = {dog1.tricks}")
    print(f"dog2.tricks = {dog2.tricks}")  # dog2도 변경됨!
    
    dog2.add_trick("fetch")
    print(f"\ndog2.add_trick('fetch') 후:")
    print(f"dog1.tricks = {dog1.tricks}")  # dog1도 변경됨!
    print(f"dog2.tricks = {dog2.tricks}")
    
    print(f"\n같은 객체인가? {dog1.tricks is dog2.tricks}")  # True
    print(f"클래스 변수: DogBad.tricks = {DogBad.tricks}")


# =============================================================================
# 2️⃣ 왜 이런 일이 발생하는가?
# =============================================================================

def why_this_happens() -> None:
    """Python의 클래스 변수 동작 설명."""
    print("\n" + "=" * 60)
    print("📖 왜 이런 일이 발생하는가?")
    print("=" * 60)
    
    print("""
    Python 클래스 본문:
    
    class Dog:
        tricks = []     # 클래스 변수 (모든 인스턴스 공유)
        
        def __init__(self):
            self.name = "..."  # 인스턴스 변수 (개별 소유)
    
    💡 Java와 비교:
    
    // Java
    class Dog {
        List<String> tricks = new ArrayList<>();  // 인스턴스 필드
        static List<String> tricks = ...;         // 클래스 필드 (명시적 static)
    }
    
    Python에서는 클래스 본문의 변수가 Java의 static처럼 동작!
    단, 불변 객체(int, str)는 재할당 시 새 객체가 생기므로 괜찮음.
    가변 객체(list, dict, set)만 문제가 됨.
    """)


# =============================================================================
# 3️⃣ ✅ 올바른 해결 방법
# =============================================================================

class DogGood:
    """
    ✅ 올바른 패턴: __init__에서 인스턴스 변수로 선언.
    """
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks: list[str] = []  # 인스턴스 변수
    
    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


def demonstrate_solution() -> None:
    """올바른 해결책 시연."""
    print("\n" + "=" * 60)
    print("✅ 해결: __init__에서 인스턴스 변수로")
    print("=" * 60)
    
    dog1 = DogGood("Buddy")
    dog2 = DogGood("Max")
    
    dog1.add_trick("roll over")
    dog2.add_trick("fetch")
    
    print(f"dog1.tricks = {dog1.tricks}")  # ['roll over']
    print(f"dog2.tricks = {dog2.tricks}")  # ['fetch']
    print(f"같은 객체? {dog1.tricks is dog2.tricks}")  # False


# =============================================================================
# 4️⃣ 불변 vs 가변 객체의 차이
# =============================================================================

class Counter:
    """불변 객체(int)는 괜찮은 예시."""
    
    count: int = 0  # 클래스 변수지만...
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def increment(self) -> None:
        # 재할당하면 새 객체가 self.count에 바인딩됨
        self.count += 1  # self.count = self.count + 1


def demonstrate_immutable() -> None:
    """불변 객체의 동작."""
    print("\n" + "=" * 60)
    print("📌 불변 객체(int)는 다르게 동작")
    print("=" * 60)
    
    c1 = Counter("A")
    c2 = Counter("B")
    
    c1.increment()
    c1.increment()
    c2.increment()
    
    print(f"c1.count = {c1.count}")  # 2
    print(f"c2.count = {c2.count}")  # 1
    print(f"Counter.count = {Counter.count}")  # 0 (클래스 변수는 변경 안됨)
    
    print("""
    💡 설명:
    c1.count += 1 은 실제로 c1.count = c1.count + 1
    
    1. c1.count를 읽으면 → 클래스 변수 Counter.count(0)를 찾음
    2. 0 + 1 = 1
    3. c1.count = 1 → 새로운 인스턴스 변수 생성!
    
    결과적으로 c1과 c2는 각자의 인스턴스 변수를 갖게 됨.
    하지만 이는 "우연히" 동작하는 것이므로 권장하지 않음!
    """)


# =============================================================================
# 5️⃣ dataclass 사용 (권장)
# =============================================================================

from dataclasses import dataclass, field


@dataclass
class DogDataclass:
    """
    ✅ 가장 권장하는 패턴: dataclass + field(default_factory).
    
    Kotlin의 data class와 유사.
    """
    
    name: str
    tricks: list[str] = field(default_factory=list)  # 매 인스턴스마다 새 리스트
    
    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


def demonstrate_dataclass() -> None:
    """dataclass 사용 예시."""
    print("\n" + "=" * 60)
    print("✅ 최선: dataclass + field(default_factory)")
    print("=" * 60)
    
    dog1 = DogDataclass("Buddy")
    dog2 = DogDataclass("Max")
    
    dog1.add_trick("roll over")
    dog2.add_trick("fetch")
    
    print(f"dog1 = {dog1}")
    print(f"dog2 = {dog2}")
    print(f"같은 tricks? {dog1.tricks is dog2.tricks}")  # False


# =============================================================================
# 6️⃣ 클래스 변수의 올바른 사용처
# =============================================================================

class Config:
    """
    ✅ 클래스 변수의 올바른 사용: 상수, 불변 설정.
    """
    
    # 상수 (대문자)
    MAX_CONNECTIONS: int = 100
    DEFAULT_TIMEOUT: float = 30.0
    SUPPORTED_FORMATS: tuple[str, ...] = ("json", "xml", "csv")  # 불변 tuple
    
    def __init__(self, timeout: float | None = None) -> None:
        self.timeout = timeout or self.DEFAULT_TIMEOUT


def demonstrate_proper_class_vars() -> None:
    """클래스 변수의 올바른 사용."""
    print("\n" + "=" * 60)
    print("📌 클래스 변수의 올바른 사용")
    print("=" * 60)
    
    print(f"Config.MAX_CONNECTIONS = {Config.MAX_CONNECTIONS}")
    print(f"Config.SUPPORTED_FORMATS = {Config.SUPPORTED_FORMATS}")
    
    c1 = Config()
    c2 = Config(timeout=60.0)
    
    print(f"c1.timeout = {c1.timeout}")
    print(f"c2.timeout = {c2.timeout}")
    
    print("""
    💡 클래스 변수 사용 가이드:
    ✅ 상수 (불변): int, float, str, tuple, frozenset
    ✅ 클래스 메타데이터
    ❌ 가변 객체: list, dict, set → 반드시 __init__에서!
    """)


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    demonstrate_problem()
    why_this_happens()
    demonstrate_solution()
    demonstrate_immutable()
    demonstrate_dataclass()
    demonstrate_proper_class_vars()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    ❌ 하지 말 것:
       class Foo:
           items = []  # 모든 인스턴스가 공유!
    
    ✅ 해야 할 것:
       class Foo:
           def __init__(self):
               self.items = []  # 인스턴스마다 개별 소유
    
    ✅✅ 최선 (dataclass):
       @dataclass
       class Foo:
           items: list = field(default_factory=list)
    
    🔍 린터 설정:
       - pylint: class-variable-slots-conflict
    """)


if __name__ == "__main__":
    main()

