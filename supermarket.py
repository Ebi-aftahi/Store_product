import store
import product

my_supermarket = store.Store("My Handpicked Store")
my_supermarket.add_product(product.Product("Gala Apple", 4.99, "Fresh Fruits" ))
my_supermarket.add_product(product.Product("Hot pickels", 3.65, "Canned" ))
my_supermarket.add_product(product.Product("Theo's patties", 7.18, "Ground meat" ))
my_supermarket.add_product(product.Product("French Bread", 1.05, "Breads" ))

for item in my_supermarket.products:
	item.print_info()
