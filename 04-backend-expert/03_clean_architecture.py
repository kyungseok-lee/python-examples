"""
03. Clean Architecture (클린 아키텍처)

계층 분리와 의존성 역전 원칙을 학습합니다.

Python 3.12+ 스타일:
- 타입 힌트: list[X], X | None
- __slots__ 사용으로 메모리 최적화
- Protocol 사용으로 인터페이스 정의
"""

from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol


# ==================== Domain Layer ====================
# 비즈니스 로직과 엔티티 (프레임워크 독립적)


@dataclass(slots=True)
class User:
    """사용자 엔티티 (불변 권장)"""

    id: int | None
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)

    def is_valid_username(self) -> bool:
        """username 검증"""
        return len(self.username) >= 3 and self.username.isalnum()

    def is_valid_email(self) -> bool:
        """email 기본 검증"""
        return "@" in self.email and "." in self.email


# ==================== Repository Interface ====================
# Protocol 사용 (구조적 서브타이핑)


class UserRepository(Protocol):
    """사용자 저장소 인터페이스 (Protocol)"""

    def save(self, user: User) -> User:
        """사용자 저장"""
        ...

    def find_by_id(self, user_id: int) -> User | None:
        """ID로 사용자 조회"""
        ...

    def find_by_email(self, email: str) -> User | None:
        """이메일로 사용자 조회"""
        ...

    def find_all(self) -> list[User]:
        """모든 사용자 조회"""
        ...

    def delete(self, user_id: int) -> bool:
        """사용자 삭제"""
        ...


# ==================== Use Case Layer ====================
# 애플리케이션 비즈니스 로직


class CreateUserError(Exception):
    """사용자 생성 오류"""

    pass


class CreateUserUseCase:
    """사용자 생성 유스케이스"""

    __slots__ = ("_user_repository",)

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def execute(self, username: str, email: str) -> User:
        """사용자 생성 실행"""
        # 비즈니스 로직
        user = User(
            id=None,
            username=username,
            email=email,
        )

        if not user.is_valid_username():
            raise CreateUserError(f"Invalid username: {username}")

        if not user.is_valid_email():
            raise CreateUserError(f"Invalid email: {email}")

        # 중복 체크
        existing = self._user_repository.find_by_email(email)
        if existing is not None:
            raise CreateUserError(f"Email already exists: {email}")

        # 저장
        return self._user_repository.save(user)


class GetUserUseCase:
    """사용자 조회 유스케이스"""

    __slots__ = ("_user_repository",)

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def execute(self, user_id: int) -> User | None:
        """ID로 사용자 조회"""
        return self._user_repository.find_by_id(user_id)


class GetUsersUseCase:
    """사용자 목록 조회 유스케이스"""

    __slots__ = ("_user_repository",)

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def execute(self) -> list[User]:
        """모든 사용자 조회"""
        return self._user_repository.find_all()


# ==================== Infrastructure Layer ====================
# 구체적인 구현 (데이터베이스, 외부 API 등)


class InMemoryUserRepository:
    """메모리 기반 사용자 저장소"""

    __slots__ = ("_users", "_next_id")

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id: int = 1

    def save(self, user: User) -> User:
        """사용자 저장"""
        # 새 ID 할당 (불변 객체이므로 새로 생성)
        saved_user = User(
            id=self._next_id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
        )
        self._users[self._next_id] = saved_user
        self._next_id += 1
        return saved_user

    def find_by_id(self, user_id: int) -> User | None:
        """ID로 사용자 조회"""
        return self._users.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        """이메일로 사용자 조회"""
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def find_all(self) -> list[User]:
        """모든 사용자 조회"""
        return list(self._users.values())

    def delete(self, user_id: int) -> bool:
        """사용자 삭제"""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False


# ==================== Presentation Layer ====================
# API, CLI 등 (FastAPI, Flask 등)


@dataclass(slots=True, frozen=True)
class UserDTO:
    """사용자 응답 DTO"""

    id: int
    username: str
    email: str


class UserController:
    """사용자 컨트롤러"""

    __slots__ = ("_create_user", "_get_user", "_get_users")

    def __init__(
        self,
        create_user_use_case: CreateUserUseCase,
        get_user_use_case: GetUserUseCase,
        get_users_use_case: GetUsersUseCase,
    ) -> None:
        self._create_user = create_user_use_case
        self._get_user = get_user_use_case
        self._get_users = get_users_use_case

    def create_user(self, username: str, email: str) -> UserDTO | dict[str, str]:
        """사용자 생성 API"""
        try:
            user = self._create_user.execute(username, email)
            return UserDTO(id=user.id, username=user.username, email=user.email)
        except CreateUserError as e:
            return {"error": str(e)}

    def get_user(self, user_id: int) -> UserDTO | None:
        """사용자 조회 API"""
        user = self._get_user.execute(user_id)
        if user is None:
            return None
        return UserDTO(id=user.id, username=user.username, email=user.email)

    def get_users(self) -> list[UserDTO]:
        """사용자 목록 조회 API"""
        users = self._get_users.execute()
        return [
            UserDTO(id=u.id, username=u.username, email=u.email)
            for u in users
        ]


# ==================== Dependency Injection ====================
# 의존성 주입 컨테이너


class Container:
    """간단한 DI 컨테이너"""

    __slots__ = ("_user_repository", "_controller")

    def __init__(self) -> None:
        # Infrastructure
        self._user_repository = InMemoryUserRepository()

        # Use Cases
        create_user_uc = CreateUserUseCase(self._user_repository)
        get_user_uc = GetUserUseCase(self._user_repository)
        get_users_uc = GetUsersUseCase(self._user_repository)

        # Presentation
        self._controller = UserController(create_user_uc, get_user_uc, get_users_uc)

    @property
    def controller(self) -> UserController:
        return self._controller


def demonstrate_clean_architecture() -> None:
    """Clean Architecture 데모"""
    print("=" * 50)
    print("Clean Architecture 데모")
    print("=" * 50)

    # DI 컨테이너 초기화
    container = Container()
    controller = container.controller

    # 사용자 생성
    print("\n사용자 생성:")
    result1 = controller.create_user("alice", "alice@example.com")
    print(f"  {result1}")

    result2 = controller.create_user("bob", "bob@example.com")
    print(f"  {result2}")

    # 중복 이메일 시도
    result3 = controller.create_user("alice2", "alice@example.com")
    print(f"  중복 시도: {result3}")

    # 잘못된 username 시도
    result4 = controller.create_user("ab", "ab@example.com")
    print(f"  짧은 이름: {result4}")

    # 사용자 목록 조회
    print("\n사용자 목록:")
    users = controller.get_users()
    for user in users:
        print(f"  {user}")

    # 사용자 단건 조회
    print("\n사용자 조회:")
    user = controller.get_user(1)
    print(f"  ID=1: {user}")

    not_found = controller.get_user(999)
    print(f"  ID=999: {not_found}")

    print("\nClean Architecture 장점:")
    print("  1. 비즈니스 로직이 프레임워크와 독립적")
    print("  2. 테스트 용이 (Mock Repository 사용)")
    print("  3. 데이터베이스 변경 시 Repository만 수정")
    print("  4. 의존성 역전 원칙 (DIP) 적용")
    print("  5. Protocol로 인터페이스 정의 (구조적 서브타이핑)")
    print()


def demonstrate_gc_optimization() -> None:
    """GC 최적화 데모"""
    print("=" * 50)
    print("GC 최적화 관점")
    print("=" * 50)

    import gc
    import sys
    import time

    # __slots__ 사용 전후 비교
    @dataclass
    class UserWithDict:
        id: int
        username: str
        email: str

    @dataclass(slots=True)
    class UserWithSlots:
        id: int
        username: str
        email: str

    n = 10000

    # 메모리 비교
    user_dict = UserWithDict(1, "test", "test@example.com")
    user_slots = UserWithSlots(1, "test", "test@example.com")

    size_dict = sys.getsizeof(user_dict) + sys.getsizeof(user_dict.__dict__)
    size_slots = sys.getsizeof(user_slots)

    print(f"\n단일 객체 메모리:")
    print(f"  __dict__ 사용: ~{size_dict} bytes")
    print(f"  __slots__ 사용: ~{size_slots} bytes")
    print(f"  절약: ~{size_dict - size_slots} bytes/객체")

    # 대량 객체 생성 성능
    gc.disable()
    try:
        start = time.perf_counter()
        users_dict = [UserWithDict(i, f"user{i}", f"u{i}@x.com") for i in range(n)]
        time_dict = time.perf_counter() - start

        start = time.perf_counter()
        users_slots = [UserWithSlots(i, f"user{i}", f"u{i}@x.com") for i in range(n)]
        time_slots = time.perf_counter() - start

        print(f"\n{n}개 객체 생성:")
        print(f"  __dict__ 사용: {time_dict:.4f}초")
        print(f"  __slots__ 사용: {time_slots:.4f}초")
        print(f"  성능 향상: {time_dict / time_slots:.2f}x")

    finally:
        gc.enable()
        gc.collect()

    print()


def main() -> None:
    """메인 함수"""
    print("\n" + "🐍 Python 백엔드 전문가 - Clean Architecture".center(50, "="))
    print()

    demonstrate_clean_architecture()
    demonstrate_gc_optimization()

    print("=" * 50)
    print("✅ Clean Architecture 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()
