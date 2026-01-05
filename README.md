# Python Backend Expert Learning Path

> **대상:** Java/Go/Kotlin 등 다른 언어 경험이 있는 개발자가 Python을 빠르게 학습하기 위한 예제 중심 프로젝트입니다.

Python 백엔드 전문가가 되기 위한 체계적인 학습 프로젝트입니다.

## 🎯 학습 목표

- Python 문법과 관용구(Idioms)를 빠르게 익히기
- 다른 언어와의 차이점 및 Python 특유의 함정(Gotchas) 이해
- 실무에서 바로 적용 가능한 백엔드 패턴 습득
- 메모리/GC 특성을 이해하고 성능 최적화 방법 학습

## 🔧 기술 스택

- **Python**: 3.12+ (LTS)
- **Web Framework**: FastAPI 0.115+
- **Data Validation**: Pydantic v2.10+
- **Database**: SQLAlchemy 2.0+
- **Testing**: pytest 8.3+

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

- **01_async_programming**: async/await, asyncio
- **02_multithreading**: threading, concurrent.futures
- **03_type_hints**: Python 3.12+ 타입 힌트, Protocol, Generic
- **04_dataclasses**: @dataclass, slots, frozen
- **05_testing**: pytest, fixtures, mocking

### 04. 백엔드 전문가 (Backend Expert)
실전 백엔드 개발에 필요한 모든 기술을 마스터합니다.

#### API 개발
- **01_fastapi_basics**: FastAPI 기본, 라우팅, 요청/응답
- **02_pydantic_models**: Pydantic v2, 데이터 검증, 시리얼라이제이션
- **03_clean_architecture**: 계층 분리, 의존성 역전, Protocol

## 🚀 빠른 시작

### 1. Python 설치 확인
```bash
python --version  # 3.12 이상 권장
```

Python이 없다면? → **[상세 설치 가이드 보기](SETUP.md)**

### 2. 프로젝트 시작

```bash
# 1) 프로젝트 클론
git clone https://github.com/kyungseok-lee/python-by-examples.git
cd python-by-examples

# 2) 가상환경 설정 (권장)
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

## 📦 환경 설정

상세한 환경 설정은 **[SETUP.md](SETUP.md)** 파일을 참고하세요.

## 🎯 Python 3.12+ 주요 특징

이 프로젝트는 Python 3.12+ 스타일을 적용합니다:

### 타입 힌트
```python
# Python 3.9+: 내장 타입 사용
def process(items: list[int]) -> dict[str, int]:
    ...

# Python 3.10+: 유니온 문법
def find(id: int) -> User | None:
    ...

# Python 3.12+: type 키워드 (PEP 695)
type Vector = list[float]
```

### 메모리 최적화 (GC 관점)
```python
from dataclasses import dataclass

# __slots__ 사용으로 메모리 절약
@dataclass(slots=True)
class User:
    id: int
    name: str
    email: str
```

### Pydantic v2
```python
from pydantic import BaseModel, ConfigDict, field_validator

class User(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    name: str
    email: str
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError('Name too short')
        return v
```

## 🔬 GC/메모리 최적화 포인트

1. **`__slots__` 사용**: 클래스에서 `__dict__` 대신 `__slots__` 사용
2. **제너레이터 활용**: 대용량 데이터 처리 시 메모리 효율적
3. **불변 객체 선호**: `frozen=True` 데이터클래스 사용
4. **Protocol 사용**: ABC 대신 구조적 서브타이핑
5. **gc 모듈 활용**: 성능 크리티컬 구간에서 GC 제어

## 📖 추가 학습 자료

- [Python 3.12 What's New](https://docs.python.org/3/whatsnew/3.12.html)
- [Pydantic v2 Documentation](https://docs.pydantic.dev/latest/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Memory Management](https://docs.python.org/3/c-api/memory.html)

## 📋 프로젝트 개선 가이드

이 프로젝트의 구조와 개선 방향에 대한 상세 가이드는 **[PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md)**를 참고하세요.

- 전문가 대상 학습 콘텐츠 작성 가이드
- 폴더 구조 제안
- 예제 파일 템플릿
- 다른 언어와의 비교 포인트

## 🤝 기여

이 프로젝트는 지속적으로 업데이트됩니다. 개선 사항이나 새로운 예제가 있다면 PR을 보내주세요!

## 📝 라이선스

MIT License
