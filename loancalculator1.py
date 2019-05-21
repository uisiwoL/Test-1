print("Welcome to Lapo MFBank")

rate=float(input("What is your company's rate in percent? "))
rate_fraction=rate/100
print("Your company's rate is %.2fpercent" %rate)


principal=float(input("Please enter the amount you want "))
print("you requested N%.2f" %principal)

if 0 < rate <= 5 and principal <= 200000:
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)

	I=principal*rate_fraction*time

	T=I+principal

	M=int(T/(time*12))

	print("Your Monthly repayment is =N=%i" %M)


elif 0 < rate <=5 and principal > 200000:
	print("Sorry you cannot get the loan")

elif 5 < rate <=10 and principal <= 500000:
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)

	I=principal*rate_fraction*time

	T=I+principal

	M=int(T/(time*12))

	print("Your Monthly repayment is =N=%i" %M)

elif 5 < rate <=10 and principal > 500000:
	print("Sorry you cannot get the loan")

elif 10 < rate <=20 and principal <= 1000000:
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)

	I=principal*rate_fraction*time

	T=I+principal

	M=int(T/(time*12))

	print("Your Monthly repayment is =N=%i" %M)

elif 10 < rate <=20 and principal > 1000000:
	print("Sorry you cannot get the loan")

elif 20 < rate <=25 and principal <= 1500000:
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)

	I=principal*rate_fraction*time

	T=I+principal

	M=int(T/(time*12))

	print("Your Monthly repayment is =N=%i" %M)

elif 20 < rate <=25 and principal > 1500000:
	print("Sorry you cannot get the loan")

else:
	time=int(input("Enter the time duration for the loan  "))
	print("The duration for the loan is %i year(s)" %time)

	I=principal*rate_fraction*time

	T=I+principal

	M=int(T/(time*12))

	print("Your Monthly repayment is =N=%i" %M)


