def calculator (num1, sign, num2):

    # checks if the numbers are intgers 
    if isinstance(num1, int) and isinstance (num2, int) :

        # checks if they are valid operators or not
        if(sign == '+'):
            return num1 + num2 
        elif(sign == '-'):
            return num1 - num2
        elif (sign == '*'):
            return num1 * num2
        elif (sign == '/'):
            return num1 / num2 
        elif (sign == '%'):
            return num1 % num2 
        else :
            print ("Invalid operator")
    else :
        print ("Invalid input")

result = calculator(5, '-', 3)
print(result)


