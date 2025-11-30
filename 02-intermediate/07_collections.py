"""
07. collections 모듈

namedtuple, Counter, defaultdict, deque 등을 학습합니다.
"""

from collections import (
    namedtuple, Counter, defaultdict, 
    deque, OrderedDict, ChainMap
)


def demonstrate_counter():
    """Counter"""
    print("=" * 50)
    print("1. Counter")
    print("=" * 50)
    
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    counter = Counter(words)
    
    print(f"카운터: {counter}")
    print(f"가장 많은 2개: {counter.most_common(2)}")
    print(f"'apple' 개수: {counter['apple']}")
    
    print()


def demonstrate_defaultdict():
    """defaultdict"""
    print("=" * 50)
    print("2. defaultdict")
    print("=" * 50)
    
    # 리스트를 기본값으로
    dd = defaultdict(list)
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    dd['vegetables'].append('carrot')
    
    print(f"defaultdict: {dict(dd)}")
    
    # 카운터로 사용
    dd_count = defaultdict(int)
    for word in ['a', 'b', 'a', 'c', 'b', 'a']:
        dd_count[word] += 1
    
    print(f"카운터: {dict(dd_count)}")
    
    print()


def demonstrate_deque():
    """deque (양방향 큐)"""
    print("=" * 50)
    print("3. deque")
    print("=" * 50)
    
    dq = deque([1, 2, 3])
    
    dq.append(4)  # 오른쪽 추가
    dq.appendleft(0)  # 왼쪽 추가
    print(f"추가 후: {dq}")
    
    dq.pop()  # 오른쪽 제거
    dq.popleft()  # 왼쪽 제거
    print(f"제거 후: {dq}")
    
    # 회전
    dq.rotate(1)  # 오른쪽으로 회전
    print(f"회전 후: {dq}")
    
    print()


def demonstrate_namedtuple():
    """namedtuple"""
    print("=" * 50)
    print("4. namedtuple")
    print("=" * 50)
    
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    
    print(f"포인트: {p}")
    print(f"x={p.x}, y={p.y}")
    print(f"인덱스 접근: p[0]={p[0]}, p[1]={p[1]}")
    
    # _asdict()
    print(f"딕셔너리로 변환: {p._asdict()}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - collections 모듈".center(50, "="))
    print()
    
    demonstrate_counter()
    demonstrate_defaultdict()
    demonstrate_deque()
    demonstrate_namedtuple()
    
    print("=" * 50)
    print("✅ collections 모듈 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

