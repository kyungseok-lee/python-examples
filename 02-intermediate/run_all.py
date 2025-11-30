"""
모든 중급 예제를 순차적으로 실행합니다.
"""

import importlib

EXAMPLES = [
    "01_decorators",
    "02_generators",
    "03_context_managers",
    "04_file_io",
    "05_error_handling",
    "06_modules_packages",
    "07_collections",
    "08_datetime",
]


def run_example(module_name):
    """예제 모듈을 실행합니다."""
    print("\n" + "=" * 70)
    print(f"▶ {module_name} 실행 중...")
    print("=" * 70)
    
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            print(f"경고: {module_name}에 main() 함수가 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
        return False
    
    return True


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 전체 예제 실행".center(70, "="))
    print(f"총 {len(EXAMPLES)}개의 예제를 실행합니다.")
    print("=" * 70)
    
    success_count = 0
    for example in EXAMPLES:
        if run_example(example):
            success_count += 1
        
        if example != EXAMPLES[-1]:
            input("\nEnter 키를 눌러 다음 예제로 이동...")
    
    print("\n" + "=" * 70)
    print(f"✅ 실행 완료: {success_count}/{len(EXAMPLES)}개 성공")
    print("=" * 70)


if __name__ == "__main__":
    main()

