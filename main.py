import click
from tabulate import tabulate
from calculator.calculator import calculate_ebay_costs, currency_against_dollar, headers


@click.command()
@click.option("-p", "--price", type=float, required=True, prompt="price in dollars")
@click.option("-v", "--vertical", is_flag=True, type=bool)
def main(price:float, vertical:bool) -> None:
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
