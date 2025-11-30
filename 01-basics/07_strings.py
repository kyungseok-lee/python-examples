"""
07. 문자열 (Strings)

문자열 조작, 포매팅, 정규표현식을 학습합니다.
"""

import re


def demonstrate_string_basics():
    """문자열 기본"""
    print("=" * 50)
    print("1. 문자열 기본")
    print("=" * 50)
    
    # 생성
    text1 = 'Hello'
    text2 = "World"
    text3 = """여러 줄
    문자열"""
    
    # Raw 문자열 (이스케이프 무시)
    path = r"C:\Users\name\documents"
    print(f"Raw 문자열: {path}")
    
    # 이스케이프 시퀀스
    escaped = "첫 줄\n둘째 줄\t탭 사용"
    print(f"이스케이프:\n{escaped}")
    
    # 문자열 연산
    combined = text1 + " " + text2
    repeated = "Ha" * 3
    print(f"\n연결: {combined}")
    print(f"반복: {repeated}")
    
    print()


def demonstrate_string_methods():
    """문자열 메서드"""
    print("=" * 50)
    print("2. 문자열 메서드")
    print("=" * 50)
    
    text = "  Python Programming  "
    
    # 대소문자 변환
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"title(): '{text.title()}'")
    print(f"swapcase(): '{text.swapcase()}'")
    
    # 공백 제거
    print(f"\nstrip(): '{text.strip()}'")
    print(f"lstrip(): '{text.lstrip()}'")
    print(f"rstrip(): '{text.rstrip()}'")
    
    # 검색
    text2 = "Python is awesome"
    print(f"\nfind('is'): {text2.find('is')}")
    print(f"index('is'): {text2.index('is')}")
    print(f"count('o'): {text2.count('o')}")
    
    # 체크
    print(f"\nstartswith('Python'): {text2.startswith('Python')}")
    print(f"endswith('awesome'): {text2.endswith('awesome')}")
    print(f"'123'.isdigit(): {'123'.isdigit()}")
    print(f"'abc'.isalpha(): {'abc'.isalpha()}")
    print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
    
    # 분리/결합
    words = "Python,Java,Go,Rust".split(',')
    print(f"\nsplit(','): {words}")
    
    joined = " | ".join(words)
    print(f"join: {joined}")
    
    # 치환
    replaced = text2.replace("awesome", "great")
    print(f"\nreplace: {replaced}")
    
    print()


def demonstrate_string_formatting():
    """문자열 포매팅"""
    print("=" * 50)
    print("3. 문자열 포매팅")
    print("=" * 50)
    
    name = "Alice"
    age = 25
    pi = 3.14159265359
    
    # % 포매팅 (레거시)
    msg1 = "이름: %s, 나이: %d" % (name, age)
    print(f"% 포매팅: {msg1}")
    
    # str.format()
    msg2 = "이름: {}, 나이: {}".format(name, age)
    msg3 = "이름: {0}, 나이: {1}, 다시: {0}".format(name, age)
    msg4 = "이름: {name}, 나이: {age}".format(name=name, age=age)
    print(f"format(): {msg2}")
    print(f"format(인덱스): {msg3}")
    print(f"format(키워드): {msg4}")
    
    # f-string (Python 3.6+, 권장)
    msg5 = f"이름: {name}, 나이: {age}"
    msg6 = f"계산: {10 + 20}"
    msg7 = f"메서드: {name.upper()}"
    print(f"\nf-string: {msg5}")
    print(f"f-string 표현식: {msg6}")
    print(f"f-string 메서드: {msg7}")
    
    # 포맷 지정
    print(f"\n소수점 2자리: {pi:.2f}")
    print(f"천 단위 구분: {1234567:,}")
    print(f"패딩 (10자리, 오른쪽 정렬): '{name:>10}'")
    print(f"패딩 (10자리, 왼쪽 정렬): '{name:<10}'")
    print(f"패딩 (10자리, 가운데 정렬): '{name:^10}'")
    print(f"0 패딩: {42:05d}")
    
    # 디버깅 (Python 3.8+)
    x = 10
    y = 20
    print(f"\n디버그 포맷: {x=}, {y=}, {x+y=}")
    
    print()


def demonstrate_string_slicing():
    """문자열 슬라이싱"""
    print("=" * 50)
    print("4. 문자열 슬라이싱")
    print("=" * 50)
    
    text = "Python Programming"
    
    print(f"원본: '{text}'")
    print(f"[0]: '{text[0]}'")
    print(f"[-1]: '{text[-1]}'")
    print(f"[0:6]: '{text[0:6]}'")
    print(f"[7:]: '{text[7:]}'")
    print(f"[:6]: '{text[:6]}'")
    print(f"[::2]: '{text[::2]}'")
    print(f"[::-1]: '{text[::-1]}'")  # 역순
    
    print()


def demonstrate_string_encoding():
    """문자열 인코딩"""
    print("=" * 50)
    print("5. 문자열 인코딩")
    print("=" * 50)
    
    text = "안녕하세요"
    
    # 인코딩: str -> bytes
    utf8_bytes = text.encode("utf-8")
    print(f"UTF-8 인코딩: {utf8_bytes}")
    
    # 디코딩: bytes -> str
    decoded = utf8_bytes.decode("utf-8")
    print(f"디코딩: {decoded}")
    
    # 다양한 인코딩
    euckr_bytes = text.encode("euc-kr")
    print(f"EUC-KR 인코딩: {euckr_bytes}")
    
    # ASCII
    ascii_text = "Hello"
    ascii_bytes = ascii_text.encode("ascii")
    print(f"ASCII 인코딩: {ascii_bytes}")
    
    print()


def demonstrate_regex_basics():
    """정규표현식 기본"""
    print("=" * 50)
    print("6. 정규표현식 기본")
    print("=" * 50)
    
    # 매칭
    pattern = r"\d+"  # 하나 이상의 숫자
    text = "Today is 2025-11-30"
    
    match = re.search(pattern, text)
    if match:
        print(f"찾은 숫자: {match.group()}")
    
    # 모든 매칭 찾기
    numbers = re.findall(r"\d+", text)
    print(f"모든 숫자: {numbers}")
    
    # 분리
    text2 = "apple,banana;cherry:grape"
    fruits = re.split(r"[,;:]", text2)
    print(f"분리: {fruits}")
    
    # 치환
    text3 = "2025-11-30"
    replaced = re.sub(r"-", "/", text3)
    print(f"치환: {replaced}")
    
    print()


def demonstrate_regex_patterns():
    """정규표현식 패턴"""
    print("=" * 50)
    print("7. 정규표현식 패턴")
    print("=" * 50)
    
    # 이메일 검증
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    emails = [
        "user@example.com",
        "invalid.email",
        "test@domain.co.kr"
    ]
    
    print("이메일 검증:")
    for email in emails:
        is_valid = bool(re.match(email_pattern, email))
        print(f"  {email}: {'✓' if is_valid else '✗'}")
    
    # 전화번호 추출
    text = "연락처: 010-1234-5678, 02-987-6543"
    phone_pattern = r"\d{2,3}-\d{3,4}-\d{4}"
    phones = re.findall(phone_pattern, text)
    print(f"\n전화번호 추출: {phones}")
    
    # URL 추출
    text2 = "Visit https://example.com and http://test.org"
    url_pattern = r"https?://[^\s]+"
    urls = re.findall(url_pattern, text2)
    print(f"URL 추출: {urls}")
    
    # 그룹 캡처
    date_pattern = r"(\d{4})-(\d{2})-(\d{2})"
    date_text = "오늘은 2025-11-30입니다"
    match = re.search(date_pattern, date_text)
    if match:
        year, month, day = match.groups()
        print(f"\n날짜 파싱: {year}년 {month}월 {day}일")
    
    print()


def demonstrate_string_template():
    """문자열 템플릿"""
    print("=" * 50)
    print("8. 문자열 템플릿")
    print("=" * 50)
    
    from string import Template
    
    # 기본 템플릿
    tmpl = Template("안녕하세요, $name님! 나이: $age세")
    result = tmpl.substitute(name="Alice", age=25)
    print(f"템플릿: {result}")
    
    # safe_substitute (누락된 키 허용)
    tmpl2 = Template("$greeting, $name!")
    result2 = tmpl2.safe_substitute(name="Bob")
    print(f"safe_substitute: {result2}")
    
    # 실무 활용: SQL 쿼리 템플릿
    query_tmpl = Template("""
        SELECT * FROM $table
        WHERE $column = '$value'
    """)
    query = query_tmpl.substitute(
        table="users",
        column="status",
        value="active"
    )
    print(f"SQL 템플릿:{query}")
    
    print()


def demonstrate_string_performance():
    """문자열 성능"""
    print("=" * 50)
    print("9. 문자열 성능")
    print("=" * 50)
    
    import time
    
    # + 연산 vs join
    n = 1000
    
    # + 연산 (비효율적)
    start = time.perf_counter()
    result = ""
    for i in range(n):
        result += str(i)
    plus_time = time.perf_counter() - start
    
    # join (효율적)
    start = time.perf_counter()
    result = "".join(str(i) for i in range(n))
    join_time = time.perf_counter() - start
    
    print(f"+ 연산 {n}회: {plus_time:.4f}초")
    print(f"join {n}회: {join_time:.4f}초")
    print(f"join이 약 {plus_time/join_time:.1f}배 빠름")
    
    # f-string vs format
    name = "Alice"
    age = 25
    iterations = 100000
    
    start = time.perf_counter()
    for _ in range(iterations):
        _ = f"Name: {name}, Age: {age}"
    fstring_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for _ in range(iterations):
        _ = "Name: {}, Age: {}".format(name, age)
    format_time = time.perf_counter() - start
    
    print(f"\nf-string {iterations}회: {fstring_time:.4f}초")
    print(f"format {iterations}회: {format_time:.4f}초")
    print(f"f-string이 약 {format_time/fstring_time:.1f}배 빠름")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 문자열".center(50, "="))
    print()
    
    demonstrate_string_basics()
    demonstrate_string_methods()
    demonstrate_string_formatting()
    demonstrate_string_slicing()
    demonstrate_string_encoding()
    demonstrate_regex_basics()
    demonstrate_regex_patterns()
    demonstrate_string_template()
    demonstrate_string_performance()
    
    print("=" * 50)
    print("✅ 문자열 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

