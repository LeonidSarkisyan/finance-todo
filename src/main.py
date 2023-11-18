from fastapi import FastAPI

from src.users.router import router as user_router


app = FastAPI(title="FinanceTodo")

routers = [user_router]

for router in routers:
    app.include_router(router)


@app.get('/')
async def home():
    return {'message': "Hello world!"}
