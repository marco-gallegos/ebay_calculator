import click
from tabulate import tabulate


# constants
headers:list[str] = ["price", "in pesos", "ebay cost", "ebay cost in peso" , "import cost + shipment", "in pesos", "final cost", "in pesos"]
handling_cost_in_usd:float = 15 # this could consider overweight cost
iva_handling:float = 16
import_tax_percent:float = 19
ebay_buy_tax:float = 8.25


currency_against_dollar: dict[str,float] = {
    "peso": 19.7
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



@click.command()
@click.option("-p", "--price", type=float, required=True, prompt="price in dollars")
@click.option("-v", "--vertical", is_flag=True, type=bool)
def main(price:float, vertical:bool) -> None:
    # unit_percent_price:float = round((price/100),2)

    # ebay_tax:float = unit_percent_price * ebay_buy_tax
    # ebay_final_price:float = price + ebay_tax
    # ebay_final_price_in_local_currency:float = ebay_final_price * currency_against_dollar["peso"]

    # value:float = calculateprice(price, currency_against_dollar["peso"])
    # value:float = round(value, 2)
    
    # values:list = []
    
    # import_cost:float = unit_percent_price * import_tax_percent

    # shipper_totalcost:float = import_cost + handling_cost_in_usd + ((handling_cost_in_usd/100)*iva_handling)
    
    # shipper_totalcost_local_currency:float =shipper_totalcost * currency_against_dollar["peso"]
    
    # final_cost:float = shipper_totalcost + ebay_final_price

    # final_cost_in_local_currency:float = final_cost * currency_against_dollar["peso"]
    
    ebay_stimates = calculate_ebay_costs(price=price, tc=currency_against_dollar["peso"])
    
    values:list = []

    printable_values:list[float] = [ 
        price, ebay_stimates['real_value'], ebay_stimates['ebay_final_price'],ebay_stimates['ebay_final_price_in_local_currency'],
        ebay_stimates['shipper_totalcost'], ebay_stimates['shipper_totalcost_local_currency'],
        ebay_stimates['final_cost'], ebay_stimates['final_cost_in_local_currency']
    ]
    


    if(vertical is True): 
        for index,header in enumerate(headers):
            new_element:list = [header, printable_values[index]]
            values.append(new_element)
        print(tabulate(values))

    else:
        values.append(printable_values)
        print(tabulate(values, headers=headers))



if __name__ == "__main__":
    main()
