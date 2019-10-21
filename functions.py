
# a script to demonstrate how to use functions

def addTwoNumbers(a,b):
    return a+b
def main():
    print('This is the main function.')


def funScope():
    x = 1
    y = 2
    print('x=' + str(x))
    print('y=' + str(y))

def funcOperator():
    x = 2
    print(x)
    print(x==1)
    
if __name__ == "__main__":
    # execute only if run as a script

    funcOperator()
    


    
##    funScope()
##    
##    x = 3
##    print('x=' + str(x))
##    print('y=' + str(y))
    
    

    
