import ast

source = """
def add(a, b):
    return a + b
"""

tree = ast.parse(source)
print(tree)