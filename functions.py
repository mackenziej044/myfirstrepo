#functions 

#define a function
def greet():
    #code block for my function
    ##
    print('hello user how are you?')
#call the greet() function 
greet()

#function with parameters
def add(a, b):
    return a + b 

result = add(2,3)
print(result)

#function with default parameter
def greet(name='Guest'):
    print(f'hello, {name}')

greet()
greet('Mackenzie')

#function with multiple returns
def sum_product(a,b):
    return a+b, a*b

sum_result, product_result = sum_product(5,6)
print(sum_result,product_result)

