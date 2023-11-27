import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.router import router as user_router
from src.balances.router import router as balance_router
from src.category.service import category_service
from src.category.router import router as category_router
from src.category.router import router_sub as subcategory_router
from src.transaction.router import router as transaction_router


def create_app(title: str, app_routers: list) -> FastAPI:
    app_created = FastAPI(title=title)

    origins = ["*"]

    app_created.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in app_routers:
        app_created.include_router(router)

    return app_created


routers = [user_router, balance_router, category_router, subcategory_router, transaction_router]

app = create_app("FinanceTodo", routers)


@app.on_event("startup")
async def startup():
    await category_service.create_default_categories()
