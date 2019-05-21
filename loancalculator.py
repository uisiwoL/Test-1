print("Welcome to Lapo MFBank")
rate=float(input("What is your company's rate in percent? "))
ratefraction = rate/100
print("Your company's rate is %f" %ratefraction)

principal = float(input("Please enter the amount you want "))
print("you requested %f" %principal)

def calculate():
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)
	I=principal*ratefraction*time
	T=I+principal
	M=int(T/(time*12))
	print("Your Monthly repayment is =N=%i" %M)

if 0 < rate <= 5 and principal <= 200000:
	calculate()

elif 0 < rate <=5 and principal > 200000:
	print("Sorry you cannot get the loan")

elif 5 < rate <=10 and principal <= 500000:
	calculate()

elif 5 < rate <=10 and principal > 500000:
	print("Sorry you cannot get the loan")

elif 10 < rate <=20 and principal <= 1000000:
	calculate()

elif 10 < rate <=20 and principal > 1000000:
	print("Sorry you cannot get the loan")

elif 20 < rate <=25 and principal <= 1500000:
	calculate()

elif 20 < rate <=25 and principal > 1500000:
	print("Sorry you cannot get the loan")

else:
	calculate()


