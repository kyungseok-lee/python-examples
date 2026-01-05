#!/usr/bin/env python3
"""
06_variable_scope_leaking.py - 변수 스코프 누출 (🟡 주의)

📌 핵심 개념:
   Python에는 블록 스코프가 없습니다.
   for/while/if/try 블록 안에서 생성된 변수가 블록 밖에서도 접근 가능합니다.

🔄 다른 언어 비교:
   - Java: 블록 스코프 있음, for 루프 변수는 밖에서 접근 불가
   - Go: 블록 스코프 있음
   - JavaScript (let): 블록 스코프 있음
   - JavaScript (var): Python과 유사하게 함수 스코프
   - Python: 함수/클래스/모듈 스코프만 있음

⚠️ 주의사항:
   - for 루프 변수가 밖에서 마지막 값으로 접근됨
   - 의도치 않은 변수 재사용 버그 발생 가능
   - 컴프리헨션은 예외적으로 자체 스코프 가짐 (Python 3+)

📚 참고: https://docs.python.org/3/reference/executionmodel.html#naming-and-binding
"""

from __future__ import annotations


# =============================================================================
# 1️⃣ for 루프 변수 누출
# =============================================================================

def for_loop_leaking() -> None:
    """for 루프 변수가 밖에서 접근 가능."""
    print("=" * 60)
    print("⚠️ for 루프 변수 누출")
    print("=" * 60)
    
    # Python
    for i in range(5):
        pass
    
    print(f"루프 후 i = {i}")  # 4 (마지막 값!)
    
    # Java에서는 컴파일 에러:
    # for (int i = 0; i < 5; i++) { }
    # System.out.println(i);  // error: cannot find symbol
    
    # 실제 문제가 되는 경우
    for item in ["apple", "banana", "cherry"]:
        if item == "banana":
            found = item
            break
    
    print(f"\n검색 결과: {found}")  # 'banana'
    print(f"마지막 item: {item}")  # 'banana' (break로 멈춤)
    
    # break 없이
    for item in ["apple", "banana", "cherry"]:
        pass
    
    print(f"루프 후 item: {item}")  # 'cherry'


# =============================================================================
# 2️⃣ if 블록 변수 누출
# =============================================================================

def if_block_leaking() -> None:
    """if 블록 안에서 생성된 변수도 밖에서 접근 가능."""
    print("\n" + "=" * 60)
    print("⚠️ if 블록 변수 누출")
    print("=" * 60)
    
    condition = True
    
    if condition:
        result = "success"
    # else 가 없으면 result가 정의되지 않을 수도!
    
    print(f"result = {result}")  # 'success'
    
    # 위험한 패턴
    def risky_function(flag: bool) -> str:
        if flag:
            message = "True case"
        # flag가 False면 message가 정의되지 않음!
        return message  # UnboundLocalError 가능성
    
    print(f"\nrisky_function(True) = {risky_function(True)}")
    
    try:
        risky_function(False)
    except UnboundLocalError as e:
        print(f"risky_function(False) -> UnboundLocalError: {e}")


# =============================================================================
# 3️⃣ try/except 블록 변수 누출
# =============================================================================

def try_except_leaking() -> None:
    """try/except 안에서 생성된 변수도 밖에서 접근 가능."""
    print("\n" + "=" * 60)
    print("⚠️ try/except 블록 변수 누출")
    print("=" * 60)
    
    try:
        data = [1, 2, 3]
        value = data[1]
    except IndexError:
        value = None
    
    print(f"value = {value}")  # 2
    print(f"data = {data}")    # [1, 2, 3] - try 블록 안에서 생성됨
    
    # 특이 케이스: except에서 바인딩된 예외 변수
    # Python 3에서는 except 블록이 끝나면 삭제됨!
    try:
        1 / 0
    except ZeroDivisionError as e:
        error_message = str(e)
    
    print(f"\nerror_message = {error_message}")
    
    # e는 블록 끝에서 삭제됨
    try:
        print(f"e = {e}")
    except NameError:
        print("e는 삭제됨 (Python 3 특성)")


# =============================================================================
# 4️⃣ 컴프리헨션의 스코프 (예외)
# =============================================================================

def comprehension_scope() -> None:
    """컴프리헨션은 자체 스코프를 가짐 (Python 3+)."""
    print("\n" + "=" * 60)
    print("✅ 컴프리헨션 스코프 (예외)")
    print("=" * 60)
    
    x = "outer"
    
    # 리스트 컴프리헨션
    result = [x for x in range(5)]  # 이 x는 컴프리헨션 내부
    
    print(f"result = {result}")
    print(f"x = {x}")  # 'outer' - 바깥 x가 보존됨!
    
    print("""
    💡 Python 2 vs Python 3:
    
    # Python 2
    [x for x in range(5)]
    print(x)  # 4 (누출!)
    
    # Python 3
    [x for x in range(5)]
    print(x)  # NameError 또는 바깥 x 값
    
    Python 3에서 컴프리헨션은 자체 스코프를 가집니다!
    제너레이터 표현식도 마찬가지.
    """)


# =============================================================================
# 5️⃣ 안전한 패턴
# =============================================================================

def safe_patterns() -> None:
    """안전한 패턴들."""
    print("\n" + "=" * 60)
    print("✅ 안전한 패턴")
    print("=" * 60)
    
    # 패턴 1: 미리 초기화
    result: str | None = None  # 명시적 초기화
    
    for item in ["a", "b", "c"]:
        if item == "b":
            result = item
            break
    
    if result is not None:
        print(f"Found: {result}")
    
    # 패턴 2: 함수로 캡슐화
    def find_item(items: list[str], target: str) -> str | None:
        for item in items:
            if item == target:
                return item
        return None
    
    found = find_item(["a", "b", "c"], "b")
    print(f"Found with function: {found}")
    
    # 패턴 3: walrus 연산자 (Python 3.8+)
    items = ["apple", "banana", "cherry"]
    
    if (found := next((x for x in items if x.startswith("b")), None)) is not None:
        print(f"Found with walrus: {found}")
    
    print("""
    💡 권장 패턴:
    
    1. 변수 미리 초기화 (None 또는 기본값)
    2. 함수로 로직 캡슐화
    3. walrus 연산자로 조건문에서 바인딩
    """)


# =============================================================================
# 6️⃣ LEGB 규칙
# =============================================================================

def legb_rule() -> None:
    """Python의 이름 탐색 규칙: LEGB."""
    print("\n" + "=" * 60)
    print("📖 LEGB 규칙")
    print("=" * 60)
    
    # L: Local (함수 내부)
    # E: Enclosing (외부 함수)
    # G: Global (모듈)
    # B: Built-in (내장)
    
    global_var = "global"
    
    def outer():
        enclosing_var = "enclosing"
        
        def inner():
            local_var = "local"
            print(f"  local_var = {local_var}")
            print(f"  enclosing_var = {enclosing_var}")
            print(f"  global_var = {global_var}")
            print(f"  len (built-in) = {len}")
        
        inner()
    
    outer()
    
    print("""
    💡 LEGB 탐색 순서:
    1. Local: 현재 함수 내부
    2. Enclosing: 외부 함수 (중첩 함수인 경우)
    3. Global: 모듈 레벨
    4. Built-in: Python 내장 (print, len, ...)
    
    주의: 블록(for, if, try)은 새로운 스코프를 만들지 않음!
    """)


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    for_loop_leaking()
    if_block_leaking()
    try_except_leaking()
    comprehension_scope()
    safe_patterns()
    legb_rule()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    📌 Python 스코프 특징:
    
    1. 블록 스코프 없음
       - for, while, if, try 블록은 스코프를 만들지 않음
       - 블록 안에서 생성된 변수가 밖에서 접근 가능
    
    2. 함수 스코프
       - 함수는 새로운 스코프를 만듦
       - 함수 내부 변수는 외부에서 접근 불가
    
    3. 컴프리헨션 스코프 (Python 3+)
       - 리스트/딕셔너리/셋 컴프리헨션
       - 제너레이터 표현식
       - 자체 스코프를 가짐
    
    ✅ 권장:
    - 변수 미리 초기화
    - 로직을 함수로 분리
    - 의도하지 않은 재사용 주의
    """)


if __name__ == "__main__":
    main()

