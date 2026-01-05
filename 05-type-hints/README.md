# 05. Type Hints - 타입 힌트

> 💡 **Java/Kotlin 개발자를 위한 핵심:**
> Python 타입 힌트는 **런타임에 강제되지 않습니다!**
> 정적 분석 도구(mypy)나 IDE 지원을 위한 것입니다.

## 🎯 학습 목표

1. 기본 타입 힌트 문법 습득
2. Generic 타입 활용
3. Protocol vs ABC 이해
4. mypy 활용법

## 🔄 다른 언어와 비교

| 구분 | Java | Kotlin | Python |
|------|------|--------|--------|
| 타이핑 | 정적, 강제 | 정적, 강제 | 동적, 힌트 |
| Null 안전성 | Optional | ?, !! | None \| T |
| 인터페이스 | interface | interface | Protocol, ABC |
| 제네릭 | <T> | <T> | [T] (3.9+) |

## 📚 예제 목록

| 파일 | 설명 | 난이도 | 소요시간 |
|------|------|--------|----------|
| [01_basic_type_hints.py](./01_basic_type_hints.py) | 기본 타입 힌트 | ⭐ | 10분 |
| [02_generic_types.py](./02_generic_types.py) | Generic 타입 | ⭐⭐ | 10분 |
| [03_protocol_vs_abc.py](./03_protocol_vs_abc.py) | Protocol과 ABC | ⭐⭐ | 10분 |

## 🚀 실행 방법

```bash
# mypy 설치
pip install mypy

# 타입 체크
mypy 01_basic_type_hints.py
```

## 📖 추가 학습 자료

- [typing 모듈](https://docs.python.org/3/library/typing.html)
- [mypy 문서](https://mypy.readthedocs.io/)

