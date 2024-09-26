from lark import Lark, Transformer
import sys

# Load the grammar from grammarl.lark
with open("grammar.lark", "r") as grammar_file:
    grammar = grammar_file.read()

# Create a Lark parser
parser = Lark(grammar, parser='lalr')

# Define an AST transformer
# In this special case the transformer is the identity function
class CalcTransformer(Transformer):
    def plus(self, items):
        return ('plus', items[0], items[1])
    
    def minus(self, items):
        return ('minus', items[0], items[1])

    def times(self, items):
        return ('times', items[0], items[1])
    
    def divide(self, items):
        return ('divide', items[0], items[1])

    def power(self, items):
        return ('power', items[0], items[1])

    def neg(self, items):
        return ('neg', items[0])

    def log(self, items):
        return ('log', items[0], items[1])

    def num(self, items):
        return ('num', float(items[0]))


# Function to evaluate the AST
def evaluate(ast):
    result = None
    if ast[0] == 'plus':
        result = evaluate(ast[1]) + evaluate(ast[2])
    elif ast[0] == 'minus':
        result = evaluate(ast[1]) - evaluate(ast[2])
    elif ast[0] == 'times':
        result = evaluate(ast[1]) * evaluate(ast[2])
    elif ast[0] == 'divide':
        result = evaluate(ast[1]) / evaluate(ast[2])
    elif ast[0] == 'power':
        result = evaluate(ast[1]) ** evaluate(ast[2])
    elif ast[0] == 'neg':
        result = -evaluate(ast[1])
    elif ast[0] == 'log':
        import math
        result = math.log(evaluate(ast[1]), evaluate(ast[2]))
    elif ast[0] == 'num':
        result = ast[1]

    return result




# Main execution
if __name__ == "__main__":
    calc_transformer = CalcTransformer() 
    input_string = sys.argv[1]
    tree = parser.parse(input_string)  # Add this line
    #print(tree)
    ast = calc_transformer.transform(tree)
    #print(ast)
    result = evaluate(ast)
    print(result)
