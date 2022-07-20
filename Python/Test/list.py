class Contect :
	def __init__(self, name, phone, email, address) :
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address

	def print_info(self):
		print("name : ", self.name)
		print("phone : ", self. phone)
		print("email : ", self.email)
		print("address : ", self.address)

	def del_info(self):
		self.name = ""
		self.phone = ""
		self.email = ""
		self.address = ""
		print("삭제하였습니다")

def input_menu():
	print("1. 입력 ")
	print("2. 삭제 ")
	print("3. 조회 ")
	print("4. 종료 ")
	number = input("번호를 입력하세요 : ")
	return int(number)

def main() :
	while True:
		print('')
		menu = input_menu()
		if menu == 1 :
			name = input("name : ")
			phone = input("phone : ")
			email = input("email : ")
			address = input("address : ")
			a=Contect(name, phone, email, address)
		elif menu == 2 :
			a.del_info()
		elif menu == 3 :
			a.print_info()
		elif menu == 4 :
			break

if __name__ == "__main__":
	main()
