# 08. Testing - pytest 테스팅

> 💡 **핵심:**
> pytest는 Python의 사실상 표준 테스트 프레임워크입니다.
> 간결한 문법, 강력한 fixture, 풍부한 플러그인을 제공합니다.

## 🔄 다른 언어와 비교

| 구분 | Java | Go | Python |
|------|------|-----|--------|
| 기본 프레임워크 | JUnit | testing | pytest |
| Assertion | assertEquals | t.Equal | assert |
| Mock | Mockito | testify | pytest-mock |
| Fixture | @BeforeEach | - | @pytest.fixture |

## 📚 예제 목록

| 파일 | 설명 | 난이도 |
|------|------|--------|
| 01_pytest_basics.py | pytest 기초 | ⭐ |
| 02_fixtures.py | Fixture 활용 | ⭐⭐ |
| 03_mocking.py | Mock 사용법 | ⭐⭐ |
| 04_parametrize.py | 파라미터화 테스트 | ⭐⭐ |

## 🚀 실행 방법

```bash
# pytest 설치
pip install pytest pytest-asyncio

# 테스트 실행
pytest -v
```

