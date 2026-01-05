# 02. Python Gotchas - 실수하기 쉬운 함정 모음

> ⚠️ **Java/Go/Kotlin 개발자 필독!**
> 다른 언어의 습관이 Python에서 버그를 유발하는 대표적인 케이스들입니다.
> 이 섹션을 먼저 읽으면 수많은 디버깅 시간을 절약할 수 있습니다.

## 🎯 학습 목표

1. Python에서 흔히 발생하는 버그 패턴 인식
2. 다른 언어 습관이 문제가 되는 이유 이해
3. 올바른 Python 패턴 습득

## ⚠️ Top 7 Python 함정

| # | 함정 | 위험도 | 다른 언어에서 문제 없는 이유 |
|---|------|--------|------------------------------|
| 1 | 가변 기본 인자 | 🔴 치명적 | Java/Go는 매 호출마다 새 객체 생성 |
| 2 | 클래스 변수 공유 | 🔴 치명적 | Java static과 다른 동작 |
| 3 | is vs == | 🟠 중요 | Java에서는 ==가 참조 비교 |
| 4 | Late Binding Closures | 🟠 중요 | JavaScript에서도 발생하지만 해결법 다름 |
| 5 | 얕은 복사 문제 | 🟡 주의 | 대부분 언어에서 발생하지만 Python이 더 빈번 |
| 6 | 변수 스코프 누출 | 🟡 주의 | 대부분 언어에 block scope 있음 |
| 7 | 순환 참조 | 🟡 주의 | JVM GC가 더 적극적으로 처리 |

## 📚 예제 목록

| 파일 | 설명 | 난이도 | 소요시간 |
|------|------|--------|----------|
| `01_mutable_default_args.py` | 가변 기본 인자 함정 | ⭐⭐⭐ | 5분 |
| `02_class_vs_instance_vars.py` | 클래스 변수 vs 인스턴스 변수 | ⭐⭐⭐ | 5분 |
| `03_is_vs_equals.py` | is vs == 차이 | ⭐⭐ | 5분 |
| `04_late_binding_closures.py` | 클로저 Late Binding | ⭐⭐ | 5분 |
| `05_shallow_vs_deep_copy.py` | 얕은 복사 vs 깊은 복사 | ⭐⭐ | 5분 |
| `06_variable_scope_leaking.py` | 변수 스코프 누출 | ⭐ | 3분 |
| `07_circular_reference.py` | 순환 참조와 메모리 | ⭐⭐ | 5분 |

## 🚀 실행 방법

```bash
cd 02-python-gotchas

# 각 함정 예제 실행
python 01_mutable_default_args.py
python 02_class_vs_instance_vars.py
# ... 등등

# 모든 예제 한번에 실행
python -c "import os; [os.system(f'python {f}') for f in sorted(os.listdir('.')) if f.endswith('.py')]"
```

## 📖 추가 학습 자료

- [Python Common Gotchas](https://docs.python-guide.org/writing/gotchas/)
- [Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- [Fluent Python (책)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)

