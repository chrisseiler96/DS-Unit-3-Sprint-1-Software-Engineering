#!/usr/bin/env python


#TODO MAKE TESTS

import itertools
from itertools import chain
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
	#Making sure Acme products are the tops!"""
	def test_default_product_price(self):
	#Test default product price being 10."""
		prod = Product('Test Product')
		self.assertEqual(prod.price, 10)

	def test_default_product_weight(self):
        #Test default product weight being 20."""
		prod = Product('Test Product')
		self.assertEqual(prod.weight, 20)

	def test_explode(self):
	#test functionality of explode method
		prod= Product('Test Product')
		prod.flammability=0.1
		test_string = prod.explode()
		self.assertEqual(test_string,'...fizzle.')


class AcmeReportTests(unittest.TestCase):
	def test_default_num_products(self):
		values=generate_products()
		self.assertEqual(values[4],30)
	def test_names(self):
		legal_words = []
		legal_words.append(NOUNS)
		legal_words.append(ADJECTIVES)
		values=generate_products()
		product_list=values[5]
		products_name_strings = []
		for prodt in product_list:
			for string in prodt.name.split():
				products_name_strings.append(string)
		#products_split = list(chain.from_iterable(products_split))
		print(products_name_strings)
		print(legal_words)
		for word in products_name_strings:
			self.assertTrue( str(word) in str(legal_words))


		




if __name__ == '__main__':
    unittest.main()
