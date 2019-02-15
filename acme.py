
import random


class Product:
#an acme product

	def __init__(self, name):
		self.name=name
		self.price=10
		self.weight=20
		self.flammability=0.5
		self.identifier=random.randrange(1000000,10000000)

	def stealability(self):

		price_weight_ratio= self.price/self.weight
		
		if price_weight_ratio<0.5:
			message='Not so stealable...'
			#print(message)
			return message

		elif price_weight_ratio>=0.5 and price_weight_ratio<1:
			message='Kinda stealable.'
			#print (message)
			return message
		
		else:
			message='Very stealable!'
			#print(message)
			return message

	def explode(self):

		price_weight_val= self.flammability*self.weight
		
		if price_weight_val<10:
			message='...fizzle.'
			#print(message)
			return message

		elif price_weight_val>=10 and price_weight_val<50:
			message='...boom!'
			#print (message)
			return message
		
		else:
			message='...BABOOM!'
			#print(message)
			return message
	




	
				






class BoxingGlove(Product):
	def __init__(self, name):
		Product.__init__(self,Product)
		self.weight=10
	
	

	def explode(self):
		message="...it's a glove."
		return message

	def punch(self):


		if self.weight<5:
			message='That tickles.'
			#print(message)
			return message

		elif self.weight>=5 and self.weight<15:
			message='Hey that hurt!'
			#print (message)
			return message
		
		else:
			message='OUCH!'
			#print(message)
			return message



	
