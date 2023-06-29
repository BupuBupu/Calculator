from simple_calculator import SimpleCalculator
from stack import Stack
class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		super().__init__()	
	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		list_tokens = self.tokenize(input_expression)
		if self.check_brackets(list_tokens)==False:
			ans = "Error"	
		else:
			ans = self.evaluate_list_tokens(list_tokens)
		self.hist.append((input_expression,ans))
		return ans
	def tokenize(self, input_expression):
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		tokens=[]
		token=""
		for i in input_expression:
			if i.isdigit() or i==".":
				token+=i
			elif i in "}+-/*(){ ":
				if token!="":
					tokens.append(int(token))
					token=""
				if i !=" ":
					tokens.append(i)
			else:
				if token!="":
					tokens.append(int(token))
					token=""
				tokens.append(i)
		token = token.strip()
		if token!="":
			tokens.append(int(token))
		return tokens	
	def check_brackets(self, list_tokens):
			# Check if brackets are valid
			# All open brackets must be closed by the same type of brackets
			# () brackets can only contain () brackets, {} brackets can contain both {} and () brackets
		stk = Stack()
		for token in list_tokens:
			k1 = str(token)
			if k1=="{":
				if len(stk)==0:
					stk.push(k1)
				elif stk.peek()=="(":
					return False
				else:
					stk.push("{")
			elif k1 == "(":
				stk.push(k1)
			elif k1==")":
				if len(stk)!=0:
					if stk.peek()=="(":
						stk.pop()
					else:
						return False
				else:
					return False
			elif k1=="}":
				if len(stk)!=0:
					if stk.peek()=="{":
						stk.pop()
					else:
						return False
				else:
					return False
		if len(stk)==0:
			return True
		else:
			return False	
	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		for i in list_tokens:
			if type(i)==type("A"):
				if i not in "+-*/}{)(":
					return "Error"

		nm_check=0
		spc_check=0
		for i in list_tokens:
			if str(i) in "}{)(+-/*":
				spc_check=0
			else:
				if(spc_check==0):
					spc_check=1
				else:
					nm_check=1
		if(nm_check!=0):
			return "Error"
		else:
			for i in range(len(list_tokens)):
				if(list_tokens[i]=='{'):
					list_tokens[i]='('
				elif(list_tokens[i]=='}'):
					list_tokens[i]=')'

			list_tokens= ['(']+list_tokens + [')']
			
			dct={}
			brc=Stack()
			for i in range(len(list_tokens)):
				if(list_tokens[i]=='('):
					brc.push(i)
				elif(list_tokens[i]==')'):
					dct[i]=brc.pop()

			while(len((list_tokens))!=1):
				for i in range(len(list_tokens)):
					if(list_tokens[i]==')'):
						stind=dct[i]
						enind=i
						anslis=self.clclis(list_tokens[stind+1:enind])
						if(anslis=="Error"):
							return "Error"
						else:
							list_tokens=list_tokens[:stind]+anslis+list_tokens[enind+1:]
							dct.clear()
							brc=Stack()
							for i in range(len(list_tokens)):
								if(list_tokens[i]=='('):
									brc.push(i)
								elif(list_tokens[i]==')'):
									dct[i]=brc.pop()
							break
			return float(list_tokens[0])
	def clclis(self,lis):

		if(len(lis)==0):
			return "Error"
		else:
			if(str(lis[0]) in "+-*/" ) or str(lis[-1]) in '+-*/':
				return "Error"
			else:
				nmcheck=0
				for i in range(len(lis)):
					if((str(lis[i]) in "+-/*") and nmcheck==0) or ((str(lis[i]) not in "+-/*") and nmcheck!=0):
						return "Error"
					elif((str(lis[i])in "+-/*") and nmcheck!=0):
						nmcheck=0
					elif((str(lis[i]) not in "+-/*") and nmcheck==0):
						nmcheck=1
					else:
						k1 = lis[i]
						if type(k1)!= type(1):
							if k1 not in "+-*/{(})":
								return "Error"				
				mul_count=0
				div_count=0
				for i in range(len(lis)):
					if(lis[i]=='*'):
						mul_count+=1
					elif(lis[i]=='/'):
						div_count+=1
				for ____ in range(div_count):
					for i in range(len(lis)):
						if(lis[i]=='/'):
							if(float(lis[i+1])==0):
								return "Error"
							else:
								lis=lis[:i-1]+[float(lis[i-1])/float(lis[i+1])]+lis[i+2:]
								break
				for __ in range(mul_count):
					for i in range(len(lis)):
						if(lis[i]=='*'):
							lis=lis[:i-1]+[float(lis[i-1])*float(lis[i+1])]+lis[i+2:]
							break
				while(len(lis)!=1):
					for i in range(len(lis)):
						if(lis[i] == '+'):
							lis=lis[:i-1]+[float(lis[i-1])+float(lis[i+1])]+lis[i+2:]
							break
						elif(lis[i]=='-'):
							lis=lis[:i-1]+[float(lis[i-1])-float(lis[i+1])]+lis[i+2:]
							break
				return lis
	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.hist[::-1]	
# advcal = AdvancedCalculator()
# exp = "34+{98-76}"
# print(advcal.evaluate_expression(exp))