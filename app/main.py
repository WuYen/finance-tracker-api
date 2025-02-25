from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.features.category.category_router import router as category_router

app = FastAPI()

app.include_router(category_router)

# CORS 設定 (允許前端存取)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Finance Tracker API is running 🚀"}
