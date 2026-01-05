#!/usr/bin/env python3
"""
07_circular_reference.py - 순환 참조와 메모리 (🟡 주의)

📌 핵심 개념:
   Python은 참조 카운팅 + 순환 GC를 사용합니다.
   순환 참조가 있으면 참조 카운팅만으로는 해제되지 않고,
   순환 GC가 실행될 때까지 메모리에 남아있습니다.

🔄 다른 언어 비교:
   - Java: Mark & Sweep GC가 순환 참조 자동 처리
   - Go: Tracing GC가 순환 참조 자동 처리
   - Swift/Objective-C: ARC(참조 카운팅), weak reference로 순환 참조 방지

⚠️ 주의사항:
   - __del__ 메서드가 있으면 순환 GC가 수집하지 못할 수 있음 (Python 3.4 이전)
   - 대용량 객체의 순환 참조는 메모리 문제 유발
   - weakref로 해결 가능

📚 참고: https://docs.python.org/3/library/gc.html
"""

from __future__ import annotations

import gc
import weakref
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


# =============================================================================
# 1️⃣ 참조 카운팅 기본
# =============================================================================

def reference_counting_basics() -> None:
    """Python의 참조 카운팅 동작."""
    print("=" * 60)
    print("📌 참조 카운팅 기본")
    print("=" * 60)
    
    import sys
    
    # 객체 생성 - 참조 카운트 1
    a = [1, 2, 3]
    print(f"a = [1, 2, 3]")
    print(f"참조 카운트: {sys.getrefcount(a) - 1}")  # -1: getrefcount 자체가 참조
    
    # 다른 변수가 참조 - 참조 카운트 증가
    b = a
    print(f"\nb = a")
    print(f"참조 카운트: {sys.getrefcount(a) - 1}")
    
    # 참조 제거 - 참조 카운트 감소
    del b
    print(f"\ndel b")
    print(f"참조 카운트: {sys.getrefcount(a) - 1}")
    
    # 참조 카운트가 0이 되면 즉시 해제
    print("""
    💡 참조 카운팅의 장점:
    - 참조가 없어지면 즉시 메모리 해제
    - 예측 가능한 메모리 관리
    - 실시간 시스템에 유리
    
    💡 참조 카운팅의 한계:
    - 순환 참조를 처리하지 못함
    - 순환 GC가 추가로 필요
    """)


# =============================================================================
# 2️⃣ 순환 참조 문제
# =============================================================================

class Node:
    """순환 참조를 만드는 클래스."""
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbor: Node | None = None
    
    def __del__(self) -> None:
        print(f"  Node({self.name}) deleted")


def circular_reference_problem() -> None:
    """순환 참조가 메모리에 남는 문제."""
    print("\n" + "=" * 60)
    print("⚠️ 순환 참조 문제")
    print("=" * 60)
    
    # GC 비활성화하여 문제 재현
    gc.disable()
    
    print("\n1. 순환 참조 생성:")
    node_a = Node("A")
    node_b = Node("B")
    
    # 순환 참조!
    node_a.neighbor = node_b
    node_b.neighbor = node_a
    
    print(f"   A -> B: {node_a.neighbor.name}")
    print(f"   B -> A: {node_b.neighbor.name}")
    
    print("\n2. 변수 삭제:")
    del node_a
    del node_b
    print("   del node_a, del node_b 실행됨")
    print("   하지만 __del__은 호출되지 않음! (순환 참조)")
    
    print("\n3. 순환 GC 실행:")
    collected = gc.collect()
    print(f"   수집된 객체 수: {collected}")
    
    gc.enable()
    
    print("""
    💡 순환 참조 시나리오:
    
    node_a ──► Node("A") ──┐
                          │
                          ▼
    node_b ──► Node("B") ◄┘
         └────────────────┘
    
    del node_a, del node_b 후에도:
    - Node("A")의 참조 카운트: 1 (Node("B")가 참조)
    - Node("B")의 참조 카운트: 1 (Node("A")가 참조)
    
    참조 카운트가 0이 아니므로 즉시 해제되지 않음!
    순환 GC가 실행되어야 수집됨.
    """)


# =============================================================================
# 3️⃣ ✅ weakref로 해결
# =============================================================================

class NodeWithWeakRef:
    """weakref로 순환 참조 방지."""
    
    def __init__(self, name: str) -> None:
        self.name = name
        self._neighbor: weakref.ref["NodeWithWeakRef"] | None = None
    
    @property
    def neighbor(self) -> "NodeWithWeakRef | None":
        if self._neighbor is None:
            return None
        return self._neighbor()  # weakref 호출
    
    @neighbor.setter
    def neighbor(self, node: "NodeWithWeakRef | None") -> None:
        if node is None:
            self._neighbor = None
        else:
            self._neighbor = weakref.ref(node)
    
    def __del__(self) -> None:
        print(f"  NodeWithWeakRef({self.name}) deleted")


def weakref_solution() -> None:
    """weakref로 순환 참조 방지."""
    print("\n" + "=" * 60)
    print("✅ weakref로 해결")
    print("=" * 60)
    
    gc.disable()
    
    print("\n1. weakref로 연결:")
    node_a = NodeWithWeakRef("A")
    node_b = NodeWithWeakRef("B")
    
    node_a.neighbor = node_b  # 약한 참조
    node_b.neighbor = node_a  # 약한 참조
    
    print(f"   A -> B: {node_a.neighbor.name if node_a.neighbor else None}")
    print(f"   B -> A: {node_b.neighbor.name if node_b.neighbor else None}")
    
    print("\n2. 변수 삭제:")
    del node_b
    print("   del node_b")
    
    # node_a.neighbor는 이제 None (약한 참조가 해제됨)
    print(f"   node_a.neighbor: {node_a.neighbor}")
    
    del node_a
    print("   del node_a")
    
    gc.enable()
    
    print("""
    💡 weakref 동작:
    
    - weakref.ref(obj)는 obj에 대한 "약한 참조" 생성
    - 약한 참조는 참조 카운트를 증가시키지 않음
    - obj가 해제되면 weakref()는 None 반환
    
    사용처:
    - 캐시 (메모리 부족 시 자동 해제)
    - 옵저버 패턴 (리스너 목록)
    - 부모-자식 관계 (자식이 부모를 약한 참조)
    """)


# =============================================================================
# 4️⃣ 실무 패턴: 캐시
# =============================================================================

def cache_with_weakref() -> None:
    """weakref를 사용한 캐시 패턴."""
    print("\n" + "=" * 60)
    print("💡 실무 패턴: WeakValueDictionary 캐시")
    print("=" * 60)
    
    class ExpensiveObject:
        def __init__(self, id: int) -> None:
            self.id = id
            print(f"  Created ExpensiveObject({id})")
        
        def __del__(self) -> None:
            print(f"  Deleted ExpensiveObject({self.id})")
    
    # 약한 참조 딕셔너리: 값이 다른 곳에서 참조되지 않으면 자동 삭제
    cache: weakref.WeakValueDictionary[int, ExpensiveObject] = weakref.WeakValueDictionary()
    
    print("\n1. 객체 생성 및 캐시에 저장:")
    obj1 = ExpensiveObject(1)
    obj2 = ExpensiveObject(2)
    
    cache[1] = obj1
    cache[2] = obj2
    
    print(f"   캐시 키: {list(cache.keys())}")
    
    print("\n2. obj1 삭제:")
    del obj1
    
    print(f"   캐시 키: {list(cache.keys())}")  # obj1이 자동으로 제거됨
    
    print("\n3. 캐시에서 조회:")
    print(f"   cache.get(1): {cache.get(1)}")  # None
    print(f"   cache.get(2): {cache.get(2)}")  # ExpensiveObject
    
    del obj2


# =============================================================================
# 5️⃣ GC 모니터링
# =============================================================================

def gc_monitoring() -> None:
    """GC 동작 모니터링."""
    print("\n" + "=" * 60)
    print("🔍 GC 모니터링")
    print("=" * 60)
    
    # GC 통계
    print("\n1. GC 통계:")
    print(f"   gc.get_count(): {gc.get_count()}")
    print("   (gen0, gen1, gen2) - 각 세대의 할당 횟수")
    
    # GC 임계값
    print(f"\n2. GC 임계값:")
    print(f"   gc.get_threshold(): {gc.get_threshold()}")
    print("   (threshold0, threshold1, threshold2)")
    
    # GC 수동 실행
    print(f"\n3. GC 수동 실행:")
    collected = gc.collect()
    print(f"   gc.collect() -> {collected} 객체 수집")
    
    # 수집 불가능한 객체 (Python 3.4 이전에서만)
    print(f"\n4. 수집 불가능한 객체:")
    print(f"   gc.garbage: {gc.garbage}")
    
    print("""
    💡 GC 세대(Generation):
    
    - Gen 0: 새로 생성된 객체 (자주 검사)
    - Gen 1: Gen 0에서 살아남은 객체
    - Gen 2: Gen 1에서 살아남은 객체 (드물게 검사)
    
    객체가 오래 살아남을수록 높은 세대로 승격
    → "오래된 객체는 더 오래 살 가능성 높음" 가정
    """)


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    reference_counting_basics()
    circular_reference_problem()
    weakref_solution()
    cache_with_weakref()
    gc_monitoring()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    📌 Python 메모리 관리:
    
    1. 참조 카운팅
       - 참조 수가 0이 되면 즉시 해제
       - 순환 참조는 처리 못함
    
    2. 순환 GC
       - 순환 참조를 찾아서 해제
       - 세대별 GC로 효율화
    
    ✅ 순환 참조 방지:
    
    1. weakref 사용
       - weakref.ref(obj)
       - WeakValueDictionary
       - WeakSet
    
    2. 명시적 해제
       - 불필요한 참조 None으로 설정
       - del 사용
    
    3. 컨텍스트 매니저
       - with문으로 리소스 자동 해제
    
    🔍 디버깅:
       - gc.collect(): 수동 GC 실행
       - gc.get_count(): 세대별 할당 수
       - objgraph: 객체 참조 그래프 시각화
    """)


if __name__ == "__main__":
    main()

