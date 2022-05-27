import csv
from datetime import datetime

def main():
    current_date_and_time = datetime.now()
    try:
        product_number_index=0

        products_dict = read_dict("products.csv", product_number_index)
    
        print("Inkom Emporium")
        print()
    #print("All products")
    #print(products_dict)
    #print("Requested Items")

        with open("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)

            next(reader)
            items_number = 0
            subtotal = 0
            price = 0

            for line in reader:
                product_number = line[0]
                quantity = int(line[1])

            
                #if product_number in products_dict:
                value = products_dict[product_number]
                product_name = value[1]
                product_price = float(value[2])
                print(f'{product_name}: {quantity} @ {product_price} ')
                price = product_price * quantity
                items_number += quantity
                subtotal += price

            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax

            print()    
            print(f'Number of Items: {items_number}') 
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {sales_tax:.2f}')

            if datetime.today().weekday() == 0:
                print()
                print("Mondays are discount days! You get 10% of your purchase")
                total_monday = float(total * 0.9)
                discount = float(total * 0.1)
                print(f'Discount: {discount:.2f}')
                print(f'Total: {total_monday:.2f}')

            else:
                print(f'Total: {total:.2f}')

        print()
        print("Thank you for shopping at the Inkom Emporium.")
    
        print(f"{current_date_and_time:%a %b %d %X %Y}")   

    except FileNotFoundError as not_found_err:
        print()
        print("Error: missing file ")
        print(f"[Errno 2] No such file or directory: '{not_found_err.filename}'")
    
    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {request_file}.")
    
    except (csv.Error, KeyError) as error:
        print()
        print(f"Error: unknown product ID in the {request_file.name} file")
        print(error)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary


if __name__ == "__main__":
    main()