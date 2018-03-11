dbb = {"matt":{"pass":1234, "balance":2000}, "diana":{"pass":4321, "balance":2000}}

def type_input(type, question): #Catches improper entries by str/int.
	if type == "str":
		while True:
			try:
				response = str(input(question))
				return response
			except:
				response = type_input(type, question)
				return response
	else:
		while True:
			try:
				response = int(input(question))
				return response
			except:
				response = type_input(type, question)
				return response

def d_verify(db, account, upass):
	error = ''
	for a,p in db.items():
		if a == account:
		#code in sign in failure error for name
			for attrName, attr in p.items():
				if attrName == "pass" and attr == upass:
					return [True, db[account], account]
					#code in sign in failure error for password
		
	return "Signing In Failed"

def transaction(type, receipt, account) :
	if type == "deposit":
		amount = type_input("int", "Enter the amount you would like to deposit: \r\n")
	else:
		amount = type_input("int", "Enter the amount you would like to withdraw: \r\n")
	if amount > 0 and amount < 1000000:
		if type == "deposit":
			account["balance"] += amount
		else:
			if account["balance"] < amount:
				print(("\r\n"*2)+"You have insufficient funds. Your account balance is"+str(account["balance"])+("\r\n"*2))
				return account
			account["balance"] -= amount
		if receipt == True:
			print("\r\nYour account balance is $"+str(account["balance"])+("\r\n"*2))
		else:
			print("\r\n")
	else:
		transaction(type, receipt, account)
	return account

def check_balance(account):
	for attrName, attr in account.items():
		if attrName == "balance":
			print(("\r\n"*3)+"Your account balance is $"+str(attr)+("\r\n"*3))
	return account
	
def sign_out(account):
	sign_out_msg = "Signing Out".center(46, "-")
	print(("\r\n"*3)+sign_out_msg+("\r\n"*3))
	init()
	#raise SystemExit
			
def sign_in(db):
	user = ''
	upass = ''
	while (user == ''):
		user = type_input("str", "Enter Your User name\r\n").lower()
	while (upass == ''):
		upass = type_input("int", "Please enter your pin.\r\n")
	#auth = verify(db, user, upass)
	auth = d_verify(db, user, upass)
	if auth[0] == True:
		sign_in_msg = "Signing In".center(46, "-")
		#include time stamp for session length later.
		print(("\r\n"*3)+sign_in_msg+("\r\n"*3))
		return auth
	else:
		print(auth+"\r\n")
		sign_in(db)
		
def list_options():
	print("Please select an option below:")
	print(''' 
	[1] - Make a deposit with receipt
	[2] - Make a deposit without receipt
	[3] - Withdraw Cash with Receipt
	[4] - Withdraw Cash without Receipt
	[5] - Check Account Balance
	[6] - Sign Out
	''')
	choice = type_input("int", "")
	return choice

def bank_actions(account):
	choice = list_options()
	if int(choice) == 1:
		account[1] = transaction("deposit", True, account[1])
	if int(choice) == 2:
		account[1] = transaction("deposit", False, account[1])
	elif int(choice) == 3:
		transaction("withdraw", True, account[1])
	elif int(choice) == 4:
		transaction("withdraw", True, account[1])
	elif int(choice) == 5:
		check_balance(account[1])
	elif int(choice) == 6:
		sign_out(account)
	else: 
		bank_actions(account)
	bank_actions(account)
		
def init():
	account = sign_in(dbb)
	bank_actions(account)
		
init()