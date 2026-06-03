class Character:
    def __init__(self, name, expressions):
        self.Name = name
        self.Expressions = expressions

    def GetExpression(self, index):
        if index < len(self.Expressions):
            return self.Expressions[index]

        return None