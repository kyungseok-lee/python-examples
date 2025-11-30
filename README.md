# Python Backend Expert Learning Path

Python 백엔드 전문가가 되기 위한 체계적인 학습 프로젝트입니다.

## 📚 커리큘럼 구성

### 01. 기본 문법 (Basics)
Python의 기초를 탄탄히 다지는 단계입니다.

- **01_variables_and_types**: 변수, 기본 자료형, 타입 변환
- **02_operators**: 산술, 비교, 논리, 비트 연산자
- **03_control_flow**: if/elif/else, match-case
- **04_loops**: for, while, comprehensions
- **05_functions**: 함수 정의, 인자, 반환값, lambda
- **06_data_structures**: list, tuple, dict, set
- **07_strings**: 문자열 조작, 포매팅, 정규표현식
- **08_classes_basic**: 클래스, 인스턴스, 메서드, 상속

### 02. 중급 개념 (Intermediate)
실무에서 자주 사용하는 중급 기술을 학습합니다.

- **01_decorators**: 함수/클래스 데코레이터, wraps
- **02_generators**: yield, 제너레이터 표현식, 이터레이터
- **03_context_managers**: with문, contextlib
- **04_file_io**: 파일 읽기/쓰기, CSV, JSON
- **05_error_handling**: try-except, 커스텀 예외
- **06_modules_packages**: 모듈 구조, __init__.py, 패키지 관리
- **07_collections**: namedtuple, Counter, defaultdict, deque
- **08_datetime**: 날짜/시간 처리, timezone

### 03. 고급 개념 (Advanced)
Python의 심화 기능과 성능 최적화를 다룹니다.

- **01_async_programming**: async/await, asyncio, aiohttp
- **02_multithreading**: threading, concurrent.futures
- **03_multiprocessing**: Process, Pool, 프로세스 간 통신
- **04_metaclasses**: type, metaclass, 클래스 생성 제어
- **05_descriptors**: property, __get__/__set__/__delete__
- **06_type_hints**: typing, Protocol, Generic, TypeVar
- **07_dataclasses**: @dataclass, field, post_init
- **08_performance**: profiling, cProfile, memory_profiler
- **09_testing**: pytest, fixtures, mocking, parametrize

### 04. 백엔드 전문가 (Backend Expert)
실전 백엔드 개발에 필요한 모든 기술을 마스터합니다.

#### API 개발
- **01_fastapi_basics**: FastAPI 기본, 라우팅, 요청/응답
- **02_pydantic_models**: 데이터 검증, BaseModel, 시리얼라이제이션
- **03_dependency_injection**: Depends, 의존성 주입 패턴
- **04_middleware**: 미들웨어 작성, CORS, 인증
- **05_background_tasks**: BackgroundTasks, Celery

#### 데이터베이스
- **06_sqlalchemy_core**: Core API, 테이블 정의, 쿼리
- **07_sqlalchemy_orm**: ORM, 관계, 세션 관리
- **08_alembic_migrations**: 마이그레이션 관리
- **09_redis_caching**: Redis 연동, 캐싱 전략
- **10_mongodb**: Motor, 비동기 MongoDB 연동

#### 아키텍처 패턴
- **11_clean_architecture**: 계층 분리, 의존성 역전
- **12_repository_pattern**: Repository, Unit of Work
- **13_service_layer**: 비즈니스 로직 분리
- **14_ddd_patterns**: Entity, Value Object, Aggregate

#### 메시징 & 이벤트
- **15_rabbitmq**: pika, 메시지 큐 패턴
- **16_kafka**: aiokafka, 이벤트 스트리밍
- **17_event_driven**: 이벤트 기반 아키텍처

#### 보안 & 인증
- **18_jwt_auth**: JWT 토큰, 인증/인가
- **19_oauth2**: OAuth2 플로우, 소셜 로그인
- **20_security**: 보안 헤더, rate limiting, CSRF

#### 테스팅 & 모니터링
- **21_integration_testing**: 통합 테스트, TestClient
- **22_e2e_testing**: End-to-End 테스트
- **23_logging**: structlog, 로깅 전략
- **24_monitoring**: Prometheus, Grafana 연동
- **25_tracing**: OpenTelemetry, 분산 추적

#### 배포 & 운영
- **26_docker**: Dockerfile, docker-compose
- **27_kubernetes**: K8s 배포, 헬스체크
- **28_ci_cd**: GitHub Actions, Jenkins
- **29_graceful_shutdown**: 무중단 배포, signal handling
- **30_performance_tuning**: 성능 최적화, 병목 분석

## 🚀 학습 방법

1. **순차적 학습**: 01부터 04까지 순서대로 학습하세요.
2. **실습 중심**: 각 예제를 직접 실행하고 수정해보세요.
3. **문서 확인**: 코드 내 주석과 docstring을 꼼꼼히 읽으세요.
4. **테스트 작성**: 학습한 내용을 테스트 코드로 검증하세요.

## 🚀 빠른 시작 (초심자용)

### 1. Python 설치 확인
```bash
python --version  # 3.11 이상 권장
# Windows에서 안되면: py --version
# macOS/Linux에서 안되면: python3 --version
```

Python이 없다면? → **[상세 설치 가이드 보기](SETUP.md)**

### 2. 프로젝트 시작

```bash
# 1) 프로젝트 클론
git clone https://github.com/kyungseok-lee/python-by-examples.git
cd python-by-examples

# 2) 가상환경 설정 (선택사항이지만 권장)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3) 첫 예제 실행 (의존성 설치 불필요!)
cd 01-basics
python 01_variables_and_types.py
```

### 3. 전체 예제 실행
```bash
# 기본 문법 전체 실행
cd 01-basics
python run_all.py
```

### 4. FastAPI 서버 실행 (백엔드 과정)
```bash
cd 04-backend-expert
pip install -r requirements.txt
uvicorn 01_fastapi_basics:app --reload

# 브라우저에서 열기: http://localhost:8000/docs
```

**문제가 있나요?** → **[문제 해결 가이드 보기](SETUP.md#6-문제-해결)**

## 📦 환경 설정 (상세)

상세한 환경 설정은 **[SETUP.md](SETUP.md)** 파일을 참고하세요.

**포함 내용:**
- ✅ Python 설치 (Windows/macOS/Linux)
- ✅ IDE 설정 (VS Code/PyCharm)
- ✅ 가상환경 생성 및 활성화
- ✅ 의존성 설치
- ✅ 문제 해결 가이드
- ✅ 학습 로드맵

## 🎯 학습 목표

이 프로젝트를 완료하면 다음을 할 수 있습니다:

- ✅ Python 언어의 모든 핵심 기능을 마스터
- ✅ FastAPI로 프로덕션급 REST API 개발
- ✅ SQLAlchemy를 활용한 복잡한 데이터 모델링
- ✅ Clean Architecture와 DDD 패턴 적용
- ✅ 비동기 프로그래밍과 성능 최적화
- ✅ 메시지 큐와 이벤트 드리븐 아키텍처 구현
- ✅ 테스트 자동화와 CI/CD 파이프라인 구축
- ✅ Docker/Kubernetes 기반 배포
- ✅ 모니터링과 로깅 시스템 구축

## 📖 추가 학습 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [SQLAlchemy 공식 문서](https://docs.sqlalchemy.org/)
- [Real Python](https://realpython.com/)
- [Awesome Python](https://github.com/vinta/awesome-python)

## 🤝 기여

이 프로젝트는 지속적으로 업데이트됩니다. 개선 사항이나 새로운 예제가 있다면 PR을 보내주세요!

## 📝 라이선스

MIT License
