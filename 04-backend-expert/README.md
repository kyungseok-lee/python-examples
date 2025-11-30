# 04. 백엔드 전문가 (Backend Expert)

실전 백엔드 개발에 필요한 모든 기술을 마스터합니다.

## 📚 학습 내용

### API 개발
- **01_fastapi_basics**: FastAPI 기본, 라우팅, 요청/응답
- **02_pydantic_models**: 데이터 검증, BaseModel
- **03_dependency_injection**: Depends, 의존성 주입
- **04_middleware**: 미들웨어, CORS, 인증

### 데이터베이스
- **05_sqlalchemy_basics**: SQLAlchemy ORM 기본
- **06_database_patterns**: Repository 패턴, Unit of Work

### 아키텍처
- **07_clean_architecture**: 계층 분리, 의존성 역전
- **08_ddd_patterns**: Entity, Value Object, Aggregate

### 보안 & 인증
- **09_jwt_auth**: JWT 토큰, 인증/인가

### 배포
- **10_docker**: Dockerfile, docker-compose

## 🚀 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 각 예제 실행
python 01_fastapi_basics.py
uvicorn 01_fastapi_basics:app --reload

# Docker 빌드 및 실행
docker build -t python-backend .
docker-compose up
```

## 📝 실무 팁

- FastAPI는 자동 API 문서(/docs)를 제공합니다
- Pydantic으로 데이터 검증을 자동화하세요
- Clean Architecture로 테스트 가능한 코드를 작성하세요
- Docker로 일관된 개발/배포 환경을 유지하세요

