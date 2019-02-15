from acme import Product
import random



def generate_products(amount=30):
		product_list=[]
		adjectives=['Awesome','Shiny','Impressive',
				'Portable','Improved']
		nouns=['Anvil','Catapult','Disguise',
				'Mousetrap','???']
		
		prices=0
		weights=0
		flam=0

		for i in range(0,amount):
			rand_adj=adjectives[random.randint(0,4)]
			rand_noun=nouns[random.randint(0,4)]


			generated_name=rand_adj + ' ' + rand_noun
			print(generated_name)

			product_list.append(Product(generated_name))
		
		
		for acme_prod in product_list:
			acme_prod.weight = random.randint(5,100)
			weights+=acme_prod.weight
			acme_prod.price = random.randint(5,100)
			prices+=acme_prod.price
			acme_prod.flammability=random.randint(0,25)/10
			flam+=acme_prod.flammability

		unique_products = len(set(product_list))
		average_product_weight = weights/len(product_list)
		average_product_price = prices/len(product_list)
		average_product_flam = flam/len(product_list)

		returnvals=[]
		returnvals.append(unique_products)
		returnvals.append(average_product_weight)
		returnvals.append(average_product_price)
		returnvals.append(average_product_flam)		
		return returnvals

def inventory_report(values):
		print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
		
		#print(product_list)
		print('Unique product names: ',values[0])
		print('Average price: ',values[1])
		print('Average weight: ',values[2])
		print('Average flammability: ',values[3])		
		
if __name__=='__main__':
	inventory_report(generate_products())					
