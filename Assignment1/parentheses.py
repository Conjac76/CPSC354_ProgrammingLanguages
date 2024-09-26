import sys

def is_valid(s):
    stack = []

    # Map closing parentheses with their corresponding opening parentheses
    close_to_open = {')': '(', '}': '{', ']': '['}

    # Iterate over each character in the string
    for char in s:
        # If it's an opening parenthesis, push it onto the stack
        if char in close_to_open.values():
            stack.append(char)
        # If it's a closing parenthesis, check if it matches the top of the stack
        elif char in close_to_open.keys():
            if stack == [] or stack.pop() != close_to_open[char]:
                return "no"
    
    # If the stack is empty, all parentheses were matched; otherwise, they weren't
    return "yes" if not stack else "no"

def main():
    # command line arguments
    if len(sys.argv) != 2:
        print("Usage: python parentheses.py \"<input_string>\"")
        return

    input_string = sys.argv[1]
    result = is_valid(input_string)
    print(result)

if __name__ == "__main__":
    main()
