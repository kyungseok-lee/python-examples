# 00. Quick Start - 10분 Python 핵심 투어

> 💡 **Java/Go/Kotlin 개발자를 위한 핵심:**
> Python은 동적 타이핑, 덕 타이핑, 간결한 문법이 특징입니다.
> 이 섹션에서 10분 안에 Python의 핵심을 파악할 수 있습니다.

## 🎯 학습 목표

1. Python 문법의 핵심 차이점 이해
2. 다른 언어와의 빠른 비교
3. Python만의 강력한 기능 체험

## 🔄 다른 언어와 빠른 비교

### 변수 선언

| Java | Go | Kotlin | Python |
|------|-----|--------|--------|
| `int x = 10;` | `var x int = 10` | `val x: Int = 10` | `x = 10` |
| `String s = "hi";` | `s := "hi"` | `val s = "hi"` | `s = "hi"` |
| 타입 필수 | 타입 추론 가능 | 타입 추론 가능 | **타입 선언 불필요** |

### 컬렉션

| Java | Go | Python |
|------|-----|--------|
| `List<Integer> list = new ArrayList<>();` | `list := []int{}` | `list = []` |
| `Map<String, Integer> map = new HashMap<>();` | `m := map[string]int{}` | `d = {}` |
| `list.add(1);` | `list = append(list, 1)` | `list.append(1)` |

### Null/None 체크

| Java | Go | Kotlin | Python |
|------|-----|--------|--------|
| `if (x != null)` | `if x != nil` | `x?.let {}` | `if x is not None:` |
| `Optional<T>` | 에러 반환 | `T?` | `T \| None` |

### 함수 정의

| Java | Go | Python |
|------|-----|--------|
| `public int add(int a, int b) { return a + b; }` | `func add(a, b int) int { return a + b }` | `def add(a, b): return a + b` |

### 클래스

| Java | Kotlin | Python |
|------|--------|--------|
| `public class User { ... }` | `data class User(...)` | `@dataclass class User:` |
| getter/setter 필요 | 자동 생성 | `@property` 데코레이터 |

## 📚 예제 목록

| 파일 | 설명 | 소요시간 |
|------|------|----------|
| `01_syntax_comparison.py` | Java/Go/Kotlin과 Python 문법 비교 | 5분 |
| `02_quick_tour.py` | Python 핵심 기능 빠른 투어 | 5분 |

## ⚠️ 처음부터 알아야 할 Python 특징

1. **들여쓰기가 문법이다** - 중괄호 `{}` 대신 들여쓰기로 블록 구분
2. **세미콜론 없음** - 줄바꿈이 문장 끝
3. **동적 타이핑** - 변수 타입이 런타임에 결정
4. **모든 것이 객체** - 함수도 객체 (일급 시민)
5. **GIL 존재** - 멀티스레딩이 Java/Go와 다르게 동작

## 🚀 실행 방법

```bash
cd 00-quick-start

# 문법 비교 예제
python 01_syntax_comparison.py

# 핵심 기능 투어
python 02_quick_tour.py
```

## 📖 추가 학습 자료

- [Python 공식 튜토리얼](https://docs.python.org/3/tutorial/)
- [Python for Java Developers](https://realpython.com/java-vs-python/)
- [Go vs Python](https://realpython.com/python-vs-go/)

