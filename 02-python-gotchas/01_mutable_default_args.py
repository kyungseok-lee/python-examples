#!/usr/bin/env python3
"""
01_mutable_default_args.py - 가변 기본 인자 함정 (🔴 치명적)

📌 핵심 개념:
   Python에서 함수의 기본 인자는 함수 정의 시점에 "한 번만" 평가됩니다.
   가변 객체(list, dict, set)를 기본 인자로 사용하면 모든 호출이 같은 객체를 공유합니다.

🔄 다른 언어 비교:
   - Java: 매 호출마다 새로운 객체가 생성됨 (이 문제 없음)
   - Go: 기본 인자 자체가 없음 (이 문제 없음)
   - Kotlin: Java와 동일, 안전함

⚠️ 주의사항:
   - def func(items=[]) 패턴은 거의 항상 버그!
   - 코드 리뷰에서 가장 흔히 지적되는 문제 중 하나

📚 참고: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
"""

from __future__ import annotations


# =============================================================================
# 1️⃣ ❌ 문제가 있는 코드
# =============================================================================

def append_to_bad(item: int, items: list[int] = []) -> list[int]:
    """
    ❌ 잘못된 패턴: 가변 객체를 기본 인자로 사용.
    
    이 함수는 매 호출마다 새 리스트를 반환할 것처럼 보이지만,
    실제로는 모든 호출이 같은 리스트를 공유합니다!
    """
    items.append(item)
    return items


def demonstrate_problem() -> None:
    """문제 상황 재현."""
    print("=" * 60)
    print("❌ 문제: 가변 기본 인자")
    print("=" * 60)
    
    print("\n# 기대: 각 호출이 독립적인 리스트 반환")
    print("# 실제: 모든 호출이 같은 리스트 공유!")
    
    result1 = append_to_bad(1)
    print(f"append_to_bad(1) = {result1}")  # [1]
    
    result2 = append_to_bad(2)
    print(f"append_to_bad(2) = {result2}")  # 예상: [2], 실제: [1, 2]
    
    result3 = append_to_bad(3)
    print(f"append_to_bad(3) = {result3}")  # 예상: [3], 실제: [1, 2, 3]
    
    print(f"\n모두 같은 객체: {result1 is result2 is result3}")  # True!
    print(f"id(result1) = {id(result1)}")
    print(f"id(result2) = {id(result2)}")
    print(f"id(result3) = {id(result3)}")
    
    # 함수의 기본값 확인
    print(f"\n함수의 __defaults__: {append_to_bad.__defaults__}")


# =============================================================================
# 2️⃣ 왜 이런 일이 발생하는가?
# =============================================================================

def why_this_happens() -> None:
    """Python의 함수 정의 동작 설명."""
    print("\n" + "=" * 60)
    print("📖 왜 이런 일이 발생하는가?")
    print("=" * 60)
    
    print("""
    Python에서 함수는 "객체"입니다.
    함수가 정의될 때(def 실행 시) 기본 인자가 평가되어
    함수 객체의 __defaults__ 속성에 저장됩니다.
    
    def func(items=[]):  # 여기서 [] 가 생성됨 (한 번만!)
        items.append(...)
        return items
    
    💡 Java/Go와의 차이:
    - Java: void func(List<Integer> items) 에서 items=null이면
            매 호출마다 new ArrayList<>() 생성
    - Go: 기본 인자 없음, 항상 명시적 전달
    - Python: def 실행 시점에 기본값 평가 후 재사용
    """)


# =============================================================================
# 3️⃣ ✅ 올바른 해결 방법
# =============================================================================

def append_to_good(item: int, items: list[int] | None = None) -> list[int]:
    """
    ✅ 올바른 패턴: None을 기본값으로 사용.
    
    매 호출마다 새 리스트를 생성합니다.
    """
    if items is None:
        items = []  # 함수 호출 시마다 새 리스트 생성
    items.append(item)
    return items


def demonstrate_solution() -> None:
    """올바른 해결책 시연."""
    print("\n" + "=" * 60)
    print("✅ 해결: None 기본값 패턴")
    print("=" * 60)
    
    result1 = append_to_good(1)
    print(f"append_to_good(1) = {result1}")  # [1]
    
    result2 = append_to_good(2)
    print(f"append_to_good(2) = {result2}")  # [2]
    
    result3 = append_to_good(3)
    print(f"append_to_good(3) = {result3}")  # [3]
    
    print(f"\n각각 다른 객체: {result1 is not result2 is not result3}")
    print(f"id(result1) = {id(result1)}")
    print(f"id(result2) = {id(result2)}")
    print(f"id(result3) = {id(result3)}")


# =============================================================================
# 4️⃣ 실무에서 자주 발생하는 케이스
# =============================================================================

class UserService:
    """❌ 클래스에서도 같은 문제 발생."""
    
    def __init__(self, roles: list[str] = []) -> None:  # noqa: B006
        """모든 인스턴스가 같은 roles 리스트 공유!"""
        self.roles = roles
    
    def add_role(self, role: str) -> None:
        self.roles.append(role)


class UserServiceFixed:
    """✅ 올바른 패턴."""
    
    def __init__(self, roles: list[str] | None = None) -> None:
        self.roles = roles if roles is not None else []
    
    def add_role(self, role: str) -> None:
        self.roles.append(role)


def demonstrate_class_case() -> None:
    """클래스에서의 문제 시연."""
    print("\n" + "=" * 60)
    print("📦 클래스에서도 같은 문제 발생")
    print("=" * 60)
    
    print("\n❌ 잘못된 클래스:")
    user1 = UserService()
    user2 = UserService()
    user1.add_role("admin")
    print(f"user1.roles = {user1.roles}")
    print(f"user2.roles = {user2.roles}")  # user2도 admin이 들어감!
    print(f"같은 리스트? {user1.roles is user2.roles}")
    
    print("\n✅ 올바른 클래스:")
    fixed1 = UserServiceFixed()
    fixed2 = UserServiceFixed()
    fixed1.add_role("admin")
    print(f"fixed1.roles = {fixed1.roles}")
    print(f"fixed2.roles = {fixed2.roles}")  # 빈 리스트
    print(f"같은 리스트? {fixed1.roles is fixed2.roles}")


# =============================================================================
# 5️⃣ dict와 set도 마찬가지
# =============================================================================

def create_config_bad(overrides: dict[str, str] = {}) -> dict[str, str]:  # noqa: B006
    """❌ dict도 같은 문제."""
    defaults = {"host": "localhost", "port": "8080"}
    defaults.update(overrides)
    return defaults


def create_config_good(overrides: dict[str, str] | None = None) -> dict[str, str]:
    """✅ 올바른 패턴."""
    defaults = {"host": "localhost", "port": "8080"}
    if overrides:
        defaults.update(overrides)
    return defaults


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    demonstrate_problem()
    why_this_happens()
    demonstrate_solution()
    demonstrate_class_case()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    ❌ 하지 말 것:
       def func(items=[]):
       def func(config={}):
       def __init__(self, data=[]):
    
    ✅ 해야 할 것:
       def func(items: list | None = None):
           if items is None:
               items = []
    
    🔍 린터 설정:
       - flake8-bugbear: B006 규칙이 이 패턴을 감지
       - pylint: dangerous-default-value 규칙
    """)


if __name__ == "__main__":
    main()

