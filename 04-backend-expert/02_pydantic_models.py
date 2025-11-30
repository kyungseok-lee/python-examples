"""
02. Pydantic 모델 (Pydantic Models)

Pydantic을 사용한 데이터 검증과 시리얼라이제이션을 학습합니다.
"""

from pydantic import BaseModel, Field, EmailStr, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    """사용자 역할"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class Address(BaseModel):
    """주소 모델"""
    street: str
    city: str
    country: str = "Korea"
    postal_code: Optional[str] = None


class User(BaseModel):
    """사용자 모델"""
    id: int
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    role: UserRole = UserRole.USER
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    address: Optional[Address] = None
    
    @validator('username')
    def username_alphanumeric(cls, v):
        """username은 영숫자만 허용"""
        if not v.isalnum():
            raise ValueError('username must be alphanumeric')
        return v
    
    @validator('age')
    def age_must_be_adult(cls, v):
        """나이는 18세 이상"""
        if v is not None and v < 18:
            raise ValueError('age must be at least 18')
        return v
    
    class Config:
        """Pydantic 설정"""
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


def demonstrate_basic_validation():
    """기본 검증"""
    print("=" * 50)
    print("1. 기본 검증")
    print("=" * 50)
    
    # 올바른 데이터
    user = User(
        id=1,
        username="alice",
        email="alice@example.com",
        age=25
    )
    print(f"사용자: {user}")
    print(f"JSON: {user.json(indent=2)}")
    
    # 검증 실패
    try:
        invalid_user = User(
            id=2,
            username="ab",  # 너무 짧음
            email="invalid-email"
        )
    except Exception as e:
        print(f"\n검증 오류: {e}")
    
    print()


def demonstrate_nested_models():
    """중첩 모델"""
    print("=" * 50)
    print("2. 중첩 모델")
    print("=" * 50)
    
    user_with_address = User(
        id=1,
        username="bob",
        email="bob@example.com",
        age=30,
        address=Address(
            street="123 Main St",
            city="Seoul",
            postal_code="12345"
        )
    )
    
    print(f"사용자: {user_with_address}")
    print(f"도시: {user_with_address.address.city}")
    
    print()


def demonstrate_model_operations():
    """모델 연산"""
    print("=" * 50)
    print("3. 모델 연산")
    print("=" * 50)
    
    user = User(
        id=1,
        username="charlie",
        email="charlie@example.com",
        age=28
    )
    
    # dict로 변환
    user_dict = user.dict()
    print(f"dict: {user_dict}")
    
    # JSON으로 변환
    user_json = user.json()
    print(f"JSON: {user_json}")
    
    # dict에서 생성
    new_user = User(**user_dict)
    print(f"복원: {new_user}")
    
    # 부분 업데이트
    updated_user = user.copy(update={"age": 29, "role": UserRole.ADMIN})
    print(f"업데이트: {updated_user}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 백엔드 전문가 - Pydantic 모델".center(50, "="))
    print()
    
    demonstrate_basic_validation()
    demonstrate_nested_models()
    demonstrate_model_operations()
    
    print("=" * 50)
    print("✅ Pydantic 모델 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

