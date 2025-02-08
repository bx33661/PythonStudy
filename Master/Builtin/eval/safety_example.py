import ast

def safe_eval(expr):
    """
    安全的eval替代方案，只允许基本的数学运算
    """
    try:
        # 解析表达式
        tree = ast.parse(expr, mode='eval')
        
        # 验证节点类型
        for node in ast.walk(tree):
            if not isinstance(node, (
                ast.Expression,
                ast.Num,
                ast.BinOp,
                ast.UnaryOp,
                ast.Add,
                ast.Sub,
                ast.Mult,
                ast.Div,
                ast.Constant
            )):
                raise ValueError("Disallowed expression")
        
        # 编译并执行
        code = compile(tree, '<string>', 'eval')
        return eval(code)
    except Exception as e:
        return f"Error: {str(e)}"

# 使用示例
print(safe_eval('2 + 2'))  # 安全：返回 4
print(safe_eval('2 * 3'))  # 安全：返回 6
print(safe_eval('__import__("os").system("ls")'))  # 安全：会抛出错误