# Python 성능 최적화 치트시트

> 자주 사용하는 성능 팁과 패턴

## 리스트 vs 제너레이터

```python
# ❌ 메모리 많이 사용
squares = [x**2 for x in range(1000000)]

# ✅ 메모리 효율적
squares = (x**2 for x in range(1000000))
```

| 방식 | 메모리 | 사용 시점 |
|------|--------|----------|
| 리스트 | O(n) | 여러 번 순회, 인덱싱 필요 |
| 제너레이터 | O(1) | 한 번만 순회, 대용량 |

---

## 문자열 연결

```python
# ❌ 느림 (O(n²))
s = ""
for item in items:
    s += str(item)

# ✅ 빠름 (O(n))
s = "".join(str(item) for item in items)

# ✅ f-string (가장 빠름)
s = f"{name}: {value}"
```

---

## 딕셔너리 조회

```python
# ❌ 두 번 조회
if key in d:
    value = d[key]

# ✅ 한 번 조회
value = d.get(key)
if value is not None:
    ...

# ✅ 기본값과 함께
value = d.get(key, default)

# ✅ setdefault (없으면 생성)
d.setdefault(key, []).append(item)
```

---

## 멤버십 테스트

```python
# ❌ 리스트: O(n)
if item in large_list:
    ...

# ✅ 셋: O(1)
large_set = set(large_list)
if item in large_set:
    ...
```

---

## __slots__ 메모리 최적화

```python
# 일반 클래스: 인스턴스당 __dict__ (동적)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# __slots__: 인스턴스당 고정 메모리 (20-30% 절약)
class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# dataclass with slots
@dataclass(slots=True)
class Point:
    x: float
    y: float
```

---

## 리스트 컴프리헨션 vs for 루프

```python
# for 루프
result = []
for x in range(1000):
    result.append(x ** 2)

# 리스트 컴프리헨션 (약 30% 빠름)
result = [x ** 2 for x in range(1000)]
```

**왜 빠른가?**
- 컴프리헨션은 최적화된 바이트코드
- append() 메서드 조회 오버헤드 없음

---

## 함수 캐싱

```python
from functools import lru_cache

# 반복 호출 캐싱
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 캐시 정보 확인
fibonacci.cache_info()

# 캐시 초기화
fibonacci.cache_clear()
```

---

## 지역 변수가 전역보다 빠름

```python
# ❌ 전역 변수 조회
import math
def calc():
    return math.sqrt(x)  # 매번 math 조회

# ✅ 지역 변수로 캐싱
def calc():
    sqrt = math.sqrt  # 한 번만 조회
    return sqrt(x)
```

---

## in 연산자 최적화

```python
# ❌ 여러 or 조건
if x == 'a' or x == 'b' or x == 'c':
    ...

# ✅ in 사용 (더 읽기 쉽고 빠름)
if x in ('a', 'b', 'c'):  # tuple이 set보다 작은 경우 빠름
    ...

if x in {'a', 'b', 'c', 'd', 'e'}:  # 많으면 set
    ...
```

---

## 프로파일링 도구

```python
# cProfile (내장)
import cProfile
cProfile.run('my_function()')

# line_profiler
@profile
def my_function():
    ...
# kernprof -l -v script.py

# memory_profiler
@profile
def my_function():
    ...
# python -m memory_profiler script.py

# timeit
import timeit
timeit.timeit('func()', number=10000)
```

---

## 성능 체크리스트

| 항목 | 확인 |
|------|------|
| 대용량 데이터 | 제너레이터 사용? |
| 문자열 연결 | join() 사용? |
| 반복 조회 | 딕셔너리/셋 사용? |
| 많은 인스턴스 | __slots__ 사용? |
| 반복 계산 | @lru_cache 사용? |
| 프로파일링 | 병목 지점 확인? |

