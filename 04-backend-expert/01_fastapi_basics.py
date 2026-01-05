"""
01. FastAPI 기본 (FastAPI Basics)

FastAPI를 사용한 REST API 개발 기초를 학습합니다.

실행 방법:
    uvicorn 01_fastapi_basics:app --reload

API 문서:
    http://localhost:8000/docs

Python 3.12+ 스타일 적용:
- 타입 힌트: list[X], dict[X, Y], X | None
- Pydantic v2 문법 사용
"""

from __future__ import annotations

from fastapi import Body, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, ConfigDict, Field


app = FastAPI(
    title="Python Backend Expert API",
    description="FastAPI 기본 예제 (Python 3.12+, Pydantic v2)",
    version="2.0.0",
)


# ============================================================
# Pydantic 모델 (v2 스타일)
# ============================================================


class ItemCreate(BaseModel):
    """아이템 생성 요청"""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    is_available: bool = True


class ItemResponse(BaseModel):
    """아이템 응답"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    is_available: bool = True


class ItemUpdate(BaseModel):
    """아이템 수정 요청 (부분 업데이트)"""

    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None
    price: float | None = Field(None, gt=0)
    is_available: bool | None = None


class MessageResponse(BaseModel):
    """메시지 응답"""

    message: str
    version: str = "2.0.0"


class HealthResponse(BaseModel):
    """헬스 체크 응답"""

    status: str
    python_version: str = "3.12+"


# ============================================================
# 메모리 저장소 (실제로는 데이터베이스 사용)
# ============================================================


class ItemStore:
    """아이템 저장소 (싱글톤 패턴)"""

    __slots__ = ("_items", "_next_id")

    def __init__(self) -> None:
        self._items: dict[int, ItemResponse] = {}
        self._next_id: int = 1

    def create(self, item: ItemCreate) -> ItemResponse:
        """아이템 생성"""
        item_response = ItemResponse(
            id=self._next_id,
            name=item.name,
            price=item.price,
            is_available=item.is_available,
        )
        self._items[self._next_id] = item_response
        self._next_id += 1
        return item_response

    def get(self, item_id: int) -> ItemResponse | None:
        """아이템 조회"""
        return self._items.get(item_id)

    def list_all(self, skip: int = 0, limit: int = 10) -> list[ItemResponse]:
        """아이템 목록 조회"""
        items = list(self._items.values())
        return items[skip : skip + limit]

    def update(self, item_id: int, item: ItemUpdate) -> ItemResponse | None:
        """아이템 수정"""
        existing = self._items.get(item_id)
        if existing is None:
            return None

        update_data = item.model_dump(exclude_unset=True)
        updated = existing.model_copy(update=update_data)
        self._items[item_id] = updated
        return updated

    def delete(self, item_id: int) -> bool:
        """아이템 삭제"""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False

    def count(self) -> int:
        """아이템 개수"""
        return len(self._items)


# 전역 저장소 인스턴스
item_store = ItemStore()


# ============================================================
# API 엔드포인트
# ============================================================


@app.get("/", response_model=MessageResponse)
async def root() -> MessageResponse:
    """루트 엔드포인트"""
    return MessageResponse(
        message="Python Backend Expert API",
    )


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """헬스 체크"""
    return HealthResponse(status="healthy")


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate) -> ItemResponse:
    """아이템 생성"""
    return item_store.create(item)


@app.get("/items", response_model=list[ItemResponse])
async def list_items(
    skip: int = Query(0, ge=0, description="건너뛸 항목 수"),
    limit: int = Query(10, ge=1, le=100, description="조회할 항목 수"),
) -> list[ItemResponse]:
    """아이템 목록 조회"""
    return item_store.list_all(skip=skip, limit=limit)


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int = Path(..., gt=0, description="아이템 ID"),
) -> ItemResponse:
    """아이템 단건 조회"""
    item = item_store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.patch("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int = Path(..., gt=0),
    item: ItemUpdate = Body(...),
) -> ItemResponse:
    """아이템 부분 수정"""
    updated = item_store.update(item_id, item)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@app.put("/items/{item_id}", response_model=ItemResponse)
async def replace_item(
    item_id: int = Path(..., gt=0),
    item: ItemCreate = Body(...),
) -> ItemResponse:
    """아이템 전체 수정"""
    existing = item_store.get(item_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # 전체 교체
    updated = ItemResponse(
        id=item_id,
        name=item.name,
        price=item.price,
        is_available=item.is_available,
    )
    item_store._items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(
    item_id: int = Path(..., gt=0),
) -> None:
    """아이템 삭제"""
    if not item_store.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items/count/total")
async def get_item_count() -> dict[str, int]:
    """아이템 총 개수"""
    return {"total": item_store.count()}


# ============================================================
# 메인 함수 (설명용)
# ============================================================


def main() -> None:
    """메인 함수"""
    print("\n" + "🐍 Python 백엔드 전문가 - FastAPI 기본".center(50, "="))
    print()
    print("FastAPI 서버 시작 방법:")
    print("  uvicorn 01_fastapi_basics:app --reload")
    print()
    print("API 문서:")
    print("  Swagger UI: http://localhost:8000/docs")
    print("  ReDoc: http://localhost:8000/redoc")
    print()
    print("주요 엔드포인트:")
    print("  GET    /              - 루트")
    print("  GET    /health        - 헬스 체크")
    print("  POST   /items         - 아이템 생성")
    print("  GET    /items         - 아이템 목록")
    print("  GET    /items/{id}    - 아이템 조회")
    print("  PATCH  /items/{id}    - 아이템 부분 수정")
    print("  PUT    /items/{id}    - 아이템 전체 수정")
    print("  DELETE /items/{id}    - 아이템 삭제")
    print()
    print("Python 3.12+ 특징:")
    print("  - 타입 힌트: list[X], X | None")
    print("  - Pydantic v2: model_dump(), model_copy()")
    print("  - __slots__ 사용으로 메모리 최적화")
    print()
    print("=" * 50)
    print("✅ FastAPI 기본 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()
