import unittest 
from examples import *


# #conditional
class TestConditional(unittest.TestCase):

	def test_first_test(self):
		a = "A"
		b = "B"
		result = get_winner(a, 5, b, 7)
		self.assertEqual(result, b)

	def test_second_test(self):
		a = "A"
		b = "B"
		result = get_winner(a, "apple", b, "banana")
		self.assertEqual(result, a)

#for loop
class TestForLoop(unittest.TestCase):

	def test_loop1(self):
		num_list = [11, 2]
		self.assertEqual(calculate_total(num_list), 13)

	def test_loop2(self):
		num_list = 5
		self.assertEqual(calculate_total(num_list), 2)




#class
class TestForClass(unittest.TestCase):

	def setUp(self):
		self.contact_Talia = Contact("Talia", "Trilling")
		self.contact_Talia.add_hobby("video games")

	def test_Class1(self):
		Talia = Contact("Talia", "Trilling")
		self.assertEqual(Talia.first_name, "Talia")
		self.assertEqual(Talia.last_name, "Trilling")
		self.assertEqual(Talia.hobbies, [])

	def test_hobbies1(self):
		self.contact_Talia.add_hobby("eating")
		self.assertEqual(self.contact_Talia.hobbies, ["video games", "eating"])

	def test_hobbies2(self):
		self.contact_Talia.add_hobby("video games")
		self.assertEqual(self.contact_Talia.hobbies, ["video games"])


if __name__ == '__main__':
	unittest.main()