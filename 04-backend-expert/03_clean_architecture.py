"""
03. Clean Architecture (클린 아키텍처)

계층 분리와 의존성 역전 원칙을 학습합니다.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime


# ==================== Domain Layer ====================
# 비즈니스 로직과 엔티티 (프레임워크 독립적)

@dataclass
class User:
    """사용자 엔티티"""
    id: Optional[int]
    username: str
    email: str
    created_at: datetime
    
    def is_valid_username(self) -> bool:
        """username 검증"""
        return len(self.username) >= 3


# ==================== Repository Interface ====================
# 추상화 (의존성 역전)

class UserRepository(ABC):
    """사용자 저장소 인터페이스"""
    
    @abstractmethod
    def save(self, user: User) -> User:
        """사용자 저장"""
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        """ID로 사용자 조회"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[User]:
        """모든 사용자 조회"""
        pass


# ==================== Use Case Layer ====================
# 애플리케이션 비즈니스 로직

class CreateUserUseCase:
    """사용자 생성 유스케이스"""
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self, username: str, email: str) -> User:
        """사용자 생성 실행"""
        # 비즈니스 로직
        user = User(
            id=None,
            username=username,
            email=email,
            created_at=datetime.now()
        )
        
        if not user.is_valid_username():
            raise ValueError("Invalid username")
        
        # 저장
        return self.user_repository.save(user)


class GetUsersUseCase:
    """사용자 목록 조회 유스케이스"""
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self) -> List[User]:
        """모든 사용자 조회"""
        return self.user_repository.find_all()


# ==================== Infrastructure Layer ====================
# 구체적인 구현 (데이터베이스, 외부 API 등)

class InMemoryUserRepository(UserRepository):
    """메모리 기반 사용자 저장소"""
    
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1
    
    def save(self, user: User) -> User:
        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def find_all(self) -> List[User]:
        return self.users.copy()


# ==================== Presentation Layer ====================
# API, CLI 등 (FastAPI, Flask 등)

class UserController:
    """사용자 컨트롤러"""
    
    def __init__(
        self,
        create_user_use_case: CreateUserUseCase,
        get_users_use_case: GetUsersUseCase
    ):
        self.create_user_use_case = create_user_use_case
        self.get_users_use_case = get_users_use_case
    
    def create_user(self, username: str, email: str):
        """사용자 생성 API"""
        user = self.create_user_use_case.execute(username, email)
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    
    def get_users(self):
        """사용자 목록 조회 API"""
        users = self.get_users_use_case.execute()
        return [
            {
                "id": u.id,
                "username": u.username,
                "email": u.email
            }
            for u in users
        ]


def demonstrate_clean_architecture():
    """Clean Architecture 데모"""
    print("=" * 50)
    print("Clean Architecture 데모")
    print("=" * 50)
    
    # 의존성 주입 (DI Container)
    user_repository = InMemoryUserRepository()
    create_user_use_case = CreateUserUseCase(user_repository)
    get_users_use_case = GetUsersUseCase(user_repository)
    controller = UserController(create_user_use_case, get_users_use_case)
    
    # 사용자 생성
    print("\n사용자 생성:")
    user1 = controller.create_user("alice", "alice@example.com")
    print(f"  {user1}")
    
    user2 = controller.create_user("bob", "bob@example.com")
    print(f"  {user2}")
    
    # 사용자 목록 조회
    print("\n사용자 목록:")
    users = controller.get_users()
    for user in users:
        print(f"  {user}")
    
    print("\nClean Architecture 장점:")
    print("  1. 비즈니스 로직이 프레임워크와 독립적")
    print("  2. 테스트 용이 (Mock Repository 사용)")
    print("  3. 데이터베이스 변경 시 Repository만 수정")
    print("  4. 의존성 역전 원칙 (DIP) 적용")
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 백엔드 전문가 - Clean Architecture".center(50, "="))
    print()
    
    demonstrate_clean_architecture()
    
    print("=" * 50)
    print("✅ Clean Architecture 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

