"""
06. 자료구조 (Data Structures)

list, tuple, dict, set 등의 내장 자료구조를 학습합니다.
"""


def demonstrate_lists():
    """리스트 (List)"""
    print("=" * 50)
    print("1. 리스트 (List)")
    print("=" * 50)
    
    # 생성
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True, None]
    
    print(f"과일: {fruits}")
    print(f"숫자: {numbers}")
    print(f"혼합: {mixed}")
    
    # 인덱싱
    print(f"\n첫 번째 과일: {fruits[0]}")
    print(f"마지막 과일: {fruits[-1]}")
    
    # 슬라이싱
    print(f"슬라이싱 [1:3]: {numbers[1:3]}")
    print(f"슬라이싱 [:3]: {numbers[:3]}")
    print(f"슬라이싱 [2:]: {numbers[2:]}")
    print(f"슬라이싱 [::2]: {numbers[::2]}")  # 2칸씩
    print(f"역순 [::-1]: {numbers[::-1]}")
    
    # 수정
    fruits[1] = "blueberry"
    print(f"\n수정 후: {fruits}")
    
    # 추가
    fruits.append("mango")
    print(f"append 후: {fruits}")
    
    fruits.insert(1, "orange")
    print(f"insert 후: {fruits}")
    
    # 삭제
    fruits.remove("cherry")
    print(f"remove 후: {fruits}")
    
    popped = fruits.pop()
    print(f"pop 후: {fruits}, 제거된 항목: {popped}")
    
    # 기타 메서드
    numbers_copy = [3, 1, 4, 1, 5, 9, 2]
    numbers_copy.sort()
    print(f"\nsort 후: {numbers_copy}")
    
    numbers_copy.reverse()
    print(f"reverse 후: {numbers_copy}")
    
    count = [1, 2, 2, 3, 2].count(2)
    print(f"count(2): {count}")
    
    print()


def demonstrate_tuples():
    """튜플 (Tuple)"""
    print("=" * 50)
    print("2. 튜플 (Tuple) - 불변 시퀀스")
    print("=" * 50)
    
    # 생성
    coordinates = (10, 20)
    rgb = (255, 128, 0)
    single = (42,)  # 하나의 요소는 쉼표 필요
    
    print(f"좌표: {coordinates}")
    print(f"RGB: {rgb}")
    print(f"단일 요소: {single}")
    
    # 언패킹
    x, y = coordinates
    print(f"x={x}, y={y}")
    
    # 튜플은 불변
    try:
        coordinates[0] = 15
    except TypeError as e:
        print(f"\n수정 불가: {e}")
    
    # 용도: 여러 값 반환
    def get_min_max(numbers):
        return min(numbers), max(numbers)
    
    minimum, maximum = get_min_max([1, 5, 3, 9, 2])
    print(f"\nmin={minimum}, max={maximum}")
    
    # 튜플 메서드
    values = (1, 2, 2, 3, 2, 4)
    print(f"\ncount(2): {values.count(2)}")
    print(f"index(3): {values.index(3)}")
    
    print()


def demonstrate_dictionaries():
    """딕셔너리 (Dictionary)"""
    print("=" * 50)
    print("3. 딕셔너리 (Dictionary)")
    print("=" * 50)
    
    # 생성
    user = {
        "name": "Alice",
        "age": 25,
        "city": "Seoul"
    }
    
    print(f"사용자: {user}")
    
    # 접근
    print(f"이름: {user['name']}")
    print(f"나이: {user.get('age')}")
    print(f"이메일: {user.get('email', 'N/A')}")  # 기본값
    
    # 수정/추가
    user["age"] = 26
    user["email"] = "alice@example.com"
    print(f"\n수정 후: {user}")
    
    # 삭제
    del user["city"]
    print(f"삭제 후: {user}")
    
    email = user.pop("email")
    print(f"pop 후: {user}, 제거된 값: {email}")
    
    # 순회
    print("\nkeys():")
    for key in user.keys():
        print(f"  {key}")
    
    print("\nvalues():")
    for value in user.values():
        print(f"  {value}")
    
    print("\nitems():")
    for key, value in user.items():
        print(f"  {key}: {value}")
    
    # 병합 (Python 3.9+)
    defaults = {"role": "user", "active": True}
    user = {**defaults, **user}
    print(f"\n병합 후: {user}")
    
    # update
    user.update({"name": "Alice Smith", "age": 27})
    print(f"update 후: {user}")
    
    print()


def demonstrate_sets():
    """셋 (Set)"""
    print("=" * 50)
    print("4. 셋 (Set) - 중복 없는 집합")
    print("=" * 50)
    
    # 생성
    fruits = {"apple", "banana", "cherry"}
    numbers = {1, 2, 3, 3, 4, 4, 5}  # 중복 자동 제거
    
    print(f"과일: {fruits}")
    print(f"숫자 (중복 제거): {numbers}")
    
    # 추가/삭제
    fruits.add("mango")
    print(f"add 후: {fruits}")
    
    fruits.remove("banana")
    print(f"remove 후: {fruits}")
    
    # 집합 연산
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"\nset1: {set1}")
    print(f"set2: {set2}")
    print(f"합집합 (|): {set1 | set2}")
    print(f"교집합 (&): {set1 & set2}")
    print(f"차집합 (-): {set1 - set2}")
    print(f"대칭차 (^): {set1 ^ set2}")
    
    # 부분집합/상위집합
    subset = {1, 2, 3}
    print(f"\n{subset} ⊂ {set1}: {subset.issubset(set1)}")
    print(f"{set1} ⊃ {subset}: {set1.issuperset(subset)}")
    
    # 활용: 중복 제거
    numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = list(set(numbers_with_duplicates))
    print(f"\n중복 제거: {numbers_with_duplicates} -> {unique_numbers}")
    
    print()


def demonstrate_list_methods():
    """리스트 고급 메서드"""
    print("=" * 50)
    print("5. 리스트 고급 메서드")
    print("=" * 50)
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # extend vs append
    list1 = [1, 2, 3]
    list1.append([4, 5])
    print(f"append [4, 5]: {list1}")
    
    list2 = [1, 2, 3]
    list2.extend([4, 5])
    print(f"extend [4, 5]: {list2}")
    
    # clear
    temp = [1, 2, 3]
    temp.clear()
    print(f"clear: {temp}")
    
    # copy (얕은 복사)
    original = [1, 2, [3, 4]]
    shallow = original.copy()
    shallow[0] = 99
    shallow[2][0] = 99
    print(f"\n원본: {original}")
    print(f"복사본: {shallow}")
    
    # 깊은 복사
    import copy
    original = [1, 2, [3, 4]]
    deep = copy.deepcopy(original)
    deep[2][0] = 99
    print(f"\n깊은 복사 - 원본: {original}")
    print(f"깊은 복사 - 복사본: {deep}")
    
    print()


def demonstrate_dict_methods():
    """딕셔너리 고급 메서드"""
    print("=" * 50)
    print("6. 딕셔너리 고급 메서드")
    print("=" * 50)
    
    # setdefault
    user = {"name": "Alice"}
    age = user.setdefault("age", 25)  # 없으면 추가하고 값 반환
    print(f"setdefault: {user}, age={age}")
    
    # fromkeys
    keys = ["name", "age", "city"]
    template = dict.fromkeys(keys, "N/A")
    print(f"fromkeys: {template}")
    
    # popitem (Python 3.7+: LIFO)
    data = {"a": 1, "b": 2, "c": 3}
    item = data.popitem()
    print(f"popitem: {data}, removed={item}")
    
    # get vs []
    user = {"name": "Bob"}
    print(f"\nget('email', 'N/A'): {user.get('email', 'N/A')}")
    try:
        print(user["email"])
    except KeyError as e:
        print(f"KeyError: {e}")
    
    print()


def demonstrate_collections_module():
    """collections 모듈"""
    print("=" * 50)
    print("7. collections 모듈")
    print("=" * 50)
    
    from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
    
    # Counter
    print("Counter:")
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counter = Counter(words)
    print(f"  {counter}")
    print(f"  most_common(2): {counter.most_common(2)}")
    
    # defaultdict
    print("\ndefaultdict:")
    dd = defaultdict(list)
    dd["fruits"].append("apple")
    dd["fruits"].append("banana")
    print(f"  {dict(dd)}")
    
    # deque (양방향 큐)
    print("\ndeque:")
    dq = deque([1, 2, 3])
    dq.append(4)  # 오른쪽 추가
    dq.appendleft(0)  # 왼쪽 추가
    print(f"  {dq}")
    print(f"  pop(): {dq.pop()}")  # 오른쪽 제거
    print(f"  popleft(): {dq.popleft()}")  # 왼쪽 제거
    print(f"  {dq}")
    
    # namedtuple
    print("\nnamedtuple:")
    Point = namedtuple("Point", ["x", "y"])
    p = Point(10, 20)
    print(f"  {p}")
    print(f"  x={p.x}, y={p.y}")
    
    print()


def demonstrate_list_performance():
    """리스트 성능 비교"""
    print("=" * 50)
    print("8. 리스트 성능 고려사항")
    print("=" * 50)
    
    import time
    
    # append vs insert(0)
    n = 10000
    
    # append (O(1))
    start = time.perf_counter()
    lst = []
    for i in range(n):
        lst.append(i)
    append_time = time.perf_counter() - start
    
    # insert(0) (O(n))
    start = time.perf_counter()
    lst = []
    for i in range(n):
        lst.insert(0, i)
    insert_time = time.perf_counter() - start
    
    print(f"append {n}회: {append_time:.4f}초")
    print(f"insert(0) {n}회: {insert_time:.4f}초")
    print(f"insert가 약 {insert_time/append_time:.1f}배 느림")
    
    # in 연산: list vs set
    items_list = list(range(10000))
    items_set = set(range(10000))
    target = 9999
    
    start = time.perf_counter()
    _ = target in items_list
    list_time = time.perf_counter() - start
    
    start = time.perf_counter()
    _ = target in items_set
    set_time = time.perf_counter() - start
    
    print(f"\n'in' 연산 (10000개):")
    print(f"  list: {list_time:.6f}초")
    print(f"  set: {set_time:.6f}초")
    print(f"  set이 약 {list_time/set_time:.0f}배 빠름")
    
    print()


def demonstrate_nested_structures():
    """중첩 자료구조"""
    print("=" * 50)
    print("9. 중첩 자료구조")
    print("=" * 50)
    
    # 리스트의 리스트
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("행렬:")
    for row in matrix:
        print(f"  {row}")
    
    # 딕셔너리의 리스트
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35}
    ]
    print("\n사용자 목록:")
    for user in users:
        print(f"  {user['name']}: {user['age']}세")
    
    # 리스트의 딕셔너리
    groups = {
        "developers": ["Alice", "Bob"],
        "designers": ["Charlie", "David"],
        "managers": ["Eve"]
    }
    print("\n그룹:")
    for group, members in groups.items():
        print(f"  {group}: {', '.join(members)}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 자료구조".center(50, "="))
    print()
    
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    demonstrate_list_methods()
    demonstrate_dict_methods()
    demonstrate_collections_module()
    demonstrate_list_performance()
    demonstrate_nested_structures()
    
    print("=" * 50)
    print("✅ 자료구조 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

