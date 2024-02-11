product_list = input("Введите названия продуктов через запятую: ").split(", ")



for i, product in enumerate(product_list):

 print(f"{i+1}) {product}")
