# 04. 백엔드 전문가 (Backend Expert)

실전 백엔드 개발에 필요한 핵심 기술을 마스터합니다.

## 📚 학습 내용

### API 개발
- **01_fastapi_basics**: FastAPI 기본, 라우팅, 요청/응답, 비동기 처리
- **02_pydantic_models**: Pydantic v2 데이터 검증, BaseModel, 시리얼라이제이션

### 아키텍처
- **03_clean_architecture**: 계층 분리, 의존성 역전 원칙, Protocol 기반 인터페이스

## 🚀 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# FastAPI 서버 실행
uvicorn 01_fastapi_basics:app --reload

# API 문서 확인
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)

# Clean Architecture 예제 실행
python 03_clean_architecture.py

# Docker 빌드 및 실행
docker build -t python-backend .
docker-compose up
```

## 📝 실무 팁

- FastAPI는 자동 API 문서(/docs)를 제공합니다
- Pydantic v2로 데이터 검증을 자동화하세요
- Clean Architecture로 테스트 가능한 코드를 작성하세요
- `__slots__`와 Protocol을 활용해 메모리/성능을 최적화하세요
- Docker로 일관된 개발/배포 환경을 유지하세요

## 🔧 기술 스택

- **FastAPI** 0.115+: 고성능 비동기 웹 프레임워크
- **Pydantic** v2.10+: 데이터 검증 및 설정 관리
- **Python** 3.12+: 최신 타입 힌트 문법 사용

