#!/usr/bin/env python3
"""
01_syntax_comparison.py - Java/Go/Kotlin과 Python 문법 비교

📌 핵심 개념:
   다른 언어 개발자가 Python으로 전환할 때 알아야 할 문법 차이점

🔄 다른 언어 비교:
   - Java: 정적 타이핑, 장황한 문법, 클래스 필수
   - Go: 정적 타이핑, 간결한 문법, 에러 반환
   - Kotlin: 정적 타이핑, 간결한 문법, null safety
   - Python: 동적 타이핑, 매우 간결, 덕 타이핑

⚠️ 주의사항:
   - Python은 들여쓰기가 문법! (4 spaces 권장)
   - 세미콜론 없음
   - 타입은 런타임에 결정됨

📚 참고: https://docs.python.org/3/tutorial/
"""

from __future__ import annotations


# =============================================================================
# 1️⃣ 변수 선언 비교
# =============================================================================

def variable_declaration() -> None:
    """
    변수 선언 방식 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - Java: int x = 10; String s = "hello";
        - Go:   var x int = 10 또는 x := 10
        - Kotlin: val x: Int = 10 또는 val x = 10
        - Python: 그냥 x = 10 (타입 선언 불필요!)
    """
    print("\n📌 변수 선언")
    print("-" * 50)
    
    # Python: 타입 선언 없이 바로 할당
    x = 10
    name = "Python"
    is_awesome = True
    price = 19.99
    
    print(f"x = {x} (type: {type(x).__name__})")
    print(f"name = {name} (type: {type(name).__name__})")
    print(f"is_awesome = {is_awesome} (type: {type(is_awesome).__name__})")
    print(f"price = {price} (type: {type(price).__name__})")
    
    # 동적 타이핑: 같은 변수에 다른 타입 할당 가능 (권장하지 않음!)
    x = "이제 문자열"  # Java에서는 컴파일 에러!
    print(f"\nx = {x} (type changed to: {type(x).__name__})")
    
    # 타입 힌트 (Python 3.5+): 타입 체커용, 런타임에는 영향 없음
    count: int = 100
    message: str = "Hello"
    print(f"\n타입 힌트 사용: count={count}, message={message}")


# =============================================================================
# 2️⃣ 컬렉션 비교
# =============================================================================

def collections_comparison() -> None:
    """
    컬렉션 타입 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - Java: ArrayList<Integer>, HashMap<String, Integer>
        - Go:   []int, map[string]int
        - Python: list, dict (타입 파라미터 불필요!)
    """
    print("\n📌 컬렉션")
    print("-" * 50)
    
    # 리스트 (Java의 ArrayList, Go의 slice)
    # Java: List<Integer> numbers = Arrays.asList(1, 2, 3);
    # Go:   numbers := []int{1, 2, 3}
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    
    # 딕셔너리 (Java의 HashMap, Go의 map)
    # Java: Map<String, Integer> ages = new HashMap<>();
    # Go:   ages := map[string]int{"Alice": 25}
    ages = {"Alice": 25, "Bob": 30}
    print(f"Dict: {ages}")
    
    # 튜플 (Java에 없음, Go에 없음 - struct 사용)
    # 불변(immutable) 시퀀스
    point = (10, 20)
    print(f"Tuple: {point}")
    
    # 셋 (Java의 HashSet, Go에 내장 없음)
    unique = {1, 2, 3, 3, 3}  # 중복 제거
    print(f"Set: {unique}")
    
    # 리스트 컴프리헨션 (Python의 강력한 기능!)
    # Java: numbers.stream().map(x -> x * 2).collect(Collectors.toList())
    # Go:   for loop 필요
    doubled = [x * 2 for x in numbers]
    print(f"\nList Comprehension: {doubled}")
    
    # 딕셔너리 컴프리헨션
    squared = {x: x**2 for x in range(5)}
    print(f"Dict Comprehension: {squared}")


# =============================================================================
# 3️⃣ 조건문 비교
# =============================================================================

def conditionals_comparison() -> None:
    """
    조건문 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - 괄호 불필요
        - 중괄호 대신 콜론(:)과 들여쓰기
        - elif (else if 아님!)
        - switch 대신 match (Python 3.10+)
    """
    print("\n📌 조건문")
    print("-" * 50)
    
    score = 85
    
    # Java: if (score >= 90) { grade = "A"; }
    # Go:   if score >= 90 { grade = "A" }
    # Python: 괄호 없이, 콜론과 들여쓰기
    if score >= 90:
        grade = "A"
    elif score >= 80:  # else if 아님!
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score {score} -> Grade {grade}")
    
    # 삼항 연산자
    # Java: String result = score >= 60 ? "Pass" : "Fail";
    # Go:   없음 (if문 사용)
    # Python:
    result = "Pass" if score >= 60 else "Fail"
    print(f"Result: {result}")
    
    # match 문 (Python 3.10+, Java의 switch와 유사하지만 더 강력)
    http_status = 404
    match http_status:
        case 200:
            message = "OK"
        case 404:
            message = "Not Found"
        case 500:
            message = "Server Error"
        case _:  # default
            message = "Unknown"
    
    print(f"HTTP {http_status}: {message}")


# =============================================================================
# 4️⃣ 반복문 비교
# =============================================================================

def loops_comparison() -> None:
    """
    반복문 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - for (int i = 0; i < n; i++) 스타일 없음!
        - for-each 스타일이 기본
        - range() 함수로 인덱스 반복
        - enumerate()로 인덱스와 값 동시에
    """
    print("\n📌 반복문")
    print("-" * 50)
    
    fruits = ["apple", "banana", "cherry"]
    
    # Java: for (String fruit : fruits) { ... }
    # Go:   for _, fruit := range fruits { ... }
    # Python:
    print("For-each style:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # 인덱스가 필요한 경우
    # Java: for (int i = 0; i < fruits.size(); i++) { ... }
    # Go:   for i, fruit := range fruits { ... }
    # Python: enumerate() 사용 (권장)
    print("\nWith index (enumerate):")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # range() - Java의 IntStream.range()와 유사
    print("\nrange(5):")
    for i in range(5):
        print(f"  {i}", end=" ")
    print()
    
    # 리스트 컴프리헨션이 for문보다 빠르고 Pythonic!
    print("\nList comprehension (더 Pythonic!):")
    upper_fruits = [f.upper() for f in fruits]
    print(f"  {upper_fruits}")


# =============================================================================
# 5️⃣ 함수 비교
# =============================================================================

def functions_comparison() -> None:
    """
    함수 정의 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - def 키워드 사용
        - 반환 타입 명시 불필요 (타입 힌트로 명시 가능)
        - 기본 인자, 키워드 인자 지원
        - *args, **kwargs로 가변 인자
    """
    print("\n📌 함수")
    print("-" * 50)
    
    # Java: public int add(int a, int b) { return a + b; }
    # Go:   func add(a, b int) int { return a + b }
    # Python:
    def add(a: int, b: int) -> int:
        return a + b
    
    print(f"add(10, 20) = {add(10, 20)}")
    
    # 기본 인자 (Java에 없음, Go에 없음, Kotlin에 있음)
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"
    
    print(f"greet('Alice') = {greet('Alice')}")
    print(f"greet('Bob', 'Hi') = {greet('Bob', 'Hi')}")
    
    # 키워드 인자 (명시적 인자 전달)
    print(f"greet(greeting='Hey', name='Charlie') = {greet(greeting='Hey', name='Charlie')}")
    
    # 다중 반환 (Go와 유사!)
    def get_name_and_age() -> tuple[str, int]:
        return "Alice", 25
    
    name, age = get_name_and_age()  # unpacking
    print(f"\nMultiple return: name={name}, age={age}")
    
    # 일급 함수 (함수를 변수처럼!)
    # Java에서는 함수형 인터페이스 필요, Go는 지원
    operation = add
    print(f"\nFirst-class function: operation(5, 3) = {operation(5, 3)}")
    
    # 람다 (Java의 람다, Go의 익명 함수)
    multiply = lambda x, y: x * y
    print(f"Lambda: multiply(4, 5) = {multiply(4, 5)}")


# =============================================================================
# 6️⃣ 클래스 비교
# =============================================================================

def classes_comparison() -> None:
    """
    클래스 정의 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - __init__이 생성자 역할
        - self가 Java의 this
        - getter/setter 대신 @property
        - 접근 제어자 없음 (관례적으로 _ 사용)
    """
    print("\n📌 클래스")
    print("-" * 50)
    
    # Java 스타일 (장황함)
    # public class User {
    #     private String name;
    #     private int age;
    #     public User(String name, int age) { ... }
    #     public String getName() { return name; }
    # }
    
    # Python 스타일
    class User:
        def __init__(self, name: str, age: int) -> None:
            self.name = name  # public
            self._age = age   # protected (관례)
        
        @property
        def age(self) -> int:
            """getter 역할"""
            return self._age
        
        @age.setter
        def age(self, value: int) -> None:
            """setter 역할"""
            if value < 0:
                raise ValueError("Age cannot be negative")
            self._age = value
        
        def __str__(self) -> str:
            """Java의 toString()"""
            return f"User(name={self.name}, age={self._age})"
    
    user = User("Alice", 25)
    print(f"User: {user}")
    print(f"user.name = {user.name}")
    print(f"user.age = {user.age}")
    
    # @dataclass (Kotlin의 data class와 유사!)
    from dataclasses import dataclass
    
    @dataclass
    class Point:
        x: float
        y: float
    
    p1 = Point(10, 20)
    p2 = Point(10, 20)
    print(f"\ndataclass: {p1}")
    print(f"p1 == p2: {p1 == p2}")  # 자동 __eq__ 생성!


# =============================================================================
# 7️⃣ 에러 처리 비교
# =============================================================================

def error_handling_comparison() -> None:
    """
    에러 처리 비교.
    
    💡 다른 언어 개발자를 위한 팁:
        - try-except-finally (try-catch-finally)
        - raise (throw)
        - Go 스타일 에러 반환도 가능
    """
    print("\n📌 에러 처리")
    print("-" * 50)
    
    # Java: try { ... } catch (Exception e) { ... } finally { ... }
    # Go:   if err != nil { return err }
    # Python:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
    finally:
        print("Finally block executed")
    
    # 커스텀 예외
    class ValidationError(Exception):
        pass
    
    def validate_age(age: int) -> int:
        if age < 0:
            raise ValidationError("Age cannot be negative")
        return age
    
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"Validation failed: {e}")
    
    # Go 스타일: 예외 대신 튜플 반환
    def divide_safe(a: int, b: int) -> tuple[float | None, str | None]:
        if b == 0:
            return None, "division by zero"
        return a / b, None
    
    result, err = divide_safe(10, 0)
    if err:
        print(f"Go-style error: {err}")


# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    print("=" * 60)
    print("📌 Python 문법 비교 - Java/Go/Kotlin 개발자를 위한 가이드")
    print("=" * 60)
    
    variable_declaration()
    collections_comparison()
    conditionals_comparison()
    loops_comparison()
    functions_comparison()
    classes_comparison()
    error_handling_comparison()
    
    print("\n" + "=" * 60)
    print("✅ 문법 비교 완료!")
    print("=" * 60)
    print("\n💡 핵심 정리:")
    print("  1. 타입 선언 불필요 (동적 타이핑)")
    print("  2. 들여쓰기가 문법 (중괄호 없음)")
    print("  3. 리스트 컴프리헨션이 Pythonic")
    print("  4. @dataclass로 보일러플레이트 제거")
    print("  5. @property로 getter/setter 대체")


if __name__ == "__main__":
    main()

