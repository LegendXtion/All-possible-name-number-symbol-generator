import os
import Wordlist_Class
import sys
import time

if __name__ == '__main__':
	W_Class = Wordlist_Class.WordList()

	while True:
		print("1: To generate A-Z")
		print("2: To generate a-z")
		print("3: To generate 0-9")
		print("4: To generate all punctuations")
		print("5: To generate A-Z & a-z")
		print("6: To generate A-Z & a-z & 0-9")
		print("7: To generate A-Z & 0-9")
		print("8: To generate a-z & 0-9")
		print("9: To generate user specific characters")
		print("99: To exit.\n\n")

		choice = int(input("? "))

		if choice == 1:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.Alpha_Upper(Limit=limit, repeatation=True)
			else:
				W_Class.Alpha_Upper(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

	
		elif choice == 2:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.Alpha_Lower(Limit=limit, repeatation=True)
			else:
				W_Class.Alpha_Lower(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")
	
		elif choice == 3:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.Numeric(Limit=limit, repeatation=True)
			else:
				W_Class.Numeric(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")
	
		elif choice == 4:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.Punctuation(Limit=limit, repeatation=True)
			else:
				W_Class.Punctuation(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

		elif choice == 5:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.Alphabets(Limit=limit, repeatation=True)
			else:
				W_Class.Alphabets(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

		elif choice == 6:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.AlphaNum(Limit=limit, repeatation=True)
			else:
				W_Class.AlphaNum(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

		elif choice == 7:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.UppAlphaNum(Limit=limit, repeatation=True)
			else:
				W_Class.UppAlphaNum(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

		elif choice == 8:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]: "))
			if repeat in 'Yy':
				W_Class.LowAlphaNum(Limit=limit, repeatation=True)
			else:
				W_Class.LowAlphaNum(Limit=limit,repeatation=False)

			print("Generated !!!\n\n")

		elif choice == 9:
			limit = int(input("Enter character limit\n--> "))
			repeat = str(input("Do u want characters with repeatation. [Y/N]"))
			chars = str(input("Enter characters like this Adg43@$!fda [Not seperated by space]: "))
			if repeat in 'Yy':
				W_Class.Specific(Limit=limit, repeatation=True, chars=chars)
			else:
				W_Class.Specific(Limit=limit,repeatation=False, chars = chars)

			print("Generated !!!\n\n")
			
		elif choice == 99:
			print("Exiting ...")
			time.sleep(3)
			sys.exit()
	
		else:
			print("Incorrect choice\n")

