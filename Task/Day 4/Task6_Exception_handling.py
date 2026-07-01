def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"Error:Missing key{e}")
    else:
        print("Order Details")
        print("Item:",item)
        print("Price:",price)
    finally:
        print("Processing Complete")

print("Order 1:")
process_order({"item": "Laptop","price":50000})
print("\nOrder 2:")
process_order({"item":"Laptop"})