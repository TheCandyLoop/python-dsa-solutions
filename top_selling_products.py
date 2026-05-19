from collections import defaultdict
import heapq

def top_selling_products(sales, k):

    product_count = defaultdict(int)

    for product, quantity in sales:
        product_count[product] += quantity

    top_products = heapq.nlargest(
        k,
        product_count.items(),
        key=lambda x: x[1]
    )

    return top_products


sales_data = [
    ("iPhone", 5),
    ("Laptop", 3),
    ("iPhone", 7),
    ("Headphones", 4),
    ("Laptop", 2)
]

print(top_selling_products(sales_data, 2))
