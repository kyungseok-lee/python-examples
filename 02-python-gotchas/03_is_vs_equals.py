#!/usr/bin/env python3
"""
03_is_vs_equals.py - is vs == 차이 (🟠 중요)

📌 핵심 개념:
   - is: 객체 동일성 (identity) - 같은 메모리 주소?
   - ==: 값 동등성 (equality) - 값이 같은가?
   
   Python은 작은 정수(-5~256)와 짧은 문자열을 캐싱(인터닝)하므로
   예상치 못한 is 결과가 나올 수 있습니다.

🔄 다른 언어 비교:
   - Java: == 는 참조 비교, .equals()는 값 비교 (Python과 반대 느낌!)
   - Go: == 는 값 비교 (Python의 ==와 동일)
   - Kotlin: == 는 값 비교, === 는 참조 비교

⚠️ 주의사항:
   - None 체크는 항상 is None (유일한 싱글톤)
   - 숫자/문자열 비교는 항상 ==
   - is를 값 비교에 쓰면 인터닝으로 인한 버그 발생

📚 참고: https://realpython.com/python-is-identity-vs-equality/
"""

from __future__ import annotations


# =============================================================================
# 1️⃣ 기본 개념: is vs ==
# =============================================================================

def basic_concept() -> None:
    """is vs == 기본 개념."""
    print("=" * 60)
    print("📌 is vs == 기본 개념")
    print("=" * 60)
    
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"c = a, id(c) = {id(c)}")
    
    print(f"\na == b: {a == b}")  # True (값이 같음)
    print(f"a is b: {a is b}")    # False (다른 객체)
    print(f"a == c: {a == c}")    # True (값이 같음)
    print(f"a is c: {a is c}")    # True (같은 객체)
    
    print("""
    💡 Java 개발자를 위한 비교:
    
    Python          Java
    ------          ----
    a == b          a.equals(b)  # 값 비교
    a is b          a == b       # 참조 비교
    """)


# =============================================================================
# 2️⃣ ⚠️ 정수 캐싱 (Integer Caching)
# =============================================================================

def integer_caching() -> None:
    """Python의 작은 정수 캐싱 함정."""
    print("\n" + "=" * 60)
    print("⚠️ 정수 캐싱 함정 (-5 ~ 256)")
    print("=" * 60)
    
    # 작은 정수 (-5 ~ 256)는 캐싱됨
    a = 256
    b = 256
    print(f"a = 256, b = 256")
    print(f"a == b: {a == b}")  # True
    print(f"a is b: {a is b}")  # True (캐싱!)
    
    # 범위 밖의 정수는 캐싱 안됨
    x = 257
    y = 257
    print(f"\nx = 257, y = 257")
    print(f"x == y: {x == y}")  # True
    print(f"x is y: {x is y}")  # False (새 객체!)
    
    print("""
    ⚠️ 위험한 패턴:
    if some_value is 100:  # 작동할 수도 있지만...
        ...
    
    if some_value is 300:  # 절대 True가 안됨!
        ...
    
    ✅ 올바른 패턴:
    if some_value == 100:  # 항상 값 비교 사용
        ...
    """)


# =============================================================================
# 3️⃣ ⚠️ 문자열 인터닝 (String Interning)
# =============================================================================

def string_interning() -> None:
    """Python의 문자열 인터닝 함정."""
    print("\n" + "=" * 60)
    print("⚠️ 문자열 인터닝 함정")
    print("=" * 60)
    
    # 리터럴 문자열은 인터닝됨
    s1 = "hello"
    s2 = "hello"
    print(f's1 = "hello", s2 = "hello"')
    print(f"s1 == s2: {s1 == s2}")  # True
    print(f"s1 is s2: {s1 is s2}")  # True (인터닝!)
    
    # 동적으로 생성된 문자열은 인터닝 안됨
    s3 = "".join(["h", "e", "l", "l", "o"])
    print(f'\ns3 = "".join(["h","e","l","l","o"])')
    print(f"s1 == s3: {s1 == s3}")  # True
    print(f"s1 is s3: {s1 is s3}")  # False (새 객체!)
    
    # 공백이 있는 문자열은 인터닝 안됨
    a = "hello world"
    b = "hello world"
    print(f'\na = "hello world", b = "hello world"')
    print(f"a == b: {a == b}")  # True
    # 인터닝 여부는 구현에 따라 다름 (신뢰하지 말 것!)
    
    print("""
    ⚠️ 문자열 비교는 반드시 == 사용!
    
    ❌ if user_input is "admin":  # 작동 안 할 수 있음
    ✅ if user_input == "admin":  # 항상 올바르게 작동
    """)


# =============================================================================
# 4️⃣ ✅ is의 올바른 사용: None 체크
# =============================================================================

def none_check() -> None:
    """None 체크는 is를 사용해야 하는 이유."""
    print("\n" + "=" * 60)
    print("✅ is의 올바른 사용: None 체크")
    print("=" * 60)
    
    # None은 싱글톤 (전역적으로 하나만 존재)
    x = None
    y = None
    print(f"x = None, y = None")
    print(f"x is None: {x is None}")    # True
    print(f"y is None: {y is None}")    # True
    print(f"x is y: {x is y}")          # True (같은 싱글톤)
    
    # __eq__를 오버라이드한 객체와의 비교
    class WeirdClass:
        def __eq__(self, other: object) -> bool:
            return True  # 모든 것과 같다고 주장
    
    weird = WeirdClass()
    print(f"\n# __eq__를 오버라이드한 클래스")
    print(f"weird == None: {weird == None}")   # True (잘못된 결과!)  # noqa: E711
    print(f"weird is None: {weird is None}")   # False (올바른 결과!)
    
    print("""
    ✅ None 체크 패턴:
    
    if x is None:      # 권장
        ...
    
    if x is not None:  # 권장
        ...
    
    ❌ 하지 말 것:
    if x == None:      # __eq__ 오버라이드에 취약
    if not x:          # 0, "", [] 도 False로 평가됨
    """)


# =============================================================================
# 5️⃣ is의 다른 올바른 사용: 싱글톤 패턴
# =============================================================================

class Singleton:
    """싱글톤 패턴 예시."""
    
    _instance: "Singleton | None" = None
    
    def __new__(cls) -> "Singleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# 센티넬 값 (None과 구분되는 "값 없음" 표시)
_UNSET = object()


def get_value(data: dict, key: str, default: object = _UNSET) -> object:
    """센티넬 패턴: None도 유효한 값일 때."""
    value = data.get(key, _UNSET)
    if value is _UNSET:
        if default is _UNSET:
            raise KeyError(key)
        return default
    return value


def singleton_and_sentinel() -> None:
    """싱글톤과 센티넬 패턴."""
    print("\n" + "=" * 60)
    print("✅ is의 다른 올바른 사용: 싱글톤/센티넬")
    print("=" * 60)
    
    # 싱글톤 확인
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton: s1 is s2 = {s1 is s2}")  # True
    
    # 센티넬 패턴
    data = {"name": "Alice", "value": None}
    print(f"\ndata = {data}")
    print(f"get_value(data, 'name') = {get_value(data, 'name')}")
    print(f"get_value(data, 'value') = {get_value(data, 'value')}")  # None 반환 (유효한 값)
    
    print("""
    💡 센티넬 패턴:
    - None도 유효한 값일 때 "값 없음"을 표시
    - _UNSET = object() 로 고유 객체 생성
    - is로 비교 (==는 object의 __eq__가 is와 동일)
    """)


# =============================================================================
# 6️⃣ 실수하기 쉬운 패턴들
# =============================================================================

def common_mistakes() -> None:
    """흔한 실수 패턴들."""
    print("\n" + "=" * 60)
    print("❌ 흔한 실수 패턴들")
    print("=" * 60)
    
    # 실수 1: 리스트 비어있음 체크
    items: list[int] = []
    
    print("# 빈 리스트 체크")
    print(f"items = {items}")
    
    # 잘못된 방법들
    if items is []:  # 항상 False!
        print("  is []: True")
    else:
        print("  is []: False (항상!)")
    
    # 올바른 방법들
    if not items:  # Pythonic
        print("  not items: True (Pythonic)")
    
    if len(items) == 0:  # 명시적
        print("  len(items) == 0: True")
    
    # 실수 2: True/False 비교
    flag = True
    
    print(f"\n# Boolean 비교")
    print(f"flag = {flag}")
    
    # 나쁜 패턴
    if flag is True:  # 작동하지만 불필요
        print("  flag is True: 작동하지만 불필요")
    
    # 좋은 패턴
    if flag:  # Pythonic
        print("  if flag: (Pythonic)")
    
    print("""
    💡 정리:
    
    빈 컬렉션 체크:
    ✅ if not items:
    ✅ if len(items) == 0:
    ❌ if items is []:
    ❌ if items == []:  # 작동하지만 비효율
    
    Boolean 체크:
    ✅ if flag:
    ✅ if not flag:
    ❌ if flag is True:
    ❌ if flag == True:
    """)


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    basic_concept()
    integer_caching()
    string_interning()
    none_check()
    singleton_and_sentinel()
    common_mistakes()
    
    print("\n" + "=" * 60)
    print("💡 핵심 정리")
    print("=" * 60)
    print("""
    📌 is vs == 사용 가이드:
    
    ✅ is 사용:
       - None 체크: if x is None, if x is not None
       - 싱글톤/센티넬 비교
       - True/False는 그냥 if x: 사용
    
    ✅ == 사용:
       - 숫자 비교: if x == 100
       - 문자열 비교: if name == "admin"
       - 컬렉션 비교: if items == [1, 2, 3]
    
    ❌ 하지 말 것:
       - if x is 100  (캐싱 범위 밖이면 항상 False)
       - if s is "hello"  (인터닝 여부 불확실)
       - if items is []  (항상 False)
    """)


if __name__ == "__main__":
    main()

