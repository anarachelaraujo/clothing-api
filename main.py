from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.adapters.controllers.user_controller import router as user_router
from app.adapters.controllers.options_controller import router as options_router


app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3001", 
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/users")
app.include_router(options_router, prefix="/options")

@app.get("/")
def read_root():
    return {"message": "Welcome to the clothing app API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
