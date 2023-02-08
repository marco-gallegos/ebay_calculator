# constants
headers:list[str] = ["price", "in pesos", "ebay cost", "ebay cost in peso" , "import cost + shipment", "in pesos", "final cost", "in pesos"]
handling_cost_in_usd:float = 15 # this could consider overweight cost
iva_handling:float = 16
import_tax_percent:float = 19
ebay_buy_tax:float = 8.25


currency_against_dollar: dict[str,float] = {
    "peso": 19.1
}


def calculateprice(dollars:float, local_currency_value_against_dollar:float) -> float:
    return dollars * local_currency_value_against_dollar


# only core functionality

def calculate_ebay_costs(price:float, tc:float):
    unit_percent_price:float = round((price/100),2)

    ebay_tax:float = unit_percent_price * ebay_buy_tax
    ebay_final_price:float = price + ebay_tax
    ebay_final_price_in_local_currency:float = ebay_final_price * tc
    value:float = calculateprice(price, tc)
    value:float = round(value, 2)

    import_cost:float = unit_percent_price * import_tax_percent

    shipper_totalcost:float = import_cost + handling_cost_in_usd + ((handling_cost_in_usd/100)*iva_handling)
    
    shipper_totalcost_local_currency:float =shipper_totalcost * tc
    
    final_cost:float = shipper_totalcost + ebay_final_price

    final_cost_in_local_currency:float = final_cost * tc

    return {
        "unit_percent_price": unit_percent_price,
        "ebay_tax": ebay_tax,
        "ebay_final_price": ebay_final_price,
        "ebay_final_price_in_local_currency": ebay_final_price_in_local_currency,
        "real_value": value,
        "import_cost": import_cost,
        "shipper_totalcost": shipper_totalcost,
        "shipper_totalcost_local_currency": shipper_totalcost_local_currency,
        "final_cost": final_cost,
        "final_cost_in_local_currency": final_cost_in_local_currency,
    }


