# 🚀 Python 학습 환경 설정 가이드

Python 초심자를 위한 단계별 환경 설정 가이드입니다.

## 📋 목차
1. [Python 설치](#1-python-설치)
2. [IDE 설치 (선택사항)](#2-ide-설치-선택사항)
3. [프로젝트 클론](#3-프로젝트-클론)
4. [가상환경 설정](#4-가상환경-설정)
5. [첫 예제 실행](#5-첫-예제-실행)
6. [문제 해결](#6-문제-해결)

---

## 1. Python 설치

> **권장 버전**: Python 3.12+ (LTS)

### Windows

#### 방법 1: 공식 웹사이트에서 설치 (권장)

1. [Python 공식 웹사이트](https://www.python.org/downloads/) 접속
2. "Download Python 3.12.x" 버튼 클릭
3. 다운로드한 설치 파일 실행
4. ⚠️ **중요**: "Add Python to PATH" 체크박스 반드시 선택!
5. "Install Now" 클릭

#### 설치 확인
```cmd
# 명령 프롬프트(cmd) 또는 PowerShell 실행
python --version
# 출력 예: Python 3.12.x

pip --version
# 출력 예: pip 24.x from ...
```

### macOS

#### 방법 1: Homebrew 사용 (권장)

```bash
# Homebrew 설치 (이미 설치되어 있다면 건너뛰기)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python 설치
brew install python@3.12

# 확인
python3 --version
pip3 --version
```

#### 방법 2: 공식 웹사이트
1. [Python 공식 웹사이트](https://www.python.org/downloads/macos/) 접속
2. macOS용 인스톨러 다운로드 및 설치

### Linux (Ubuntu/Debian)

```bash
# 시스템 업데이트
sudo apt update
sudo apt upgrade -y

# Python 설치
sudo apt install python3.12 python3.12-venv python3-pip -y

# 확인
python3 --version
pip3 --version
```

---

## 2. IDE 설치 (선택사항)

### VS Code (추천 - 무료)

1. [VS Code 다운로드](https://code.visualstudio.com/)
2. 설치 후 실행
3. 확장 프로그램 설치:
   - Python (Microsoft)
   - Pylance (Microsoft)
   - Ruff (Astral Software) - 린터/포매터

### PyCharm Community (무료)

1. [PyCharm Community 다운로드](https://www.jetbrains.com/pycharm/download/)
2. 설치 및 실행

### Cursor (AI 지원)

1. [Cursor 다운로드](https://cursor.sh/)
2. AI 기반 코드 완성 지원

---

## 3. 프로젝트 클론

### Git 설치 확인

```bash
git --version
```

Git이 없다면:
- **Windows**: [Git for Windows](https://git-scm.com/download/win) 설치
- **macOS**: `brew install git`
- **Linux**: `sudo apt install git`

### 프로젝트 클론

```bash
# 원하는 폴더로 이동 (예: 홈 디렉토리)
cd ~

# 프로젝트 클론
git clone https://github.com/kyungseok-lee/python-by-examples.git

# 프로젝트 폴더로 이동
cd python-by-examples
```

---

## 4. 가상환경 설정

가상환경은 프로젝트마다 독립적인 Python 환경을 만들어줍니다. (강력 권장!)

### 가상환경 생성

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 가상환경 활성화

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

✅ 활성화되면 프롬프트 앞에 `(venv)` 표시가 나타납니다.

```bash
(venv) $  # 이렇게 보이면 성공!
```

### 가상환경 비활성화 (나중에 사용)

```bash
deactivate
```

---

## 5. 첫 예제 실행

### 5-1. 기본 문법부터 시작 (01-basics)

```bash
# 기본 문법 폴더로 이동
cd 01-basics

# 의존성 없음 - 바로 실행 가능!

# 첫 번째 예제 실행
python 01_variables_and_types.py
```

### 5-2. 모든 예제 순차 실행

```bash
# 01-basics 폴더에서
python run_all.py
```

### 5-3. 고급 과정 (의존성 설치 필요)

```bash
# 고급 과정 (pytest 등)
cd ../03-advanced
pip install -r requirements.txt
python 01_async_programming.py

# 백엔드 전문가 (FastAPI 등)
cd ../04-backend-expert
pip install -r requirements.txt
python 01_fastapi_basics.py
```

### 5-4. FastAPI 서버 실행

```bash
cd 04-backend-expert

# 의존성 설치 (처음 한 번만)
pip install -r requirements.txt

# FastAPI 서버 시작
uvicorn 01_fastapi_basics:app --reload
```

브라우저에서 접속:
- API 문서: http://localhost:8000/docs
- 대체 문서: http://localhost:8000/redoc

서버 종료: `Ctrl + C`

---

## 6. 문제 해결

### 문제 1: "python" 명령어를 찾을 수 없습니다

**Windows:**
```cmd
# python 대신 py 사용
py --version
py -m venv venv
```

**macOS/Linux:**
```bash
# python 대신 python3 사용
python3 --version
python3 -m venv venv
```

### 문제 2: pip 명령어 오류

```bash
# pip 업그레이드
python -m pip install --upgrade pip

# 또는
python3 -m pip install --upgrade pip
```

### 문제 3: 가상환경 활성화 안됨 (Windows PowerShell)

PowerShell 실행 정책 오류 시:

```powershell
# PowerShell을 관리자 권한으로 실행
Set-ExecutionPolicy RemoteSigned

# 다시 시도
venv\Scripts\Activate.ps1
```

### 문제 4: 모듈을 찾을 수 없습니다 (ModuleNotFoundError)

```bash
# 가상환경이 활성화되어 있는지 확인
# (venv) 표시가 있어야 함

# 의존성 다시 설치
pip install -r requirements.txt
```

### 문제 5: Pydantic 관련 오류

이 프로젝트는 **Pydantic v2**를 사용합니다. v1과 호환되지 않는 문법이 있습니다.

```bash
# Pydantic 버전 확인
pip show pydantic

# 업그레이드
pip install --upgrade pydantic
```

### 문제 6: 포트가 이미 사용 중입니다 (FastAPI)

```bash
# 다른 포트로 실행
uvicorn 01_fastapi_basics:app --reload --port 8001
```

---

## 📚 학습 순서 추천

### 1주차: 기본 문법 마스터
```bash
cd 01-basics
python run_all.py  # 모든 예제 실행해보기
```
- 매일 2-3개 예제씩 학습
- 코드를 직접 수정해보며 실험

### 2주차: 중급 개념
```bash
cd 02-intermediate
# 데코레이터, 제너레이터 등 실습
```

### 3주차: 고급 개념
```bash
cd 03-advanced
pip install -r requirements.txt
# 비동기, 타입 힌트, 데이터클래스 등
```

### 4주차: 백엔드 개발
```bash
cd 04-backend-expert
pip install -r requirements.txt
# FastAPI로 실제 API 만들기
```

---

## 🎯 빠른 시작 체크리스트

- [ ] Python 3.12+ 설치 완료
- [ ] `python --version` 명령어 작동 확인
- [ ] 프로젝트 클론 완료
- [ ] 가상환경 생성 및 활성화
- [ ] `01-basics/01_variables_and_types.py` 실행 성공
- [ ] VS Code 또는 선호하는 에디터 설치

모든 체크박스가 완료되면 학습을 시작할 준비가 끝났습니다! 🎉

---

## 💡 학습 팁

1. **코드를 직접 수정해보세요**
   - 예제의 값을 바꿔보고 실행해보세요
   - 오류가 나면 왜 그런지 고민해보세요

2. **주석을 꼼꼼히 읽으세요**
   - 모든 코드에 한국어 설명이 있습니다

3. **타입 힌트를 활용하세요**
   - Python 3.12+ 스타일 타입 힌트 학습
   - IDE의 자동 완성 기능 활용

4. **직접 프로젝트를 만들어보세요**
   - 학습한 내용으로 간단한 프로그램 작성

---

## 🎓 다음 단계

환경 설정이 완료되었다면:

1. `01-basics/README.md` 읽기
2. 첫 번째 예제 실행하기
3. 매일 조금씩 학습하기
4. 실습 프로젝트 만들어보기

**화이팅! 🚀**
