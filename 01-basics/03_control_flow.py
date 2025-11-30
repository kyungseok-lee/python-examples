"""
03. 제어 흐름 (Control Flow)

조건문을 사용한 프로그램 흐름 제어를 학습합니다.
"""


def demonstrate_if_statement():
    """if 문"""
    print("=" * 50)
    print("1. if 문")
    print("=" * 50)
    
    age = 25
    
    if age >= 18:
        print(f"나이: {age} - 성인입니다")
    
    # if-else
    if age < 20:
        print("20세 미만입니다")
    else:
        print("20세 이상입니다")
    
    # if-elif-else
    if age < 13:
        category = "어린이"
    elif age < 20:
        category = "청소년"
    elif age < 65:
        category = "성인"
    else:
        category = "노인"
    
    print(f"연령대: {category}")
    print()


def demonstrate_nested_if():
    """중첩 if 문"""
    print("=" * 50)
    print("2. 중첩 if 문")
    print("=" * 50)
    
    score = 85
    attendance = 90
    
    if score >= 60:
        if attendance >= 80:
            result = "합격"
        else:
            result = "출석 미달로 불합격"
    else:
        result = "점수 미달로 불합격"
    
    print(f"점수: {score}, 출석: {attendance}%")
    print(f"결과: {result}")
    print()


def demonstrate_ternary_operator():
    """삼항 연산자 (Conditional Expression)"""
    print("=" * 50)
    print("3. 삼항 연산자")
    print("=" * 50)
    
    age = 18
    
    # Python의 삼항 연산자
    status = "성인" if age >= 18 else "미성년자"
    print(f"나이: {age} - {status}")
    
    # 중첩 삼항 연산자 (가독성 주의!)
    score = 75
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(f"점수: {score} - 학점: {grade}")
    
    # 더 나은 방법: 일반 if-elif-else 사용
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"(개선) 점수: {score} - 학점: {grade}")
    print()


def demonstrate_match_statement():
    """match 문 (Python 3.10+)"""
    print("=" * 50)
    print("4. match 문 (구조 패턴 매칭)")
    print("=" * 50)
    
    # 기본 매칭
    def get_http_status_message(status_code):
        match status_code:
            case 200:
                return "OK"
            case 201:
                return "Created"
            case 400:
                return "Bad Request"
            case 401:
                return "Unauthorized"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return "Unknown Status"
    
    codes = [200, 404, 500, 999]
    for code in codes:
        message = get_http_status_message(code)
        print(f"HTTP {code}: {message}")
    
    print()
    
    # 여러 값 매칭
    def categorize_day(day):
        match day:
            case "월" | "화" | "수" | "목" | "금":
                return "평일"
            case "토" | "일":
                return "주말"
            case _:
                return "잘못된 요일"
    
    for day in ["월", "토", "ABC"]:
        print(f"{day}: {categorize_day(day)}")
    
    print()
    
    # 구조 패턴 매칭
    def process_command(command):
        match command:
            case ["quit"]:
                return "프로그램을 종료합니다"
            case ["load", filename]:
                return f"파일 로드: {filename}"
            case ["save", filename]:
                return f"파일 저장: {filename}"
            case ["delete", *files]:
                return f"파일 삭제: {', '.join(files)}"
            case _:
                return "알 수 없는 명령"
    
    commands = [
        ["quit"],
        ["load", "data.json"],
        ["save", "output.txt"],
        ["delete", "file1.txt", "file2.txt", "file3.txt"],
        ["unknown"]
    ]
    
    for cmd in commands:
        result = process_command(cmd)
        print(f"{cmd} -> {result}")
    
    print()


def demonstrate_guard_clauses():
    """가드 절 (Guard Clauses) - 조기 반환 패턴"""
    print("=" * 50)
    print("5. 가드 절 (조기 반환)")
    print("=" * 50)
    
    # 나쁜 예: 중첩이 깊음
    def process_user_bad(user):
        if user is not None:
            if user.get("is_active"):
                if user.get("email"):
                    return f"처리 완료: {user['email']}"
                else:
                    return "이메일 없음"
            else:
                return "비활성 사용자"
        else:
            return "사용자 없음"
    
    # 좋은 예: 가드 절로 조기 반환
    def process_user_good(user):
        if user is None:
            return "사용자 없음"
        
        if not user.get("is_active"):
            return "비활성 사용자"
        
        if not user.get("email"):
            return "이메일 없음"
        
        return f"처리 완료: {user['email']}"
    
    test_users = [
        None,
        {"is_active": False, "email": "test@example.com"},
        {"is_active": True, "email": ""},
        {"is_active": True, "email": "user@example.com"}
    ]
    
    print("가드 절 패턴 적용:")
    for user in test_users:
        result = process_user_good(user)
        print(f"  {user} -> {result}")
    
    print()


def demonstrate_truthy_falsy():
    """Truthy/Falsy 값 활용"""
    print("=" * 50)
    print("6. Truthy/Falsy 값 활용")
    print("=" * 50)
    
    # Falsy 값들: False, None, 0, 0.0, '', [], {}, set()
    values = [
        True, False, None,
        0, 1, -1,
        0.0, 3.14,
        '', 'text',
        [], [1, 2],
        {}, {'key': 'value'},
        set(), {1, 2}
    ]
    
    for value in values:
        truthy = "Truthy" if value else "Falsy"
        print(f"{str(value):20} -> {truthy}")
    
    print()
    
    # 실무 활용
    def get_username(user):
        # None 체크와 빈 문자열 체크를 동시에
        return user.get("name") or "익명"
    
    users = [
        {"name": "Alice"},
        {"name": ""},
        {"email": "test@example.com"},
        None
    ]
    
    print("실무 활용:")
    for user in users:
        if user:
            name = get_username(user)
            print(f"  사용자: {name}")
        else:
            print("  사용자: None")
    
    print()


def demonstrate_short_circuit():
    """단락 평가 (Short-circuit Evaluation)"""
    print("=" * 50)
    print("7. 단락 평가")
    print("=" * 50)
    
    # and: 첫 Falsy 값 반환, 모두 Truthy면 마지막 값 반환
    print("and 연산:")
    print(f"'a' and 'b' and 'c': {'a' and 'b' and 'c'}")
    print(f"'a' and '' and 'c': {'a' and '' and 'c'}")
    print(f"'a' and 0 and 'c': {'a' and 0 and 'c'}")
    
    # or: 첫 Truthy 값 반환, 모두 Falsy면 마지막 값 반환
    print("\nor 연산:")
    print(f"'' or 'b' or 'c': {'' or 'b' or 'c'}")
    print(f"'' or 0 or 'c': {'' or 0 or 'c'}")
    print(f"'' or 0 or []: {'' or 0 or []}")
    
    # 실무 활용: 기본값 설정
    print("\n기본값 설정:")
    config = {}
    host = config.get("host") or "localhost"
    port = config.get("port") or 8000
    print(f"서버: {host}:{port}")
    
    # 실무 활용: 안전한 체인 호출
    print("\n안전한 체인 호출:")
    user = {"profile": {"address": {"city": "Seoul"}}}
    city = user and user.get("profile") and user.get("profile").get("address") and \
           user.get("profile").get("address").get("city")
    print(f"도시: {city}")
    
    # 더 나은 방법: try-except 또는 get 체인
    city = user.get("profile", {}).get("address", {}).get("city", "Unknown")
    print(f"도시 (개선): {city}")
    
    print()


def demonstrate_walrus_operator():
    """바다코끼리 연산자 := (Python 3.8+)"""
    print("=" * 50)
    print("8. 바다코끼리 연산자 :=")
    print("=" * 50)
    
    # 조건문에서 할당과 동시에 사용
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 기존 방식
    filtered = [n for n in numbers if n ** 2 > 50]
    print(f"제곱이 50 초과: {filtered}")
    
    # 바다코끼리 연산자 사용
    filtered_with_squares = [(n, square) for n in numbers if (square := n ** 2) > 50]
    print(f"바다코끼리 사용: {filtered_with_squares}")
    
    # if 문에서 사용
    text = "Python Programming"
    if (length := len(text)) > 10:
        print(f"\n문자열 길이 {length}는 10보다 큽니다")
    
    # while 문에서 사용
    print("\n파일 읽기 시뮬레이션:")
    data_chunks = ["Hello", "World", "Python", ""]
    index = 0
    
    def read_chunk():
        nonlocal index
        if index < len(data_chunks):
            chunk = data_chunks[index]
            index += 1
            return chunk
        return None
    
    # 바다코끼리 연산자로 간결하게
    while (chunk := read_chunk()) is not None and chunk:
        print(f"  청크: {chunk}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 제어 흐름".center(50, "="))
    print()
    
    demonstrate_if_statement()
    demonstrate_nested_if()
    demonstrate_ternary_operator()
    demonstrate_match_statement()
    demonstrate_guard_clauses()
    demonstrate_truthy_falsy()
    demonstrate_short_circuit()
    demonstrate_walrus_operator()
    
    print("=" * 50)
    print("✅ 제어 흐름 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

