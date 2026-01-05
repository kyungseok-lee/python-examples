#!/usr/bin/env python3
"""
05_shallow_vs_deep_copy.py - 얕은 복사 vs 깊은 복사 (🟡 주의)

📌 핵심 개념:
   Python에서 객체를 복사할 때 "얕은 복사"가 기본입니다.
   중첩된 객체(리스트 안의 리스트)는 참조가 복사되어 원본과 공유됩니다.

🔄 다른 언어 비교:
   - Java: clone()이 얕은 복사, 깊은 복사는 직접 구현 필요
   - Go: 슬라이스 복사가 얕은 복사 (Python과 유사)
   - Kotlin: copy()가 얕은 복사 (data class)

⚠️ 주의사항:
   - 리스트 슬라이싱 [:]은 얕은 복사
   - list(), dict() 생성자도 얕은 복사
   - 중첩 구조는 copy.deepcopy() 필요

📚 참고: https://docs.python.org/3/library/copy.html
"""

from __future__ import annotations

import copy


# =============================================================================
# 1️⃣ 기본 개념: 할당 vs 복사
# =============================================================================

def assignment_vs_copy() -> None:
    """할당과 복사의 차이."""
    print("=" * 60)
    print("📌 할당 vs 복사")
    print("=" * 60)
    
    # 할당: 같은 객체를 참조
    original = [1, 2, 3]
    assigned = original  # 같은 객체!
    
    print(f"original = {original}, id = {id(original)}")
    print(f"assigned = original, id = {id(assigned)}")
    print(f"같은 객체? {original is assigned}")  # True
    
    assigned.append(4)
    print(f"\nassigned.append(4) 후:")
    print(f"original = {original}")  # [1, 2, 3, 4] - 원본도 변경!
    print(f"assigned = {assigned}")
    
    # 복사: 새 객체 생성
    original2 = [1, 2, 3]
    copied = original2.copy()  # 또는 list(original2) 또는 original2[:]
    
    print(f"\n원본: {original2}, id = {id(original2)}")
    print(f"복사본: {copied}, id = {id(copied)}")
    print(f"같은 객체? {original2 is copied}")  # False
    
    copied.append(4)
    print(f"\ncopied.append(4) 후:")
    print(f"original2 = {original2}")  # [1, 2, 3] - 원본 유지!
    print(f"copied = {copied}")  # [1, 2, 3, 4]


# =============================================================================
# 2️⃣ ⚠️ 얕은 복사의 함정
# =============================================================================

def shallow_copy_gotcha() -> None:
    """얕은 복사의 함정: 중첩 객체."""
    print("\n" + "=" * 60)
    print("⚠️ 얕은 복사의 함정: 중첩 객체")
    print("=" * 60)
    
    # 중첩 리스트
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 얕은 복사 방법들 (모두 동일한 결과)
    shallow1 = matrix.copy()
    shallow2 = list(matrix)
    shallow3 = matrix[:]
    
    print(f"original: {matrix}")
    print(f"shallow copy: {shallow1}")
    print(f"같은 외부 리스트? {matrix is shallow1}")  # False
    print(f"같은 내부 리스트? {matrix[0] is shallow1[0]}")  # True!
    
    # 내부 리스트 수정
    shallow1[0][0] = 999
    
    print(f"\nshallow1[0][0] = 999 후:")
    print(f"original: {matrix}")   # [[999, 2, 3], ...] - 원본도 변경!
    print(f"shallow: {shallow1}")
    
    print("""
    💡 얕은 복사의 동작:
    
    original  ──►  [ ●, ●, ● ]
                    │  │  │
                    ▼  ▼  ▼
                 [1,2,3] [4,5,6] [7,8,9]
                    ▲  ▲  ▲
                    │  │  │
    shallow   ──►  [ ●, ●, ● ]
    
    외부 리스트는 새로 생성되지만,
    내부 리스트들은 참조가 복사됨!
    """)


# =============================================================================
# 3️⃣ ✅ 깊은 복사로 해결
# =============================================================================

def deep_copy_solution() -> None:
    """깊은 복사로 완전한 복사."""
    print("\n" + "=" * 60)
    print("✅ 깊은 복사: copy.deepcopy()")
    print("=" * 60)
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    deep = copy.deepcopy(matrix)
    
    print(f"original: {matrix}")
    print(f"deep copy: {deep}")
    print(f"같은 외부 리스트? {matrix is deep}")  # False
    print(f"같은 내부 리스트? {matrix[0] is deep[0]}")  # False!
    
    # 내부 리스트 수정
    deep[0][0] = 999
    
    print(f"\ndeep[0][0] = 999 후:")
    print(f"original: {matrix}")  # [[1, 2, 3], ...] - 원본 유지!
    print(f"deep: {deep}")
    
    print("""
    💡 깊은 복사의 동작:
    
    original  ──►  [ ●, ●, ● ]
                    │  │  │
                    ▼  ▼  ▼
                 [1,2,3] [4,5,6] [7,8,9]
    
    deep      ──►  [ ●, ●, ● ]
                    │  │  │
                    ▼  ▼  ▼
                 [1,2,3] [4,5,6] [7,8,9]  (새로 생성된 객체들)
    
    모든 중첩 객체가 재귀적으로 복사됨!
    """)


# =============================================================================
# 4️⃣ 딕셔너리도 동일
# =============================================================================

def dict_copy() -> None:
    """딕셔너리의 얕은/깊은 복사."""
    print("\n" + "=" * 60)
    print("📌 딕셔너리도 동일")
    print("=" * 60)
    
    original = {
        "name": "Alice",
        "scores": [90, 85, 88],
        "address": {"city": "Seoul", "zip": "12345"}
    }
    
    # 얕은 복사
    shallow = original.copy()  # 또는 dict(original)
    shallow["scores"].append(100)
    shallow["address"]["city"] = "Busan"
    
    print("얕은 복사 후 내부 객체 수정:")
    print(f"original['scores'] = {original['scores']}")  # [90, 85, 88, 100]
    print(f"original['address'] = {original['address']}")  # {'city': 'Busan', ...}
    
    # 깊은 복사
    original2 = {
        "name": "Bob",
        "scores": [70, 75, 80],
        "address": {"city": "Seoul", "zip": "54321"}
    }
    
    deep = copy.deepcopy(original2)
    deep["scores"].append(100)
    deep["address"]["city"] = "Incheon"
    
    print("\n깊은 복사 후 내부 객체 수정:")
    print(f"original2['scores'] = {original2['scores']}")  # [70, 75, 80]
    print(f"original2['address'] = {original2['address']}")  # {'city': 'Seoul', ...}


# =============================================================================
# 5️⃣ 복사 방법 정리
# =============================================================================

def copy_methods_summary() -> None:
    """복사 방법 정리."""
    print("\n" + "=" * 60)
    print("📌 복사 방법 정리")
    print("=" * 60)
    
    print("""
    1. 리스트 복사:
       얕은 복사: list.copy(), list[:], list(list), copy.copy()
       깊은 복사: copy.deepcopy()
    
    2. 딕셔너리 복사:
       얕은 복사: dict.copy(), dict(dict), {**dict}, copy.copy()
       깊은 복사: copy.deepcopy()
    
    3. 셋 복사:
       얕은 복사: set.copy(), set(set), copy.copy()
       깊은 복사: copy.deepcopy() (보통 불필요 - 셋은 불변 객체만 포함)
    
    4. 언제 깊은 복사가 필요한가?
       - 중첩 구조 (리스트 안의 리스트, 딕셔너리 안의 리스트 등)
       - 원본과 완전히 독립적인 복사본이 필요할 때
       - 복잡한 객체 그래프를 복사할 때
    
    5. 깊은 복사의 비용:
       - 시간: 모든 중첩 객체를 재귀적으로 복사
       - 메모리: 모든 객체가 새로 생성됨
       - 순환 참조: deepcopy가 알아서 처리
    """)


# =============================================================================
# 6️⃣ 실무 팁: 불변 객체 선호
# =============================================================================

def immutable_preference() -> None:
    """불변 객체를 사용하면 복사 문제 회피."""
    print("\n" + "=" * 60)
    print("💡 실무 팁: 불변 객체 선호")
    print("=" * 60)
    
    from dataclasses import dataclass
    
    # 불변 데이터클래스
    @dataclass(frozen=True)
    class Point:
        x: float
        y: float
    
    @dataclass(frozen=True)
    class Rectangle:
        top_left: Point
        bottom_right: Point
    
    # 불변 객체는 복사 걱정 없음
    p1 = Point(0, 0)
    p2 = Point(10, 10)
    rect = Rectangle(p1, p2)
    
    # 새 객체 생성으로 "수정"
    new_rect = Rectangle(Point(5, 5), rect.bottom_right)
    
    print(f"rect = {rect}")
    print(f"new_rect = {new_rect}")
    print(f"rect.top_left is new_rect.bottom_right? {rect.bottom_right is new_rect.bottom_right}")  # True, 안전함
    
    print("""
    💡 불변 객체의 장점:
    - 복사 없이 안전하게 공유 가능
    - 스레드 안전
    - 해시 가능 (딕셔너리 키, 셋 원소로 사용)
    - 함수형 프로그래밍과 잘 어울림
    """)


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    assignment_vs_copy()
    shallow_copy_gotcha()
    deep_copy_solution()
    dict_copy()
    copy_methods_summary()
    immutable_preference()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    📌 기억할 것:
    
    1. 할당 (=): 같은 객체 참조
    2. 얕은 복사: 외부 객체만 새로 생성, 내부 객체는 공유
    3. 깊은 복사: 모든 중첩 객체 재귀적으로 복사
    
    ✅ 권장 패턴:
    
    # 단순 리스트
    new_list = original.copy()
    
    # 중첩 구조
    import copy
    new_nested = copy.deepcopy(original)
    
    # 최선: 불변 객체 사용
    @dataclass(frozen=True)
    class ImmutableData:
        ...
    """)


if __name__ == "__main__":
    main()

