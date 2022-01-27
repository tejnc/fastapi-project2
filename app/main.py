from fastapi import FastAPI

from app.routes import routing


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    
app.include_router(routing.router)