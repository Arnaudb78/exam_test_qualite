ERROR_INVALID_PARAMS = "Veuillez entrer des nombres valides"
ERROR_ZERO_DIVISION = "Division par zéro impossible"
ERROR_POWER = "Pas de puissances non entière pour les nombres négatifs"
ERROR_OPERAND = "Une expression doit contenir au moins une opérande"
ERROR_EXPRESSION = "Expression invalid"
USER_ANSWER = "Voulez vous effectuer une opération ?"
USER_CHOICE = "Saisir O pour oui, * pour non : "
USER_CALCUL = "Saisir votre calcul :"
END_PROGRAM = "Programme terminé."



class MathOperations :
    def __init__(self):
        self.operators = {
            '+': self.addition,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division,
            '**': self.power,
            '%': self.modulo
        }

    def addition(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a + b
    
    def subtraction(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a - b
    
    def multiplication(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a * b
    
    def division(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b != 0:
            return a / b
        raise ValueError(ERROR_ZERO_DIVISION)
            
    def power(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if a < 0 and not isinstance(b, (int)):
            raise ValueError(ERROR_POWER)
        return a ** b
        
    def modulo(self, a : float, b : float):
        if not (isinstance(a, (int)) and isinstance(b, (int))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b == 0:
            raise ValueError(ERROR_ZERO_DIVISION)
        return a % b
    
    def evaluate(self, calc):
        if calc == []:
            raise ValueError(ERROR_OPERAND)
        res = float(calc[0])
        for i in range(1, len(calc), 2):
            operator = self.operators.get(calc[i])
            if not operator:
                raise ValueError(ERROR_EXPRESSION)
            operand = float(calc[i+1])
            res = operator(res, operand)
        return res
    
    def parse(self, expression):
        return [op for op in expression.split(' ') if op.strip() != '']
    
    def main(self):
        print(USER_ANSWER)
        choice = 'O'
        while choice == 'O':
            choice = input(USER_CHOICE)
        
            if choice == '*':
                print(END_PROGRAM)
                break  
            else:
                expression = input(USER_CALCUL)
                calc = self.parse(expression)
                result = self.evaluate(calc)
                print("Le résultat est : " + str(result))


if __name__ == "__main__":
    math_ops = MathOperations()
    math_ops.main()