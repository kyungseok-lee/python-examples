# Python 함정(Gotchas) 치트시트

> ⚠️ 다른 언어 개발자가 자주 실수하는 패턴

## 🔴 1. 가변 기본 인자

```python
# ❌ 잘못됨 - 모든 호출이 같은 리스트 공유
def append_to(item, items=[]):
    items.append(item)
    return items

# ✅ 올바름
def append_to(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**왜?** Python은 함수 정의 시점에 기본 인자를 한 번만 평가

---

## 🔴 2. 클래스 변수 공유

```python
# ❌ 잘못됨 - 모든 인스턴스가 같은 리스트 공유
class Dog:
    tricks = []  # 클래스 변수!
    
    def add_trick(self, trick):
        self.tricks.append(trick)

# ✅ 올바름
class Dog:
    def __init__(self):
        self.tricks = []  # 인스턴스 변수

# ✅✅ 최선 (dataclass)
@dataclass
class Dog:
    tricks: list = field(default_factory=list)
```

**왜?** 클래스 본문의 변수는 Java의 static처럼 공유됨

---

## 🟠 3. is vs ==

```python
# 값 비교: ==
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True

# 동일성 비교: is
a is b  # False (다른 객체)

# None 체크는 is 사용
if x is None:
    ...

# ⚠️ 작은 정수 캐싱
a = 256
b = 256
a is b  # True (캐싱!)

a = 257
b = 257
a is b  # False!
```

**규칙:** None은 `is`, 숫자/문자열은 `==`

---

## 🟠 4. Late Binding Closures

```python
# ❌ 잘못됨 - 모두 마지막 값(4)
funcs = [lambda: i for i in range(5)]
[f() for f in funcs]  # [4, 4, 4, 4, 4]

# ✅ 올바름 - 기본 인자로 캡처
funcs = [lambda i=i: i for i in range(5)]
[f() for f in funcs]  # [0, 1, 2, 3, 4]
```

**왜?** 클로저는 변수 "참조"를 캡처, 실행 시점에 값을 읽음

---

## 🟡 5. 얕은 복사 vs 깊은 복사

```python
import copy

# 얕은 복사 (내부 객체 공유)
shallow = original.copy()
shallow = list(original)
shallow = original[:]

# 깊은 복사 (모든 객체 복사)
deep = copy.deepcopy(original)
```

```python
# ⚠️ 중첩 구조 주의
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0][0] = 999
# matrix도 변경됨! [[999, 2], [3, 4]]
```

---

## 🟡 6. 변수 스코프 누출

```python
# Python에는 블록 스코프가 없음!
for i in range(5):
    x = i

print(i)  # 4 (마지막 값)
print(x)  # 4

# Java에서는 i가 for문 밖에서 접근 불가
```

**해결:** 변수 미리 초기화, 함수로 분리

---

## 🟡 7. 순환 참조

```python
# ⚠️ 순환 참조 - GC까지 메모리에 남음
class Node:
    def __init__(self):
        self.neighbor = None

a = Node()
b = Node()
a.neighbor = b
b.neighbor = a  # 순환!

# ✅ weakref로 해결
import weakref

class Node:
    def __init__(self):
        self._neighbor = None
    
    @property
    def neighbor(self):
        return self._neighbor() if self._neighbor else None
    
    @neighbor.setter
    def neighbor(self, node):
        self._neighbor = weakref.ref(node) if node else None
```

---

## 빠른 점검 목록

| 패턴 | 검사 |
|------|------|
| `def func(x=[])` | 가변 기본 인자? |
| `class Foo: items = []` | 클래스 변수에 가변 객체? |
| `if x is 100` | is로 값 비교? |
| `lambda: i` in loop | 루프 안 람다? |
| `list.copy()` with nested | 중첩 구조 얕은 복사? |
| loop 후 변수 사용 | 스코프 누출? |
| 양방향 참조 | 순환 참조? |

