# 🎯 Python Examples 프로젝트 개선 프롬프트

> 이 문서는 AI에게 프로젝트 개선을 요청할 때 사용할 수 있는 최적화된 프롬프트입니다.

---

## 프로젝트 개요

이 프로젝트는 **Java/Go/Kotlin/TypeScript 등 다른 언어를 이미 숙지한 개발자**가 
**Python을 빠르게 학습**하기 위한 예제 중심 교육 자료입니다.

---

## 🚀 메인 프롬프트

```markdown
당신은 Python/Go/Java/Kotlin에 정통한 10년차 백엔드 시니어 엔지니어입니다.

## 프로젝트 목표
- 대상: Java/Go/Kotlin/TypeScript 등 1개 이상의 언어를 숙지한 개발자
- 목적: Python을 "빠르게" 학습하여 실무에 투입 가능한 수준 도달
- 방식: 다른 언어와의 비교 + 예제 실행 + 함정 회피

## 핵심 원칙

### 1. "다른 언어 대비" 관점 필수
모든 예제에서 Java/Go/Kotlin 개발자가 헷갈리는 부분을 명시합니다:
- Python은 이렇게 동작하지만, Java에서는...
- Go와 달리 Python은...
- Kotlin의 data class vs Python의 dataclass

### 2. "왜?"를 설명
단순 문법이 아닌, 왜 그렇게 설계되었는지:
- GIL이 존재하는 이유
- 왜 Python은 멀티스레딩보다 멀티프로세싱을 권장하는가
- 왜 @property 데코레이터가 getter/setter보다 권장되는가

### 3. "실수하기 쉬운 패턴" 강조
다른 언어 습관이 Python에서 문제가 되는 케이스:
- 가변 기본 인자 함정 (def func(items=[]))
- 클래스 변수 vs 인스턴스 변수 혼동
- is vs == 차이
- 얕은 복사/깊은 복사 문제
- 순환 참조와 GC
- 클로저의 late binding 문제

### 4. 성능 관점 필수 포함
Python의 성능 특성을 명확히:
- 왜 list comprehension이 for문보다 빠른가
- generator vs list 메모리 차이
- dict 조회가 O(1)인 이유 (hash table)
- __slots__으로 메모리 절약하는 방법

### 5. Pythonic 관용구 (Idioms)
다른 언어 스타일이 아닌 Python다운 코드:
- EAFP vs LBYL
- 덕 타이핑 (Duck Typing)
- with문 활용
- unpacking 활용

## 폴더 구조 제안

```
📁 python-examples/
├── 00-quick-start/           # 10분 안에 Python 핵심 파악
│   ├── README.md            # "다른 언어 vs Python" 빠른 비교표
│   ├── 01_syntax_comparison.py   # Java/Go/Kotlin 문법 비교
│   └── 02_quick_tour.py         # Python 핵심 기능 투어
│
├── 01-pythonic-basics/       # Python다운 기초 (타 언어와 비교)
│   ├── README.md
│   ├── 01_variables_vs_java.py      # 동적 타이핑 vs 정적 타이핑
│   ├── 02_collections_comparison.py # List/Dict vs ArrayList/HashMap
│   ├── 03_functions_as_objects.py   # 일급 함수 (Java에는 없는)
│   ├── 04_comprehensions.py         # List/Dict/Set Comprehension
│   └── 05_unpacking_magic.py        # *args, **kwargs, unpacking
│
├── 02-python-gotchas/        # ⚠️ 실수하기 쉬운 패턴 (중요!)
│   ├── README.md
│   ├── 01_mutable_default_args.py   # def func(items=[]) 함정
│   ├── 02_class_vs_instance_vars.py # 클래스 변수 공유 문제
│   ├── 03_is_vs_equals.py           # is vs == 차이
│   ├── 04_late_binding_closures.py  # 클로저 late binding
│   ├── 05_shallow_vs_deep_copy.py   # 복사 문제
│   ├── 06_variable_scope_leaking.py # for문 변수 누출
│   └── 07_circular_reference.py     # 순환 참조와 메모리 누수
│
├── 03-memory-and-gc/         # 메모리 관리 & GC (심화)
│   ├── README.md
│   ├── 01_reference_counting.py     # 참조 카운팅 동작
│   ├── 02_cyclic_gc.py              # 순환 GC 동작
│   ├── 03_gc_tuning.py              # GC 설정 조정
│   ├── 04_memory_profiling.py       # 메모리 프로파일링
│   ├── 05_slots_optimization.py     # __slots__ 메모리 최적화
│   └── 06_weakref_patterns.py       # weakref 활용
│
├── 04-concurrency/           # 동시성 (Java/Go 개발자 주목!)
│   ├── README.md
│   ├── 01_gil_explained.py          # GIL이란? (Java와 가장 큰 차이)
│   ├── 02_threading_limitations.py  # 스레딩의 한계
│   ├── 03_multiprocessing.py        # 멀티프로세싱
│   ├── 04_asyncio_basics.py         # async/await (Go goroutine 비교)
│   ├── 05_asyncio_patterns.py       # 실무 async 패턴
│   └── 06_concurrent_futures.py     # ThreadPool/ProcessPool
│
├── 05-type-hints/            # 타입 힌트 (정적 타입 언어 출신자용)
│   ├── README.md
│   ├── 01_basic_type_hints.py       # 기본 타입 힌트
│   ├── 02_generic_types.py          # Generic (Java Generics 비교)
│   ├── 03_protocol_vs_interface.py  # Protocol vs Java Interface
│   ├── 04_typing_patterns.py        # 실무 타이핑 패턴
│   └── 05_mypy_strict_mode.py       # mypy로 컴파일 타임 체크
│
├── 06-oop-patterns/          # OOP (Java/Kotlin 개발자용)
│   ├── README.md
│   ├── 01_class_basics.py           # 클래스 기초
│   ├── 02_dunder_methods.py         # __init__, __str__, __eq__ 등
│   ├── 03_dataclasses.py            # @dataclass (Kotlin data class)
│   ├── 04_inheritance_vs_composition.py
│   ├── 05_abstract_vs_protocol.py   # ABC vs Protocol
│   └── 06_descriptors.py            # 디스크립터 (고급)
│
├── 07-functional/            # 함수형 프로그래밍
│   ├── README.md
│   ├── 01_first_class_functions.py  # 일급 함수
│   ├── 02_lambda_and_closures.py    # 람다 & 클로저
│   ├── 03_map_filter_reduce.py      # 함수형 도구
│   ├── 04_functools_patterns.py     # functools 활용
│   └── 05_itertools_patterns.py     # itertools 활용
│
├── 08-testing/               # 테스팅 (pytest)
│   ├── README.md
│   ├── 01_pytest_basics.py
│   ├── 02_fixtures.py
│   ├── 03_mocking.py
│   ├── 04_parametrize.py
│   └── 05_async_testing.py
│
├── 09-backend-patterns/      # 백엔드 실무 패턴
│   ├── README.md
│   ├── 01_fastapi_basics.py
│   ├── 02_pydantic_validation.py
│   ├── 03_dependency_injection.py
│   ├── 04_repository_pattern.py
│   ├── 05_clean_architecture.py
│   └── 06_error_handling.py
│
├── 10-performance/           # 성능 최적화
│   ├── README.md
│   ├── 01_profiling_tools.py        # cProfile, line_profiler
│   ├── 02_list_vs_generator.py      # 메모리 효율
│   ├── 03_dict_performance.py       # dict 최적화
│   ├── 04_string_performance.py     # 문자열 연결 최적화
│   └── 05_cython_intro.py           # Cython 소개
│
└── 99-cheatsheets/           # 빠른 참조
    ├── syntax_cheatsheet.md         # 문법 치트시트
    ├── stdlib_cheatsheet.md         # 표준 라이브러리
    ├── gotchas_cheatsheet.md        # 함정 모음
    └── performance_cheatsheet.md    # 성능 팁
```

## 각 예제 파일 템플릿

모든 예제 파일은 다음 구조를 따릅니다:

```python
"""
[파일명] - [제목]

📌 핵심 개념: (1-2문장)

🔄 다른 언어 비교:
- Java: ...
- Go: ...
- Kotlin: ...

⚠️ 주의사항: (실수하기 쉬운 부분)

📚 참고: (공식 문서 링크)
"""

from __future__ import annotations  # Python 3.12+ 스타일
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import ...

# =============================================================================
# 1️⃣ 개념 설명 (간결하게)
# =============================================================================

def concept_demo() -> None:
    """
    개념 설명용 데모.
    
    💡 Java/Go 개발자를 위한 팁:
        - Java에서는 이렇게 하지만, Python에서는...
        - Go와 달리 Python은...
    """
    pass

# =============================================================================
# 2️⃣ 실제 사용 예시
# =============================================================================

def practical_example() -> None:
    """실무에서 자주 사용하는 패턴."""
    pass

# =============================================================================
# 3️⃣ ⚠️ 함정 (Gotcha) - 다른 언어 습관으로 실수하기 쉬운 부분
# =============================================================================

def common_mistake() -> None:
    """
    ❌ 잘못된 패턴 (다른 언어 습관)
    """
    pass

def correct_pattern() -> None:
    """
    ✅ 올바른 Python 패턴
    """
    pass

# =============================================================================
# 4️⃣ 성능 비교 (선택)
# =============================================================================

def performance_comparison() -> None:
    """성능 차이를 보여주는 예시."""
    import timeit
    # ...

# =============================================================================
# 메인 실행
# =============================================================================

def main() -> None:
    """예제 실행."""
    print("=" * 60)
    print("📌 [제목]")
    print("=" * 60)
    
    concept_demo()
    practical_example()
    
    print("\n⚠️ 함정 (Gotcha):")
    common_mistake()
    correct_pattern()

if __name__ == "__main__":
    main()
```

## README.md 템플릿

각 폴더의 README.md:

```markdown
# [섹션 번호]. [제목]

> 💡 **Java/Go/Kotlin 개발자를 위한 핵심:**
> Python에서는 [핵심 차이점] 이 다르게 동작합니다.

## 🎯 학습 목표

1. [목표 1]
2. [목표 2]

## 🔄 다른 언어와 비교

| 개념 | Java | Go | Python |
|------|------|-----|--------|
| 예시 | ... | ... | ... |

## 📚 예제 목록

| 파일 | 설명 | 난이도 | 소요시간 |
|------|------|--------|----------|
| 01_xxx.py | ... | ⭐ | 5분 |
| 02_xxx.py | ... | ⭐⭐ | 10분 |

## ⚠️ 이 섹션에서 다루는 함정(Gotcha)

- [ ] 함정 1
- [ ] 함정 2

## 🚀 실행 방법

\```bash
python 01_xxx.py
\```

## 📖 추가 학습 자료

- [공식 문서](...)
- [PEP 링크](...)
```

## 작업 요청

위 구조와 템플릿을 기반으로 프로젝트를 개선해주세요.
작업 순서:
1. 기존 파일 분석 및 보존할 부분 식별
2. 새 폴더 구조 생성
3. 00-quick-start 섹션 먼저 완성
4. 02-python-gotchas 섹션 (가장 중요!)
5. 나머지 섹션 순차 작업
6. 치트시트 작성
7. 메인 README 업데이트

각 커밋은 섹션 단위로 분리해주세요.
```

---

## 🎯 섹션별 상세 프롬프트

### Quick Start 섹션

```markdown
00-quick-start 섹션을 작성해주세요.

목표: 10분 안에 Python의 핵심을 파악
대상: Java/Go/Kotlin 개발자

포함 내용:
1. README.md - 다른 언어 vs Python 빠른 비교표
   - 변수 선언, 타입, 컬렉션, 함수, 클래스, 에러 처리
   - 각각 Java/Go/Kotlin/Python 코드 비교

2. 01_syntax_comparison.py
   - 동일한 기능을 Java식, Go식, Python식으로 구현
   - Python 방식이 왜 더 간결한지 설명

3. 02_quick_tour.py
   - 5분 안에 실행하며 Python 핵심 기능 훑기
   - 리스트 컴프리헨션, 딕셔너리, 제너레이터, with문, 데코레이터
```

### Gotchas 섹션 (가장 중요)

```markdown
02-python-gotchas 섹션을 작성해주세요.

이 섹션은 다른 언어 개발자가 Python에서 가장 많이 실수하는 패턴을 다룹니다.

필수 포함:
1. 가변 기본 인자 함정
   - def func(items=[])가 왜 위험한가
   - Java에서는 이런 문제가 없는 이유
   - 해결 방법

2. 클래스 변수 vs 인스턴스 변수
   - 클래스 레벨에서 선언한 가변 객체 공유 문제
   - Java/Kotlin의 static과 다른 점

3. is vs ==
   - 작은 정수 캐싱 (-5 ~ 256)
   - 문자열 인터닝
   - None 체크는 왜 is를 사용하는가

4. Late Binding Closures
   - for 루프 안의 람다가 마지막 값만 참조하는 문제
   - JavaScript 개발자도 겪는 문제지만 해결법이 다름

5. 얕은 복사 vs 깊은 복사
   - 리스트 슬라이싱이 얕은 복사인 이유
   - copy vs deepcopy

6. 변수 스코프 누출
   - for문 루프 변수가 바깥에서 접근 가능
   - Python에는 block scope가 없다!

7. 순환 참조와 메모리
   - __del__이 호출되지 않는 경우
   - weakref로 해결하는 방법
```

### Memory & GC 섹션

```markdown
03-memory-and-gc 섹션을 작성해주세요.

JVM/Go 런타임과 CPython의 메모리 관리 차이를 명확히 합니다.

포함 내용:
1. 참조 카운팅 vs JVM GC
   - CPython은 Reference Counting + Cyclic GC
   - JVM은 Mark & Sweep 계열
   - 실시간 해제 vs 지연 해제의 차이

2. GC 동작 관측 실험
   - gc 모듈 활용
   - tracemalloc으로 메모리 추적

3. __slots__ 최적화
   - Java에는 없는 메모리 최적화 기법
   - 언제 사용해야 하는가

4. weakref 패턴
   - 캐시 구현
   - 옵저버 패턴
```

### Concurrency 섹션

```markdown
04-concurrency 섹션을 작성해주세요.

Java/Go 개발자가 가장 혼란스러워하는 부분입니다.

핵심 포인트:
1. GIL (Global Interpreter Lock)
   - Java 개발자: "왜 멀티스레드가 CPU 바운드에서 느린가?"
   - Go 개발자: "goroutine처럼 쓸 수 없는가?"
   - GIL의 존재 이유와 우회 방법

2. Threading의 한계와 적합한 사용처
   - I/O 바운드에서만 효과적
   - CPU 바운드는 multiprocessing

3. asyncio vs goroutine
   - 코루틴 동작 방식 비교
   - 이벤트 루프 개념

4. 실무 패턴
   - concurrent.futures 활용
   - aiohttp, asyncpg 등 async 라이브러리
```

---

## ✅ 체크리스트

프로젝트 완성 시 확인:

- [ ] 모든 예제가 실행 가능한가?
- [ ] Java/Go/Kotlin 비교가 포함되었는가?
- [ ] 함정(Gotcha)이 명확히 설명되었는가?
- [ ] 성능 관점이 포함되었는가?
- [ ] 타입 힌트가 일관되게 적용되었는가?
- [ ] README가 "10분 학습" 가능하게 작성되었는가?
- [ ] 치트시트가 유용한가?

---

## 📌 커밋 메시지 규칙

```
feat: add 00-quick-start section
feat: add 02-python-gotchas section
docs: update main README with learning path
refactor: reorganize folder structure
perf: add performance comparison examples
```

