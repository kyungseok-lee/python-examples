"""
08. 날짜와 시간 (datetime)

datetime, timedelta, timezone 처리를 학습합니다.
"""

from datetime import datetime, date, time, timedelta, timezone
import time as time_module


def demonstrate_datetime_basics():
    """datetime 기본"""
    print("=" * 50)
    print("1. datetime 기본")
    print("=" * 50)
    
    # 현재 시간
    now = datetime.now()
    today = date.today()
    current_time = datetime.now().time()
    
    print(f"현재 날짜시간: {now}")
    print(f"오늘 날짜: {today}")
    print(f"현재 시간: {current_time}")
    
    # 특정 날짜시간 생성
    dt = datetime(2025, 11, 30, 15, 30, 45)
    print(f"\n특정 날짜시간: {dt}")
    
    # 구성 요소 접근
    print(f"년: {dt.year}, 월: {dt.month}, 일: {dt.day}")
    print(f"시: {dt.hour}, 분: {dt.minute}, 초: {dt.second}")
    
    print()


def demonstrate_timedelta():
    """timedelta (시간 간격)"""
    print("=" * 50)
    print("2. timedelta")
    print("=" * 50)
    
    now = datetime.now()
    
    # 시간 더하기/빼기
    tomorrow = now + timedelta(days=1)
    next_week = now + timedelta(weeks=1)
    three_hours_ago = now - timedelta(hours=3)
    
    print(f"현재: {now}")
    print(f"내일: {tomorrow}")
    print(f"다음 주: {next_week}")
    print(f"3시간 전: {three_hours_ago}")
    
    # 시간 차이 계산
    dt1 = datetime(2025, 1, 1)
    dt2 = datetime(2025, 12, 31)
    diff = dt2 - dt1
    
    print(f"\n2025년 기간: {diff.days}일")
    
    print()


def demonstrate_formatting():
    """날짜시간 포매팅"""
    print("=" * 50)
    print("3. 날짜시간 포매팅")
    print("=" * 50)
    
    now = datetime.now()
    
    # strftime (datetime -> 문자열)
    print(f"ISO 형식: {now.isoformat()}")
    print(f"사용자 정의: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"한국어 스타일: {now.strftime('%Y년 %m월 %d일 %H시 %M분')}")
    
    # strptime (문자열 -> datetime)
    date_str = "2025-11-30 15:30:00"
    parsed = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    print(f"\n파싱: {date_str} -> {parsed}")
    
    print()


def demonstrate_timezone():
    """타임존"""
    print("=" * 50)
    print("4. 타임존")
    print("=" * 50)
    
    # UTC
    utc_now = datetime.now(timezone.utc)
    print(f"UTC: {utc_now}")
    
    # 타임존 변환
    kst = timezone(timedelta(hours=9))
    kst_now = utc_now.astimezone(kst)
    print(f"KST: {kst_now}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - datetime".center(50, "="))
    print()
    
    demonstrate_datetime_basics()
    demonstrate_timedelta()
    demonstrate_formatting()
    demonstrate_timezone()
    
    print("=" * 50)
    print("✅ datetime 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

