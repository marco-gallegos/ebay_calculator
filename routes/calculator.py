from fastapi import APIRouter

app = APIRouter()

@app.get("/calculator/{user_id}")
async def read_user(user_id: str):
    print(user_id)
    return {"user_id": user_id}
