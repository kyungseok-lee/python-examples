# Python 문법 치트시트

> Java/Go/Kotlin 개발자를 위한 빠른 참조

## 변수와 타입

```python
# 변수 선언 (타입 선언 불필요)
x = 10
name = "Python"
is_active = True

# 타입 힌트 (선택)
x: int = 10
name: str = "Python"
```

| Java | Python |
|------|--------|
| `int x = 10;` | `x = 10` |
| `String s = "hi";` | `s = "hi"` |
| `final int X = 10;` | `X = 10` (관례만) |

## 기본 타입

```python
# 숫자
x = 10          # int (무한 정밀도!)
y = 3.14        # float
z = 1 + 2j      # complex

# 문자열
s = "hello"
s = 'hello'
s = """multi
line"""
f"Hello {name}"  # f-string (포맷팅)

# 불리언
True, False

# None (Java의 null)
x = None
```

## 컬렉션

```python
# 리스트 (ArrayList)
nums = [1, 2, 3]
nums.append(4)
nums[0]  # 첫 번째
nums[-1]  # 마지막

# 튜플 (불변 리스트)
point = (10, 20)
x, y = point  # 언패킹

# 딕셔너리 (HashMap)
ages = {"Alice": 25, "Bob": 30}
ages["Alice"]
ages.get("Charlie", 0)  # 기본값

# 셋 (HashSet)
unique = {1, 2, 3}
```

## 조건문

```python
# if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# 삼항 연산자
result = "Pass" if score >= 60 else "Fail"

# match (Python 3.10+)
match status:
    case 200:
        msg = "OK"
    case 404:
        msg = "Not Found"
    case _:
        msg = "Unknown"
```

## 반복문

```python
# for-each
for item in items:
    print(item)

# with index
for i, item in enumerate(items):
    print(i, item)

# range
for i in range(5):       # 0, 1, 2, 3, 4
for i in range(1, 5):    # 1, 2, 3, 4
for i in range(0, 10, 2): # 0, 2, 4, 6, 8

# while
while condition:
    ...

# 컴프리헨션 (★ Pythonic!)
squares = [x**2 for x in range(10)]
evens = [x for x in nums if x % 2 == 0]
```

## 함수

```python
# 기본 함수
def add(a: int, b: int) -> int:
    return a + b

# 기본 인자
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# 가변 인자
def sum_all(*args: int) -> int:
    return sum(args)

def print_info(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# 람다
square = lambda x: x ** 2
```

## 클래스

```python
class User:
    # 클래스 변수
    count: int = 0
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name  # 인스턴스 변수
        self._age = age   # protected (관례)
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    def __str__(self) -> str:
        return f"User({self.name})"
    
    @classmethod
    def create(cls, name: str) -> "User":
        return cls(name, 0)
    
    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name) > 0
```

## dataclass (★ 권장)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass(frozen=True)  # 불변
class ImmutablePoint:
    x: float
    y: float

@dataclass(slots=True)  # 메모리 최적화
class OptimizedPoint:
    x: float
    y: float
```

## 에러 처리

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unknown error: {e}")
else:
    print("Success")  # 예외 없을 때
finally:
    print("Always executed")

# 예외 발생
raise ValueError("Invalid value")

# 커스텀 예외
class CustomError(Exception):
    pass
```

## 컨텍스트 매니저

```python
# 파일 처리
with open("file.txt", "r") as f:
    content = f.read()

# 여러 리소스
with open("a.txt") as f1, open("b.txt") as f2:
    ...
```

## 타입 힌트

```python
from typing import Optional, Union

# 기본
def func(x: int, y: str) -> bool:
    ...

# Optional (None 가능)
def find(id: int) -> Optional[User]:  # User | None
    ...

# Union
def process(x: Union[int, str]) -> None:  # int | str
    ...

# 컬렉션
def func(items: list[int]) -> dict[str, int]:
    ...

# Python 3.10+
def func(x: int | str) -> User | None:
    ...
```

## 유용한 내장 함수

```python
len(items)          # 길이
range(10)           # 0~9
enumerate(items)    # (index, item) 쌍
zip(a, b)           # 두 리스트 병렬 순회
map(func, items)    # 모든 원소에 func 적용
filter(pred, items) # 조건에 맞는 원소만
sorted(items)       # 정렬된 새 리스트
any(items)          # 하나라도 True?
all(items)          # 모두 True?
```

