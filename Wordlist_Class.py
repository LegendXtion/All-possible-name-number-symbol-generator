class WordList():
	def __init__(self):
		import string
		import itertools

		self.itertools = itertools
		self.list_num = string.digits
		self.list_upp = string.ascii_uppercase
		self.list_low = string.ascii_lowercase
		self.list_upp_low = string.ascii_letters
		self.list_pun = string.punctuation

	def writer(self, compination, fileName):
		f = open(fileName, 'w')
		for ch in compination:
			f.write(ch+'\n')
		f.close()


	def Numeric(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName='Numeric_0-9_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName='Numeric_0-9_{Limit}.txt')


	def Alpha_Lower(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_low, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'a-z_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_low, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'a-z_{Limit}.txt')

		
	def Alpha_Upper(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_upp, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_upp, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z_{Limit}.txt')
		

	def Alphabets(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_upp_low, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_upp_low, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z_{Limit}.txt')
		

	def AlphaNum(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_upp_low+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z,0-9_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_upp_low+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z,0-9_{Limit}.txt')
		

	def LowAlphaNum(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_low+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'a-z,0-9_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_low+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'a-z,0-9_{Limit}.txt')
		

	def UppAlphaNum(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_upp+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,0-9_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_upp+self.list_num, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,0-9_{Limit}.txt')
		

	def AlphaNumPunc(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_upp_low+self.list_num+self.list_pun, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z,0-9,punctuations_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_upp_low+self.list_num+self.list_pun, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'A-Z,a-z,0-9,punctuations_{Limit}.txt')
		

	def Punctuation(self, Limit=0, repeatation=True):
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(self.list_pun, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'Punctuations_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(self.list_pun, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'Punctuations_{Limit}.txt')
		

	def Specific(self, Limit=0, repeatation=True, chars=''):
		list_sp = list(set(chars))
		if repeatation == True:
			compinations = self.itertools.combinations_with_replacement(list_sp, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'{chars}_{Limit}_with_r.txt')
		else:
			compinations = self.itertools.combinations(list_sp, Limit)
			result = map(''.join, compinations)
			self.writer(compination=result, fileName=f'{chars}_{Limit}.txt')
		

		
