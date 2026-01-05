"""
03. 타입 힌팅 (Type Hints)

Python 3.12+ 스타일의 타입 힌팅을 학습합니다.

Python 3.9+: list[int], dict[str, int] 등 내장 타입 사용 가능
Python 3.10+: X | None, X | Y 유니온 문법
Python 3.12+: type 키워드, Generic 개선
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeAlias, TypeVar

# TYPE_CHECKING은 런타임에 False, 타입 체커에서만 True
if TYPE_CHECKING:
    pass


def demonstrate_basic_types() -> None:
    """기본 타입 힌팅 (Python 3.12 스타일)"""
    print("=" * 50)
    print("1. 기본 타입 힌팅 (Python 3.12 스타일)")
    print("=" * 50)

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    def add(a: int, b: int) -> int:
        return a + b

    # Python 3.12: 타입 파라미터 문법 (PEP 695)
    # def generic_func[T](item: T) -> T:
    #     return item

    print(f"  {greet('Alice')}")
    print(f"  {add(10, 20)}")
    print()


def demonstrate_collection_types() -> None:
    """컬렉션 타입 (Python 3.9+ 스타일)"""
    print("=" * 50)
    print("2. 컬렉션 타입 (내장 타입 사용)")
    print("=" * 50)

    # Python 3.9+: typing.List 대신 list 사용
    def process_numbers(numbers: list[int]) -> list[int]:
        return [n * 2 for n in numbers]

    # Python 3.10+: Union 대신 | 사용
    def get_user_info(user_id: int) -> dict[str, str | int]:
        return {"id": user_id, "name": "Alice", "age": 25}

    # Sequence: 읽기 전용 시퀀스 (list, tuple 모두 가능)
    def sum_sequence(items: Sequence[int]) -> int:
        return sum(items)

    print(f"  {process_numbers([1, 2, 3])}")
    print(f"  {get_user_info(1)}")
    print(f"  {sum_sequence([1, 2, 3])}")
    print(f"  {sum_sequence((1, 2, 3))}")
    print()


def demonstrate_optional() -> None:
    """Optional 타입 (Python 3.10+ 스타일)"""
    print("=" * 50)
    print("3. Optional 타입 (X | None)")
    print("=" * 50)

    # Python 3.10+: Optional[X] 대신 X | None 사용
    def find_user(user_id: int) -> dict[str, str] | None:
        if user_id == 1:
            return {"name": "Alice"}
        return None

    user = find_user(1)
    print(f"  사용자: {user}")

    no_user = find_user(999)
    print(f"  없는 사용자: {no_user}")
    print()


def demonstrate_type_alias() -> None:
    """타입 별칭 (TypeAlias)"""
    print("=" * 50)
    print("4. 타입 별칭")
    print("=" * 50)

    # Python 3.10+: TypeAlias 명시적 선언
    UserDict: TypeAlias = dict[str, str | int]
    UserList: TypeAlias = list[UserDict]

    # Python 3.12+: type 키워드 (권장)
    # type UserDict = dict[str, str | int]
    # type UserList = list[UserDict]

    def get_users() -> UserList:
        return [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
        ]

    users = get_users()
    print(f"  사용자 목록: {users}")
    print()


def demonstrate_callable() -> None:
    """Callable 타입"""
    print("=" * 50)
    print("5. Callable 타입")
    print("=" * 50)

    # collections.abc.Callable 사용 (typing.Callable 대신)
    def apply_operation(
        x: int,
        y: int,
        operation: Callable[[int, int], int],
    ) -> int:
        return operation(x, y)

    def multiply(a: int, b: int) -> int:
        return a * b

    result = apply_operation(5, 3, multiply)
    print(f"  5 * 3 = {result}")

    # 람다도 가능
    result = apply_operation(10, 4, lambda a, b: a - b)
    print(f"  10 - 4 = {result}")
    print()


def demonstrate_generic() -> None:
    """제네릭 타입 (Python 3.12 스타일)"""
    print("=" * 50)
    print("6. 제네릭 타입")
    print("=" * 50)

    T = TypeVar("T")

    # 기존 방식 (Python 3.11 이하)
    class Stack(Generic[T]):
        """제네릭 스택"""

        __slots__ = ("_items",)  # 메모리 최적화

        def __init__(self) -> None:
            self._items: list[T] = []

        def push(self, item: T) -> None:
            self._items.append(item)

        def pop(self) -> T:
            return self._items.pop()

        def is_empty(self) -> bool:
            return len(self._items) == 0

        def __len__(self) -> int:
            return len(self._items)

    # Python 3.12+: 새로운 문법 (PEP 695)
    # class Stack[T]:
    #     def __init__(self) -> None:
    #         self._items: list[T] = []
    #     ...

    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    print(f"  Pop: {int_stack.pop()}")
    print(f"  Length: {len(int_stack)}")
    print()


def demonstrate_protocol() -> None:
    """Protocol (구조적 서브타이핑)"""
    print("=" * 50)
    print("7. Protocol (덕 타이핑)")
    print("=" * 50)

    from typing import Protocol

    class Drawable(Protocol):
        """그릴 수 있는 객체"""

        def draw(self) -> str: ...

    @dataclass(slots=True)  # 메모리 최적화
    class Circle:
        radius: float

        def draw(self) -> str:
            return f"Circle(r={self.radius})"

    @dataclass(slots=True)
    class Rectangle:
        width: float
        height: float

        def draw(self) -> str:
            return f"Rectangle({self.width}x{self.height})"

    def render(shape: Drawable) -> None:
        print(f"  Rendering: {shape.draw()}")

    # Circle과 Rectangle은 Drawable을 상속하지 않지만
    # draw() 메서드가 있으므로 Protocol 만족
    render(Circle(5.0))
    render(Rectangle(3.0, 4.0))
    print()


def demonstrate_iterator_types() -> None:
    """Iterator/Generator 타입"""
    print("=" * 50)
    print("8. Iterator/Generator 타입")
    print("=" * 50)

    # Iterator 반환 타입
    def count_up(n: int) -> Iterator[int]:
        """제너레이터 함수"""
        for i in range(n):
            yield i

    # Generator 사용
    print("  Count up to 5:")
    for num in count_up(5):
        print(f"    {num}", end=" ")
    print("\n")


def main() -> None:
    """메인 함수"""
    print("\n" + "🐍 Python 고급 - 타입 힌팅 (3.12 스타일)".center(50, "="))
    print()

    demonstrate_basic_types()
    demonstrate_collection_types()
    demonstrate_optional()
    demonstrate_type_alias()
    demonstrate_callable()
    demonstrate_generic()
    demonstrate_protocol()
    demonstrate_iterator_types()

    print("=" * 50)
    print("✅ 타입 힌팅 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()
