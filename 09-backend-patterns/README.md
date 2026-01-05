# 09. Backend Patterns - 백엔드 실무 패턴

> 💡 **핵심:**
> FastAPI + Pydantic + SQLAlchemy는 Python 백엔드의 황금 조합입니다.
> Spring Boot나 Go의 패턴과 유사하게 Clean Architecture를 적용할 수 있습니다.

## 🔄 다른 언어와 비교

| 구분 | Spring Boot | Go | FastAPI |
|------|-------------|-----|---------|
| 프레임워크 | Spring MVC | Gin, Echo | FastAPI |
| ORM | JPA/Hibernate | GORM | SQLAlchemy |
| Validation | Bean Validation | go-playground | Pydantic |
| DI | Spring DI | wire, fx | Depends |

## 📚 예제 목록

| 파일 | 설명 | 난이도 |
|------|------|--------|
| 01_fastapi_basics.py | FastAPI 기초 | ⭐⭐ |
| 02_pydantic_validation.py | Pydantic 검증 | ⭐⭐ |
| 03_dependency_injection.py | 의존성 주입 | ⭐⭐⭐ |
| 04_repository_pattern.py | Repository 패턴 | ⭐⭐⭐ |

## 🚀 실행 방법

```bash
# 의존성 설치
pip install fastapi uvicorn pydantic sqlalchemy

# 서버 실행
uvicorn 01_fastapi_basics:app --reload
```

