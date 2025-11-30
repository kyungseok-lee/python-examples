@echo off
REM Python 학습 환경 빠른 설정 스크립트 (Windows)
REM 사용법: quickstart.bat

echo ==========================================
echo 🐍 Python 학습 환경 설정을 시작합니다
echo ==========================================
echo.

REM Python 버전 확인
echo 1️⃣  Python 버전 확인 중...
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Python이 설치되어 있지 않습니다!
        echo 📖 SETUP.md 파일을 참고하여 Python을 먼저 설치해주세요.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
) else (
    set PYTHON_CMD=python
)

for /f "tokens=2" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% 발견
echo.

REM 가상환경 생성
echo 2️⃣  가상환경 생성 중...
if exist venv (
    echo ⚠️  가상환경이 이미 존재합니다. 건너뜁니다.
) else (
    %PYTHON_CMD% -m venv venv
    echo ✅ 가상환경 생성 완료
)
echo.

REM 가상환경 활성화 안내
echo 3️⃣  가상환경 활성화 방법:
echo    CMD:        venv\Scripts\activate
echo    PowerShell: venv\Scripts\Activate.ps1
echo.

REM 첫 예제 실행 안내
echo 4️⃣  첫 예제 실행 방법:
echo    cd 01-basics
echo    %PYTHON_CMD% 01_variables_and_types.py
echo.

REM 완료
echo ==========================================
echo ✅ 환경 설정이 완료되었습니다!
echo ==========================================
echo.
echo 📚 다음 단계:
echo    1. 가상환경 활성화 (위의 명령어 참고)
echo    2. cd 01-basics
echo    3. %PYTHON_CMD% 01_variables_and_types.py
echo.
echo 📖 자세한 가이드: SETUP.md 파일을 참고하세요
echo.
pause

