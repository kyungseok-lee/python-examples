#!/usr/bin/env python3
"""
04_late_binding_closures.py - 클로저 Late Binding (🟠 중요)

📌 핵심 개념:
   Python 클로저는 변수를 "late binding"합니다.
   루프 안에서 람다/함수를 생성하면 모든 함수가 마지막 값을 참조합니다.

🔄 다른 언어 비교:
   - JavaScript: 동일한 문제 있음 (var 사용 시)
   - Java: 람다에서 effectively final 변수만 캡처 (문제 없음)
   - Go: 클로저가 변수를 캡처하지만 루프 변수는 복사됨 (Go 1.22+)
   - Kotlin: Java와 동일, effectively final 필요

⚠️ 주의사항:
   - for 루프에서 람다 생성 시 특히 주의
   - 콜백 등록, 이벤트 핸들러에서 자주 발생

📚 참고: https://docs.python-guide.org/writing/gotchas/#late-binding-closures
"""

from __future__ import annotations

from typing import Callable


# =============================================================================
# 1️⃣ ❌ 문제가 있는 코드
# =============================================================================

def demonstrate_problem() -> None:
    """Late binding 문제 재현."""
    print("=" * 60)
    print("❌ 문제: Late Binding Closures")
    print("=" * 60)
    
    # 0부터 4까지의 값을 반환하는 함수들을 만들고 싶음
    functions: list[Callable[[], int]] = []
    
    for i in range(5):
        functions.append(lambda: i)  # i를 캡처
    
    print("\n# 기대: 0, 1, 2, 3, 4")
    print("# 실제:")
    for f in functions:
        print(f"  {f()}", end=" ")  # 4, 4, 4, 4, 4 출력!
    print()
    
    print("""
    ❓ 왜 모두 4인가?
    
    lambda: i 는 i의 "현재 값"이 아니라 i라는 "변수 자체"를 참조합니다.
    루프가 끝난 후 i = 4 이므로, 모든 람다가 4를 반환합니다.
    
    이것이 "late binding" - 람다 실행 시점에 i의 값을 읽음.
    """)


# =============================================================================
# 2️⃣ 왜 이런 일이 발생하는가?
# =============================================================================

def why_this_happens() -> None:
    """Python의 클로저 동작 설명."""
    print("\n" + "=" * 60)
    print("📖 왜 이런 일이 발생하는가?")
    print("=" * 60)
    
    print("""
    Python 클로저의 동작:
    
    1. 클로저는 외부 변수에 대한 "참조(reference)"를 저장
    2. 람다/함수가 실행될 때 참조를 통해 현재 값을 읽음
    3. 루프가 끝난 후에는 루프 변수가 마지막 값을 가지고 있음
    
    💡 Java와 비교:
    
    // Java - 컴파일 에러!
    for (int i = 0; i < 5; i++) {
        // error: variable i is not effectively final
        list.add(() -> i);
    }
    
    Java는 람다에서 변하는 변수를 캡처할 수 없어서 이 버그가 불가능!
    
    💡 JavaScript (var) 와 동일:
    
    for (var i = 0; i < 5; i++) {
        funcs.push(function() { return i; });
    }
    // 모두 5 반환 (JavaScript도 동일한 문제)
    
    💡 JavaScript (let) - 해결됨:
    
    for (let i = 0; i < 5; i++) {
        funcs.push(function() { return i; });
    }
    // 0, 1, 2, 3, 4 (let은 블록 스코프)
    
    Python에는 let 같은 블록 스코프가 없어서 다른 방법 필요!
    """)


# =============================================================================
# 3️⃣ ✅ 해결 방법 1: 기본 인자로 값 캡처
# =============================================================================

def solution_default_argument() -> None:
    """기본 인자로 값 캡처."""
    print("\n" + "=" * 60)
    print("✅ 해결 1: 기본 인자로 값 캡처")
    print("=" * 60)
    
    functions: list[Callable[[], int]] = []
    
    for i in range(5):
        # i=i 로 현재 값을 기본 인자로 "복사"
        functions.append(lambda i=i: i)
    
    print("\n# 결과: 0, 1, 2, 3, 4")
    for f in functions:
        print(f"  {f()}", end=" ")
    print()
    
    print("""
    💡 동작 원리:
    lambda i=i: i
           ^^^
           이 부분이 "현재 시점의 i 값"을 기본 인자로 저장
    
    기본 인자는 함수 정의 시점에 평가되므로 값이 복사됨!
    (01_mutable_default_args.py와 연결되는 개념)
    """)


# =============================================================================
# 4️⃣ ✅ 해결 방법 2: functools.partial 사용
# =============================================================================

from functools import partial


def solution_partial() -> None:
    """functools.partial 사용."""
    print("\n" + "=" * 60)
    print("✅ 해결 2: functools.partial")
    print("=" * 60)
    
    def make_multiplier(x: int) -> int:
        return x
    
    functions: list[Callable[[], int]] = []
    
    for i in range(5):
        functions.append(partial(make_multiplier, i))
    
    print("\n# 결과: 0, 1, 2, 3, 4")
    for f in functions:
        print(f"  {f()}", end=" ")
    print()
    
    print("""
    💡 partial의 장점:
    - 가독성이 좋음
    - 타입 힌트와 잘 어울림
    - 인자가 많을 때 유용
    """)


# =============================================================================
# 5️⃣ ✅ 해결 방법 3: 팩토리 함수 사용
# =============================================================================

def solution_factory() -> None:
    """팩토리 함수로 클로저 생성."""
    print("\n" + "=" * 60)
    print("✅ 해결 3: 팩토리 함수")
    print("=" * 60)
    
    def make_func(x: int) -> Callable[[], int]:
        """각 호출마다 새로운 스코프에서 x를 캡처."""
        return lambda: x
    
    functions: list[Callable[[], int]] = []
    
    for i in range(5):
        functions.append(make_func(i))  # i가 x로 복사됨
    
    print("\n# 결과: 0, 1, 2, 3, 4")
    for f in functions:
        print(f"  {f()}", end=" ")
    print()
    
    print("""
    💡 팩토리 함수의 장점:
    - 가장 명확한 의도 표현
    - 복잡한 로직을 담을 수 있음
    - 테스트하기 쉬움
    """)


# =============================================================================
# 6️⃣ 실무 예시: 버튼 콜백
# =============================================================================

def practical_example() -> None:
    """실무에서 자주 발생하는 케이스."""
    print("\n" + "=" * 60)
    print("📦 실무 예시: 버튼 콜백")
    print("=" * 60)
    
    # GUI 프레임워크에서 버튼 콜백 등록 시뮬레이션
    class Button:
        def __init__(self, label: str) -> None:
            self.label = label
            self.callback: Callable[[], None] | None = None
        
        def on_click(self, callback: Callable[[], None]) -> None:
            self.callback = callback
        
        def click(self) -> None:
            if self.callback:
                self.callback()
    
    # ❌ 잘못된 패턴
    print("\n❌ 잘못된 패턴:")
    buttons_bad: list[Button] = []
    for i in range(3):
        btn = Button(f"Button {i}")
        btn.on_click(lambda: print(f"  Clicked button {i}"))  # 모두 2!
        buttons_bad.append(btn)
    
    for btn in buttons_bad:
        btn.click()
    
    # ✅ 올바른 패턴
    print("\n✅ 올바른 패턴:")
    buttons_good: list[Button] = []
    for i in range(3):
        btn = Button(f"Button {i}")
        btn.on_click(lambda i=i: print(f"  Clicked button {i}"))
        buttons_good.append(btn)
    
    for btn in buttons_good:
        btn.click()


# =============================================================================
# 7️⃣ 리스트 컴프리헨션에서도 동일
# =============================================================================

def comprehension_case() -> None:
    """리스트 컴프리헨션에서의 같은 문제."""
    print("\n" + "=" * 60)
    print("📌 리스트 컴프리헨션에서도 동일")
    print("=" * 60)
    
    # ❌ 잘못된 패턴
    funcs_bad = [lambda: i for i in range(5)]
    print("\n❌ [lambda: i for i in range(5)]:")
    print(f"  Results: {[f() for f in funcs_bad]}")  # [4, 4, 4, 4, 4]
    
    # ✅ 올바른 패턴
    funcs_good = [lambda i=i: i for i in range(5)]
    print("\n✅ [lambda i=i: i for i in range(5)]:")
    print(f"  Results: {[f() for f in funcs_good]}")  # [0, 1, 2, 3, 4]


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    demonstrate_problem()
    why_this_happens()
    solution_default_argument()
    solution_partial()
    solution_factory()
    practical_example()
    comprehension_case()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    ❌ 문제 패턴:
       for i in range(n):
           funcs.append(lambda: i)  # 모두 마지막 값!
    
    ✅ 해결 방법 3가지:
    
    1. 기본 인자 (가장 간단):
       lambda i=i: i
    
    2. partial (가독성 좋음):
       from functools import partial
       partial(func, i)
    
    3. 팩토리 함수 (가장 명확):
       def make_func(x):
           return lambda: x
    
    🔍 기억할 것:
    - 루프 안에서 람다 생성 시 항상 주의!
    - 콜백, 이벤트 핸들러에서 특히 빈번함
    """)


if __name__ == "__main__":
    main()

