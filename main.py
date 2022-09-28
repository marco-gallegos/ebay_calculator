import click
from tabulate import tabulate

headers:list[str] = ["price", "in pesos", "ebay cost", "ebay cost in peso" , "import cost + shipment", "in pesos", "final cost", "in pesos"]
handling_cost_in_usd:float = 15 # this could consider overweight cost
iva_handling:float = 16
import_tax_percent:float = 19
ebay_buy_tax:float = 8.25

currency_against_dollar: dict[str,float] = {
    "peso": 20.2
}


def calculateprice(dollars:float, local_currency_value_against_dollar:float) -> float:
    return dollars * local_currency_value_against_dollar


@click.command()
@click.option("-p", "--price", type=float, required=True, prompt="price in dollars")
def main(price:float) -> None:
    unit_percent_price:float = round((price/100),2)

    ebay_tax:float = unit_percent_price * ebay_buy_tax
    ebay_final_price:float = price + ebay_tax
    ebay_final_price_in_local_currency:float = ebay_final_price * currency_against_dollar["peso"]

    value:float = calculateprice(price, currency_against_dollar["peso"])
    value:float = round(value, 2)
    
    values:list = []
    
    import_cost:float = unit_percent_price * import_tax_percent

    shipper_totalcost:float = import_cost + handling_cost_in_usd + ((handling_cost_in_usd/100)*iva_handling)
    
    shipper_totalcost_local_currency:float =shipper_totalcost * currency_against_dollar["peso"]
    
    final_cost:float = shipper_totalcost + ebay_final_price

    final_cost_in_local_currency:float = final_cost * currency_against_dollar["peso"]

    values.append(
        [ 
            price, value, ebay_final_price, ebay_final_price_in_local_currency,
            shipper_totalcost, shipper_totalcost_local_currency, final_cost, final_cost_in_local_currency
        ]
    )

    print(tabulate(values, headers=headers))


if __name__ == "__main__":
    main()
