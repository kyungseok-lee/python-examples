"""
02. Pydantic 모델 (Pydantic Models)

Pydantic v2를 사용한 데이터 검증과 시리얼라이제이션을 학습합니다.

주요 변경사항 (Pydantic v1 → v2):
- validator → field_validator
- root_validator → model_validator
- .dict() → .model_dump()
- .json() → .model_dump_json()
- Config 클래스 → model_config
- .copy() → .model_copy()
"""

from __future__ import annotations

import json
from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)


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
    postal_code: str | None = None


class User(BaseModel):
    """사용자 모델 (Pydantic v2)"""

    model_config = ConfigDict(
        # JSON 인코딩 설정
        json_encoders={datetime: lambda v: v.isoformat()},
        # 추가 필드 무시
        extra="ignore",
        # 문자열 앞뒤 공백 제거
        str_strip_whitespace=True,
    )

    id: int
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: int | None = Field(None, ge=0, le=150)
    role: UserRole = UserRole.USER
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    address: Address | None = None

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """username은 영숫자만 허용"""
        if not v.isalnum():
            raise ValueError("username must be alphanumeric")
        return v

    @field_validator("age")
    @classmethod
    def age_must_be_adult(cls, v: int | None) -> int | None:
        """나이는 18세 이상"""
        if v is not None and v < 18:
            raise ValueError("age must be at least 18")
        return v

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        """모델 전체 검증"""
        # 예: ADMIN 역할은 이메일 도메인 검증
        if self.role == UserRole.ADMIN and not self.email.endswith("@admin.com"):
            # 경고만 출력 (실제로는 로깅 사용)
            pass
        return self


def demonstrate_basic_validation() -> None:
    """기본 검증"""
    print("=" * 50)
    print("1. 기본 검증 (Pydantic v2)")
    print("=" * 50)

    # 올바른 데이터
    user = User(
        id=1,
        username="alice",
        email="alice@example.com",
        age=25,
    )
    print(f"사용자: {user}")
    print(f"JSON: {user.model_dump_json(indent=2)}")

    # 검증 실패
    try:
        User(
            id=2,
            username="ab",  # 너무 짧음
            email="invalid-email",  # 잘못된 이메일
        )
    except Exception as e:
        print(f"\n검증 오류: {e}")

    print()


def demonstrate_nested_models() -> None:
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
            postal_code="12345",
        ),
    )

    print(f"사용자: {user_with_address}")
    if user_with_address.address:
        print(f"도시: {user_with_address.address.city}")

    print()


def demonstrate_model_operations() -> None:
    """모델 연산 (Pydantic v2)"""
    print("=" * 50)
    print("3. 모델 연산 (Pydantic v2)")
    print("=" * 50)

    user = User(
        id=1,
        username="charlie",
        email="charlie@example.com",
        age=28,
    )

    # dict로 변환 (v2: model_dump)
    user_dict = user.model_dump()
    print(f"dict: {user_dict}")

    # JSON으로 변환 (v2: model_dump_json)
    user_json = user.model_dump_json()
    print(f"JSON: {user_json}")

    # dict에서 생성
    new_user = User(**user_dict)
    print(f"복원: {new_user}")

    # 부분 업데이트 (v2: model_copy)
    updated_user = user.model_copy(update={"age": 29, "role": UserRole.ADMIN})
    print(f"업데이트: {updated_user}")

    # exclude/include 옵션
    partial_dict = user.model_dump(exclude={"created_at", "is_active"})
    print(f"부분 dict: {partial_dict}")

    print()


def demonstrate_serialization_modes() -> None:
    """직렬화 모드 (Pydantic v2)"""
    print("=" * 50)
    print("4. 직렬화 모드 (Pydantic v2)")
    print("=" * 50)

    user = User(
        id=1,
        username="david",
        email="david@example.com",
        age=35,
        role=UserRole.ADMIN,
    )

    # 기본 모드 (python 객체)
    print(f"Python 모드: {user.model_dump(mode='python')}")

    # JSON 호환 모드 (문자열/숫자만)
    print(f"JSON 모드: {user.model_dump(mode='json')}")

    # by_alias 옵션
    print(f"JSON string: {user.model_dump_json(indent=2)}")

    print()


def demonstrate_validation_performance() -> None:
    """검증 성능 (GC 관점)"""
    print("=" * 50)
    print("5. 검증 성능 (GC 관점)")
    print("=" * 50)

    import gc
    import time

    # GC 비활성화로 순수 검증 시간 측정
    gc.disable()
    try:
        start = time.perf_counter()

        # 대량 객체 생성
        users: list[User] = []
        for i in range(1000):
            users.append(
                User(
                    id=i,
                    username=f"user{i:04d}",
                    email=f"user{i}@example.com",
                    age=20 + (i % 50),
                )
            )

        creation_time = time.perf_counter() - start
        print(f"1000개 User 생성: {creation_time:.4f}초")

        # 직렬화 성능
        start = time.perf_counter()
        for user in users:
            _ = user.model_dump()
        dump_time = time.perf_counter() - start
        print(f"1000개 model_dump: {dump_time:.4f}초")

        # 메모리 정리
        del users

    finally:
        gc.enable()
        gc.collect()

    print()


def main() -> None:
    """메인 함수"""
    print("\n" + "🐍 Python 백엔드 전문가 - Pydantic v2 모델".center(50, "="))
    print()

    demonstrate_basic_validation()
    demonstrate_nested_models()
    demonstrate_model_operations()
    demonstrate_serialization_modes()
    demonstrate_validation_performance()

    print("=" * 50)
    print("✅ Pydantic v2 모델 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()
