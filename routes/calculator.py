from fastapi import APIRouter
from calculator.calculator import calculate_ebay_costs, currency_against_dollar

app = APIRouter()

@app.get("/calculator/{price}")
async def read_user(price: float, dollar_price: float = -1):
    dollar_price_to_use = dollar_price if dollar_price is not -1 and dollar_price > 5 else currency_against_dollar['peso']
    ebay_costs = calculate_ebay_costs(price, dollar_price_to_use)
    print(ebay_costs)
    return ebay_costs
