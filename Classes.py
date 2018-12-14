class Customer:
	name = ""
	address = ""
	telephone = ""
	def description(self):
		desc_str = "%s lives at %s and their telephone number is %s" % (self.name, self.address, self.telephone)
		return desc_str

person1 = Customer()
person1.name = "Bill"
person1.address = "123 Sunnybrook Drive"
person1.telephone = "4161114444"

person2 = Customer()
person2.name = "Sara"
person2.address = "321 Sunnybroook Drive"
person2.telephone = "4164441111"

print(person1.description())
print(person2.description())