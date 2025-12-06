"""
The main app of source file
"""

from fastapi import FastAPI
# from contextlib import asynccontextmanager
# from app.core.database import get_session, Base
from app.routers.routers import router


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     try:
#         async with engine.begin() as conn:
#             print("program runnn")
#             await conn.run_sync(Base.metadata.create_all())
#             print("DB CONNECTED")
#     except Exception as e:
#         print("DB connection error")
#         raise e
#     # os.makedirs(config("UPLOAD_DIR"), exist_ok=True)
#     print("\n🚀 FastAPI Started | DB Ready | Upload Dir OK.\n")

#     yield

app = FastAPI(title="My FastAPI Project")
app.include_router(router)

# @app.get("/")
# def root():
#     """
#     the root path
#     """
#     return {"message": "FastAPI is running!"}
