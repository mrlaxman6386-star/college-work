# Shopping Bill: Create separate functions: input_items(), calculate_total(),
# calculate_discount(), generate_bill()
# The program should accept item prices and quantities and finally display the bill.
def input_items():
    items = []
    n = int(input("Enter number of items: "))
    for i in range(1, n + 1):
        price = int(input(f"Enter price of item {i}: "))
        quantity = int(input(f"Enter quantity of item {i}: "))
        items.append([price, quantity])
    return items
def calculate_total(items):
    total = 0
    for item in items:
        price = item[0]
        quantity = item[1]
        total = total + price * quantity
    return total
def calculate_discount(total):
    if total >= 5000:
        discount = total * 10 / 100
        return discount
    else:
        return 0
def generate_bill(items):
    total = calculate_total(items)
    discount = calculate_discount(total)
    final_amount = total - discount
    print("=============================")
    print("======= SHOPPING BILL =======")
    print("=============================")
    print("Total items:", len(items))
    print("Total bill:", total)
    print("Discount:", discount)
    print("Final amount:", final_amount)
    print("=============================")
a = input_items()
generate_bill(a)