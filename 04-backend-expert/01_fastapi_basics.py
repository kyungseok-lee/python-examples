"""
01. FastAPI 기본 (FastAPI Basics)

FastAPI를 사용한 REST API 개발 기초를 학습합니다.

실행 방법:
    uvicorn 01_fastapi_basics:app --reload

API 문서:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, Query, Path, Body, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Python Backend Expert API",
    description="FastAPI 기본 예제",
    version="1.0.0"
)


# Pydantic 모델
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    is_available: bool = True


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float


# 메모리 저장소 (실제로는 데이터베이스 사용)
items_db: List[ItemResponse] = []
next_id = 1


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "Python Backend Expert API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {"status": "healthy"}


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    """아이템 생성"""
    global next_id
    
    item_response = ItemResponse(
        id=next_id,
        name=item.name,
        price=item.price
    )
    items_db.append(item_response)
    next_id += 1
    
    return item_response


@app.get("/items", response_model=List[ItemResponse])
async def list_items(
    skip: int = Query(0, ge=0, description="건너뛸 항목 수"),
    limit: int = Query(10, ge=1, le=100, description="조회할 항목 수")
):
    """아이템 목록 조회"""
    return items_db[skip:skip + limit]


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int = Path(..., gt=0, description="아이템 ID")
):
    """아이템 단건 조회"""
    for item in items_db:
        if item.id == item_id:
            return item
    
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int = Path(..., gt=0),
    item: Item = Body(...)
):
    """아이템 수정"""
    for idx, db_item in enumerate(items_db):
        if db_item.id == item_id:
            updated_item = ItemResponse(
                id=item_id,
                name=item.name,
                price=item.price
            )
            items_db[idx] = updated_item
            return updated_item
    
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(
    item_id: int = Path(..., gt=0)
):
    """아이템 삭제"""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return
    
    raise HTTPException(status_code=404, detail="Item not found")


def main():
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
    print("  GET    /")
    print("  GET    /health")
    print("  POST   /items")
    print("  GET    /items")
    print("  GET    /items/{item_id}")
    print("  PUT    /items/{item_id}")
    print("  DELETE /items/{item_id}")
    print()
    print("=" * 50)
    print("✅ FastAPI 기본 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

