import math
print('Scientific Calculator Supports: + , - , * , / , % , ^ ,squareroot , sin, cos,tan')
op= input('Enter operation:').lower()
basic_ops = ['-', '+', '*', '%', '^']
trigonometric_ops = ['sin', 'cos', 'tan']
if op in basic_ops:
     try:
          x = float(input('Enter the first number:'))
          y = float(input('Enter the second number:'))
          if op == '+':
           result = x + y
          elif  op == '-':
            result = x - y
          elif op == '*':
            result = x * y
          elif op == '%':
            result = x % y     
          elif op == '^':
            result = x ** y   
          print  ('the result is:', result)  
     except  Exception as e:
          print('An unexpected error occurred:', e)  
elif op == '/':
    try:
        a =  float(input('Enter the first number:'))
        b =  float(input('Enter the second number:'))  
        result = a / b
        print('the result is:',result)
    except Exception as e:
        print('An unexpected error occurred:', e)
elif op == 'squareroot':
    try:
        h = float(input('Enter a number:'))
        result = math.sqrt(h)  #or we can use result = h ** (1/2)   
        print('the result is:', result)  
    except Exception as e:
        print('An unexpected error occurred:', e)    
elif op in trigonometric_ops:
    
    ang = float(input('Enter the angle in degrees:'))        
    rad = math.radians(ang)
    if op == 'sin':
        result = math.sin(rad)
    elif op == 'cos':
        result = math.cos(rad)
    elif op == 'tan':
        result = math.tan(rad)
    print('the result is :', result)   

       
else : print('operation', op, 'is not supported ')            
