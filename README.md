# 🐍 Python Examples for Experienced Developers

> **Java/Go/Kotlin/TypeScript 개발자를 위한 Python 빠른 학습 가이드**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 이 프로젝트는 누구를 위한 것인가?

- ✅ Java, Go, Kotlin, TypeScript 중 **1개 이상의 언어를 이미 숙지**한 개발자
- ✅ Python을 **빠르게** 학습하여 실무에 투입하고 싶은 개발자
- ✅ 다른 언어 습관으로 인한 **Python 함정(Gotcha)** 을 피하고 싶은 개발자
- ✅ **Pythonic**한 코드를 작성하고 싶은 개발자

---

## 🚀 빠른 시작 (10분)

```bash
# 1. 저장소 클론
git clone https://github.com/your-username/python-examples.git
cd python-examples

# 2. 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Quick Start 예제 실행
cd 00-quick-start
python 01_syntax_comparison.py
python 02_quick_tour.py
```

---

## 📚 학습 로드맵

### Phase 1: 기초 (1-2시간)
| 순서 | 섹션 | 설명 | 소요시간 |
|------|------|------|----------|
| 1 | [00-quick-start](./00-quick-start/) | Python 핵심 10분 파악 | 10분 |
| 2 | [01-pythonic-basics](./01-pythonic-basics/) | Python다운 기초 문법 | 30분 |
| 3 | [02-python-gotchas](./02-python-gotchas/) | ⚠️ **필독!** 실수하기 쉬운 패턴 | 30분 |

### Phase 2: 심화 (2-3시간)
| 순서 | 섹션 | 설명 | 소요시간 |
|------|------|------|----------|
| 4 | [03-memory-and-gc](./03-memory-and-gc/) | 메모리 관리 & GC | 30분 |
| 5 | [04-concurrency](./04-concurrency/) | 동시성 (GIL, asyncio) | 45분 |
| 6 | [05-type-hints](./05-type-hints/) | 타입 힌트 | 30분 |

### Phase 3: 패턴 & 실무 (2-3시간)
| 순서 | 섹션 | 설명 | 소요시간 |
|------|------|------|----------|
| 7 | [06-oop-patterns](./06-oop-patterns/) | OOP 패턴 | 30분 |
| 8 | [07-functional](./07-functional/) | 함수형 프로그래밍 | 30분 |
| 9 | [08-testing](./08-testing/) | pytest 테스팅 | 30분 |
| 10 | [09-backend-patterns](./09-backend-patterns/) | 백엔드 실무 패턴 | 45분 |
| 11 | [10-performance](./10-performance/) | 성능 최적화 | 30분 |

### 빠른 참조
- [99-cheatsheets](./99-cheatsheets/) - 문법, 함정, 성능 치트시트

---

## 🔄 다른 언어 vs Python 핵심 비교

| 개념 | Java | Go | Kotlin | Python |
|------|------|-----|--------|--------|
| 변수 선언 | `int x = 1;` | `x := 1` | `val x = 1` | `x = 1` |
| 타입 시스템 | 정적 | 정적 | 정적 | 동적 (힌트 가능) |
| 컬렉션 | `ArrayList<String>` | `[]string{}` | `listOf()` | `list()` / `[]` |
| 널 처리 | `Optional<T>` | 제로값 | `?.` / `?:` | `None` / `Optional` |
| 동시성 | Thread, Executor | goroutine | coroutine | **GIL** / asyncio |
| 패키지 관리 | Maven/Gradle | go mod | Gradle | pip / poetry |
| 엔트리포인트 | `main()` | `main()` | `main()` | `if __name__ == "__main__":` |

---

## ⚠️ Java/Go/Kotlin 개발자가 가장 많이 하는 실수 TOP 7

1. **가변 기본 인자** - `def func(items=[])` → 모든 호출이 같은 리스트 공유!
2. **클래스 변수 공유** - 인스턴스 간 가변 클래스 변수 공유 문제
3. **is vs ==** - 작은 정수 캐싱으로 인한 혼란
4. **Late Binding Closures** - 루프 안 람다가 마지막 값만 참조
5. **얕은 복사** - 리스트 슬라이싱은 얕은 복사!
6. **변수 스코프 누출** - for문 변수가 바깥에서 접근 가능
7. **GIL** - 멀티스레드가 CPU 바운드에서 느린 이유

👉 자세한 내용: [02-python-gotchas](./02-python-gotchas/)

---

## 🛠️ 개발 환경 설정

### 필수 요구사항
- Python 3.12+
- pip 또는 poetry

### 권장 IDE 설정
```bash
# VS Code 확장
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance

# 린터/포매터 설치
pip install ruff mypy
```

### 프로젝트 의존성
```bash
pip install -r requirements.txt
```

---

## 📖 참고 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [PEP 8 - 스타일 가이드](https://pep8.org/)
- [Real Python](https://realpython.com/)
- [Python Design Patterns](https://python-patterns.guide/)

---

## 📄 라이선스

MIT License - 자유롭게 사용하세요!

