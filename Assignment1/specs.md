# Specifications 

## Parentheses Validation (`parentheses.py`)

Checks if the parentheses in a given string are balanced. It processes the string character by character, using a stack data structure to ensure each opening parenthesis has a corresponding and correctly ordered closing parenthesis.

### Methods

- **`is_valid(s: str) -> str`**
  - **Purpose:** Checks if the parentheses in the string `s` are valid 
  - **Parameters:** 
    - `s` (str): The input string containing parentheses.
  - **Returns:** 
    - "yes" if the parentheses are valid.
    - "no" if the parentheses are not valid.
  - **Logic:**
    - A stack is used to keep track of opening parentheses.
    - A dictionary `close_to_open` maps closing parentheses to their corresponding opening parentheses.
    - For each character in the string:
      - If it's an opening parenthesis, it's pushed onto the stack.
      - If it's a closing parenthesis, it checks if it matches the top of the stack. If not, it returns "no".
    - If the stack is empty at the end, it returns "yes"; otherwise, it returns "no".

- **`main()`**
  - **Purpose:** Command-line input and initiates the validation process.
  - **Logic:**
    - Checks if the correct number of arguments is provided.
    - Calls `is_valid()` with the input string and prints the result.

### Program Flow

1. The program starts by checking command-line arguments.
2. It reads the input string and passes it to the `is_valid` function.
3. The `is_valid` function uses a stack to validate the parentheses.
4. The result is printed ("yes" or "no").

---
## Calculator (`calculator.py`)


Calculates equations containing numbers, operators (`+`, `-`, `*`, `/`, `^`), and parentheses. It handles operator precedence and parentheses using recursive function calls.

### Methods

- **`isNumber(Number: str) -> bool`**
  - **Purpose:** Checks if a character is a numeric digit.
  - **Parameters:** 
    - `Number` (str): The character to check.
  - **Returns:** 
    - `True` if the character is a digit, `False` otherwise.

- **`isOperator(Operator: str) -> bool`**
  - **Purpose:** Checks if a character is an operator or parenthesis.
  - **Parameters:** 
    - `Operator` (str): The character to check.
  - **Returns:** 
    - `True` if the character is an operator or parenthesis, `False` otherwise.

- **`Calc(Operator_number: int, Math_input: list) -> float`**
  - **Purpose:** Performs calculations based on the operator at a given index in the list.
  - **Parameters:**
    - `Operator_number` (int): The index of the operator in the list.
    - `Math_input` (list): List containing numbers and operators.
  - **Returns:**
    - The result of the calculation.
  - **Logic:**
    - Fetches operands from positions around the operator and performs the operation (addition, subtraction, multiplication, division, or exponentiation).

- **`Operator_Priority_Check(New_Operator: str, Old_Operator: str) -> bool`**
  - **Purpose:** Checks if the new operator has higher precedence than the old one.
  - **Parameters:**
    - `New_Operator` (str): The new operator.
    - `Old_Operator` (str): The current top operator.
  - **Returns:**
    - `True` if the new operator has higher precedence, `False` otherwise.
  - **Logic:**
    - Handles precedence and associativity rules for operators, giving priority to higher precedence operators or handling right-associative operations.

- **`parenthsis_handler(input_list: list) -> list or bool`**
  - **Purpose:** Finds and processes the innermost parentheses in an expression.
  - **Parameters:**
    - `input_list` (list): List of the mathematical expression components.
  - **Returns:**
    - A new list containing the evaluated parentheses expression, or `False` if no complete parentheses are found.
  - **Logic:**
    - Identifies the innermost parenthesis indices, extracts the expression inside, and returns it for evaluation.

- **`number_and_operator_splitter(string: str) -> list`**
  - **Purpose:** Splits a string into numbers and operators.
  - **Parameters:**
    - `string` (str): The input mathematical expression as a string.
  - **Returns:**
    - A list of numbers and operators.
  - **Logic:**
    - Iterates through the string, grouping characters into numbers or recognizing operators, and handles implicit multiplications (e.g., `2(3)`).

- **`func_parser(math_function: list) -> float`**
  - **Purpose:** Recursively evaluates the mathematical expression by resolving operators based on precedence.
  - **Parameters:**
    - `math_function` (list): List of numbers and operators.
  - **Returns:**
    - The final evaluated result of the expression.
  - **Logic:**
    - Identifies the operator with the highest precedence, performs the calculation, and recursively evaluates the simplified expression until one value remains.

- **`basic_logic(Inital_list: list) -> float`**
  - **Purpose:** Handles the overall evaluation process, including parentheses.
  - **Parameters:**
    - `Inital_list` (list): The initial list of numbers, operators, and parentheses.
  - **Returns:**
    - The evaluated result of the expression.
  - **Logic:**
    - Uses `parenthsis_handler` to resolve nested parentheses first, then uses `func_parser` for the main evaluation.

- **`main(expression: str)`**
  - **Purpose:** Entry point for evaluating an expression from command-line input.
  - **Parameters:**
    - `expression` (str): The mathematical expression as a string.
  - **Logic:**
    - Cleans the input expression, converts it into a list of numbers and operators, and calls `basic_logic` to evaluate it.
    - Prints the final result.

### Program Flow

1. The program reads the input from command-line arguments.
2. It uses `number_and_operator_splitter` to break the expression into components.
3. The `basic_logic` function evaluates the expression, resolving parentheses and operator precedence recursively.
4. The final result is printed to the console.
