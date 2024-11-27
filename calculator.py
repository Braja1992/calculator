# calculator.py
class Calculator:
    def addition(self, a, b):
    	return a + b
    
    def subtraction(self, a, b):
        pass
        
    def division(self, a, b):
    	if b == 0:
        	raise ValueError("Cannot divide by zero")
    	return a / b
        
    def multiplication(self, a, b):
   	 return a * b