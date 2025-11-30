"""
06. 모듈과 패키지 (Modules and Packages)

모듈 구조, import, 패키지 관리를 학습합니다.
"""

import sys
import importlib


def demonstrate_import():
    """import 기본"""
    print("=" * 50)
    print("1. import 기본")
    print("=" * 50)
    
    # 표준 라이브러리
    import math
    import datetime as dt
    from collections import Counter
    
    print(f"math.pi: {math.pi}")
    print(f"오늘: {dt.date.today()}")
    print(f"Counter: {Counter(['a', 'b', 'a', 'c', 'b', 'a'])}")
    
    # __name__과 __file__
    print(f"\n__name__: {__name__}")
    print(f"__file__: {__file__}")
    
    print()


def demonstrate_module_search_path():
    """모듈 검색 경로"""
    print("=" * 50)
    print("2. 모듈 검색 경로")
    print("=" * 50)
    
    print("sys.path (처음 3개):")
    for i, path in enumerate(sys.path[:3], 1):
        print(f"  {i}. {path}")
    
    print()


def demonstrate_reload():
    """모듈 리로드"""
    print("=" * 50)
    print("3. 모듈 리로드")
    print("=" * 50)
    
    # 개발 중에 모듈을 수정하고 다시 로드할 때 사용
    print("importlib.reload()를 사용하여 모듈을 다시 로드할 수 있습니다")
    print("예: importlib.reload(module_name)")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 모듈과 패키지".center(50, "="))
    print()
    
    demonstrate_import()
    demonstrate_module_search_path()
    demonstrate_reload()
    
    print("=" * 50)
    print("✅ 모듈과 패키지 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

