"""
02. 멀티스레딩 (Multithreading)

threading과 concurrent.futures를 학습합니다.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def demonstrate_threading():
    """threading 기본"""
    print("=" * 50)
    print("1. threading 기본")
    print("=" * 50)
    
    def worker(name, duration):
        print(f"  {name} 시작")
        time.sleep(duration)
        print(f"  {name} 완료")
    
    # 스레드 생성 및 시작
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(f"작업{i+1}", 1))
        threads.append(thread)
        thread.start()
    
    # 모든 스레드 완료 대기
    for thread in threads:
        thread.join()
    
    print()


def demonstrate_thread_pool():
    """ThreadPoolExecutor"""
    print("=" * 50)
    print("2. ThreadPoolExecutor")
    print("=" * 50)
    
    def task(n):
        time.sleep(0.5)
        return n * n
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        
        for future in as_completed(futures):
            result = future.result()
            print(f"  결과: {result}")
    
    print()


def demonstrate_lock():
    """threading.Lock"""
    print("=" * 50)
    print("3. threading.Lock")
    print("=" * 50)
    
    counter = 0
    lock = threading.Lock()
    
    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1
    
    threads = [threading.Thread(target=increment) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    print(f"  최종 카운터: {counter:,}")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 멀티스레딩".center(50, "="))
    print()
    
    demonstrate_threading()
    demonstrate_thread_pool()
    demonstrate_lock()
    
    print("=" * 50)
    print("✅ 멀티스레딩 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

