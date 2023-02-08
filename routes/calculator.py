from fastapi import APIRouter

app = APIRouter()

@app.get("/calculator/{price}")
async def read_user(price: float, dollar_price: float = 1):
    return { "price": price, "dollar_price": dollar_price }
