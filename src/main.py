from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.users.router import router as user_router


app = FastAPI(title="FinanceTodo")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [user_router]

for router in routers:
    app.include_router(router)


@app.get('/')
async def home():
    return {'message': "Hello world!"}
