import sys

# Make sure the number is valid
def isNumber(Number:str):
    if(Number >= "0" and Number <= "9"):
        return True
    return False

# Check if the character is an operator or a parenthesis.
def isOperator(Operator:str):
    if(Operator == "("):
        return True
    if(Operator == ")"):
        return True
    if(Operator == "^"):
        return True
    if(Operator == "+"):
        return True
    if(Operator == "-"):
        return True
    if(Operator == "*"):
        return True
    if(Operator == "/"):
        return True
    
def Calc(Operator_number:int,Math_input:list):
    # Perform the calculation based on the operator's position in the list.
    # This function finds the operator at the given index and calculates the 
    # result of the operation.

    # Set operator
    Operator = Math_input[Operator_number]

    # Set operands from the list based on the operator's position.
    First_num = float(Math_input[Operator_number-1])
    Second_num = float(Math_input[Operator_number+1])

    ## FOR TESTING PURPOSES ##
    #print(First_num,":",Operator,":",Second_num)

    # Calculate the operation based on the operator type, in the order of operations
    if(Operator == "^"):
        return pow(First_num,Second_num)
    if(Operator == "*" or Operator == "/"):
        if (Operator == "*"):
            return First_num * Second_num
        if (Operator == "/"):
            return First_num / Second_num
    if(Operator == "+" or Operator == "-"):
        if (Operator == "+"):
            return First_num + Second_num
        if (Operator == "-"):
            return First_num - Second_num

# Checks if the new operator (New_Operator) has higher precedence 
# than the current top operator (Old_Operator)
def Operator_Priority_Check(New_Operator:str,Old_Operator:str):

    # Exponentiation has the highest precedence, so no new operator
    # should be processed before an exponent. 
    # Therefore, it returns False, meaning we will not process the new operator
    if (Old_Operator == "^"):
        return False

    # Exponentiation is right associative (evaluated from right to left), so a 
    # new exponent operator should be processed before lower-precedence operations.
    # It returns True, indicating that the new exponent should be added to the 
    # stack and given priority.
    if (New_Operator == "^"):
        return True

    # This line checks if the old operator is multiplication (*) or division (/). 
    # If one of these operators is already on the stack, it should be processed 
    # before the new operator, unless the new operator is an exponent (^).
    # Hence, it returns False, meaning we deal with multiplication or division in 
    # the stack before any new addition or subtraction.
    if (Old_Operator == "*" or Old_Operator == "/"):
        return False
    if (New_Operator == "*" or New_Operator == "/"):
        return True
    if (Old_Operator == "+" or Old_Operator == "-"):
        return False
    if (New_Operator == "+" or New_Operator == "-"):
        return True
    return 

# Finds the innermost parentheses and extracts the expression inside.
def parenthsis_handler(input_list:list):

    #parenthesis start/end index
    parenthsis_start = 0
    parenthsis_end = 0
    index = 0
    for item in input_list:
        # Set start index
        if(item == "(" and parenthsis_end == 0):
            parenthsis_start = index 
        
        # Set end index
        if(item == ")" and parenthsis_end == 0):
            parenthsis_end = index
        index = index + 1

    # No complete set of parentheses found.
    if (parenthsis_start == parenthsis_end):
        return False

    # create a list called new_list that will store:
    # The starting index of the first opening parenthesis ( found.
    # The ending index of the first closing parenthesis ) that 
    # corresponds to that opening parenthesis.
    new_list = []
    new_list.append(parenthsis_start)
    new_list.append(parenthsis_end)
    for item in range(parenthsis_start,parenthsis_end):
        if (item == parenthsis_start):
            input_list.pop(parenthsis_start)
        if (item == parenthsis_end-1):
            input_list.pop(parenthsis_start)
        else:
            new_list.append(input_list[item])
    return new_list


# Splits the input string into numbers and operators, correctly handling multiple-digit numbers and decimal points.
def number_and_operator_splitter(string:str):
    Math_function = []
    Number = ""

    # Add a flag to signal end.
    string = string + "?" 
    previous_char = ""
    for char in string:
        if(char == "?"):
            # End of the string; append any remaining number.
            if (Number != ""):
                Math_function.append(Number)
        
        # Build multi-digit numbers.
        if(isNumber(char)):
            Number = Number + char
        if(isOperator(char)):

            # Handle negative numbers or implied multiplication by 0.
            if (Number == "" and char != ")" and char != "(" and previous_char != ")"):
                Math_function.append(0)
            else:
                if (Number != ""):

                    # Add the completed number to the list.
                    Math_function.append(Number)

            # Handle implicit multiplication, ex. 2(3) -> 2 * 3.
            if (isNumber(previous_char) and char == "("):
                Math_function.append("*")
            Math_function.append(char)
            # Reset the number.
            Number = ""
        previous_char = char
    return Math_function


# Recursively evaluates the mathematical expression using operator precedence.
def func_parser(math_function:list):
    if (len(math_function) == 1):

        # Base case: return the single remaining value.
        return math_function[0]
    
    # Find the operator with the highest precedence.
    Current_index = 0
    Highest_priority_operator_index = 0
    Symbol = ""
    for math_symbol in math_function:
        if(isOperator(math_symbol)):
            if (Operator_Priority_Check(math_symbol,Symbol)):
                Highest_priority_operator_index = Current_index
                Symbol = math_symbol
        Current_index = Current_index + 1
    # Calculate the value of the highest precedence operation.
    Answer = Calc(Highest_priority_operator_index,math_function)
    if (len(math_function) == 2):
        for item in range(0,2):
            math_function.pop(0)
        math_function.insert(0,Answer)
    else:
        for item in range(0,3):
            math_function.pop(Highest_priority_operator_index-1)
        math_function.insert(Highest_priority_operator_index-1,Answer)
    return func_parser(math_function)

# Handles parentheses in the expression and recursively evaluates the expression.
def basic_logic(Inital_list):
    parenthsis_copy = []
    for item in Inital_list:
        parenthsis_copy.append(item)
    any_parenthsis = parenthsis_handler(parenthsis_copy)
    
    # No parentheses left, parse normally.
    if (any_parenthsis == False):
        Answer = func_parser(Inital_list)
        return Answer
    
    # Evaluate the expression within parentheses first.
    else:    
        index_start = any_parenthsis.pop(0)
        index_end = any_parenthsis.pop(0)
        Answer = func_parser(any_parenthsis)
        # Replace the evaluated parentheses with their result.
        for item in range(index_start,index_end+1):
            Inital_list.pop(index_start)
        Inital_list.insert(index_start,Answer)

        # Recur to handle any remaining parentheses.
        return basic_logic(Inital_list)

def main(expression):
    expression = expression.replace(" ", "")
    Inital_list = number_and_operator_splitter(expression)
    result = int(basic_logic(Inital_list))
    print(result)

if __name__ == "__main__":
    # Get the input expression from command line arguments
    expression = sys.argv[1]
    main(expression)