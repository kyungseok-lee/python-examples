"""
01. 비동기 프로그래밍 (Async Programming)

async/await와 asyncio를 사용한 비동기 프로그래밍을 학습합니다.
"""

import asyncio
import time


async def demonstrate_basic_async():
    """기본 async/await"""
    print("=" * 50)
    print("1. 기본 async/await")
    print("=" * 50)
    
    async def fetch_data(name, delay):
        print(f"  {name} 시작")
        await asyncio.sleep(delay)
        print(f"  {name} 완료")
        return f"{name} 데이터"
    
    # 순차 실행
    start = time.perf_counter()
    result1 = await fetch_data("작업A", 1)
    result2 = await fetch_data("작업B", 1)
    end = time.perf_counter()
    
    print(f"순차 실행 시간: {end - start:.2f}초")
    print()


async def demonstrate_gather():
    """asyncio.gather - 병렬 실행"""
    print("=" * 50)
    print("2. asyncio.gather")
    print("=" * 50)
    
    async def fetch_data(name, delay):
        await asyncio.sleep(delay)
        return f"{name} 완료"
    
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch_data("작업A", 1),
        fetch_data("작업B", 1),
        fetch_data("작업C", 1)
    )
    end = time.perf_counter()
    
    print(f"  결과: {results}")
    print(f"  병렬 실행 시간: {end - start:.2f}초")
    print()


async def demonstrate_create_task():
    """asyncio.create_task"""
    print("=" * 50)
    print("3. asyncio.create_task")
    print("=" * 50)
    
    async def say_after(delay, message):
        await asyncio.sleep(delay)
        print(f"  {message}")
        return message
    
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    
    await task1
    await task2
    
    print()


async def main():
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 비동기 프로그래밍".center(50, "="))
    print()
    
    await demonstrate_basic_async()
    await demonstrate_gather()
    await demonstrate_create_task()
    
    print("=" * 50)
    print("✅ 비동기 프로그래밍 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

