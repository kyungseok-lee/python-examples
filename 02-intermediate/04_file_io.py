"""
04. 파일 입출력 (File I/O)

파일 읽기/쓰기, CSV, JSON 처리를 학습합니다.
"""

import json
import csv
import os


def demonstrate_file_basics():
    """파일 기본 읽기/쓰기"""
    print("=" * 50)
    print("1. 파일 기본 읽기/쓰기")
    print("=" * 50)
    
    # 쓰기
    with open('/tmp/sample.txt', 'w', encoding='utf-8') as f:
        f.write("첫 번째 줄\n")
        f.write("두 번째 줄\n")
        f.writelines(["세 번째 줄\n", "네 번째 줄\n"])
    
    # 읽기
    with open('/tmp/sample.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"전체 내용:\n{content}")
    
    # 줄 단위 읽기
    with open('/tmp/sample.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"줄 목록: {lines}")
    
    print()


def demonstrate_json():
    """JSON 처리"""
    print("=" * 50)
    print("2. JSON 처리")
    print("=" * 50)
    
    data = {
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "Go", "Java"],
        "address": {
            "city": "Seoul",
            "country": "Korea"
        }
    }
    
    # JSON 파일로 저장
    with open('/tmp/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("JSON 파일 저장 완료")
    
    # JSON 파일 읽기
    with open('/tmp/data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(f"읽은 데이터:\n{json.dumps(loaded_data, ensure_ascii=False, indent=2)}")
    
    print()


def demonstrate_csv():
    """CSV 처리"""
    print("=" * 50)
    print("3. CSV 처리")
    print("=" * 50)
    
    # CSV 쓰기
    users = [
        ["name", "age", "city"],
        ["Alice", 25, "Seoul"],
        ["Bob", 30, "Busan"],
        ["Charlie", 35, "Incheon"]
    ]
    
    with open('/tmp/users.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(users)
    
    print("CSV 파일 저장 완료")
    
    # CSV 읽기
    with open('/tmp/users.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"  {row}")
    
    # DictReader/DictWriter
    print("\nDictReader:")
    with open('/tmp/users.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  {row['name']}: {row['age']}세, {row['city']}")
    
    print()


def demonstrate_pathlib():
    """pathlib 사용"""
    print("=" * 50)
    print("4. pathlib 모듈")
    print("=" * 50)
    
    from pathlib import Path
    
    # 경로 생성
    path = Path("/tmp/test_dir")
    path.mkdir(exist_ok=True)
    
    # 파일 생성
    file_path = path / "test.txt"
    file_path.write_text("Hello, pathlib!", encoding='utf-8')
    
    # 파일 읽기
    content = file_path.read_text(encoding='utf-8')
    print(f"내용: {content}")
    
    # 파일 정보
    print(f"존재 여부: {file_path.exists()}")
    print(f"파일 이름: {file_path.name}")
    print(f"확장자: {file_path.suffix}")
    print(f"부모 디렉토리: {file_path.parent}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 파일 I/O".center(50, "="))
    print()
    
    demonstrate_file_basics()
    demonstrate_json()
    demonstrate_csv()
    demonstrate_pathlib()
    
    print("=" * 50)
    print("✅ 파일 I/O 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

