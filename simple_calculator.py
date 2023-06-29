from stack import Stack

class SimpleCalculator:
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.hist = []
		

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		num1 = ""
		op = 0
		nop=0
		num2 = ""
		
		for j in input_expression:
			if j=="+" or j=="-" or j=="*" or j=="/":
					op=j
					nop+=1
			elif nop==0:
				num1+=j
			else:
				num2+=j
		num1=num1.strip()
		num2=num2.strip()
		try:
			num1=float(num1)
		except:
			pass
		try:
			num2 = float(num2)
		except:
			pass
		if type(num1)!=type("a") and nop==1 and type(num2)!=type("a"):
			if op=="+":
				ans= float(num1) + float(num2)
			elif op=="-":
				ans= float(num1)-float(num2)
			elif op=="*":
				ans= float(num1)*float(num2)
			else:
				if num2!=0:
					ans= float(num1)/float(num2)
				else:
					ans= "Error"
		else:
			ans= "Error"

		self.hist.append((input_expression,ans))

		return ans

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.hist[::-1]
		
