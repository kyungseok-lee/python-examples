"""
03. 타입 힌팅 (Type Hints)

typing 모듈을 사용한 타입 힌팅을 학습합니다.
"""

from typing import List, Dict, Optional, Union, Tuple, Callable, TypeVar, Generic


def demonstrate_basic_types():
    """기본 타입 힌팅"""
    print("=" * 50)
    print("1. 기본 타입 힌팅")
    print("=" * 50)
    
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    def add(a: int, b: int) -> int:
        return a + b
    
    print(f"  {greet('Alice')}")
    print(f"  {add(10, 20)}")
    print()


def demonstrate_collection_types():
    """컬렉션 타입"""
    print("=" * 50)
    print("2. 컬렉션 타입")
    print("=" * 50)
    
    def process_numbers(numbers: List[int]) -> List[int]:
        return [n * 2 for n in numbers]
    
    def get_user_info(user_id: int) -> Dict[str, Union[str, int]]:
        return {"id": user_id, "name": "Alice", "age": 25}
    
    print(f"  {process_numbers([1, 2, 3])}")
    print(f"  {get_user_info(1)}")
    print()


def demonstrate_optional():
    """Optional 타입"""
    print("=" * 50)
    print("3. Optional 타입")
    print("=" * 50)
    
    def find_user(user_id: int) -> Optional[Dict[str, str]]:
        if user_id == 1:
            return {"name": "Alice"}
        return None
    
    user = find_user(1)
    print(f"  사용자: {user}")
    
    no_user = find_user(999)
    print(f"  없는 사용자: {no_user}")
    print()


def demonstrate_generic():
    """제네릭 타입"""
    print("=" * 50)
    print("4. 제네릭 타입")
    print("=" * 50)
    
    T = TypeVar('T')
    
    class Stack(Generic[T]):
        def __init__(self):
            self.items: List[T] = []
        
        def push(self, item: T) -> None:
            self.items.append(item)
        
        def pop(self) -> T:
            return self.items.pop()
    
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    print(f"  Pop: {int_stack.pop()}")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 타입 힌팅".center(50, "="))
    print()
    
    demonstrate_basic_types()
    demonstrate_collection_types()
    demonstrate_optional()
    demonstrate_generic()
    
    print("=" * 50)
    print("✅ 타입 힌팅 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

