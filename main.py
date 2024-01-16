from math import sqrt

ERROR_INVALID_PARAMS = "Veuillez entrer des nombres valides"
ERROR_ZERO_DIVISION = "Division par zéro impossible"
ERROR_POWER = "Pas de puissances non entière pour les nombres négatifs"
ERROR_SQRT = "Pas de Racine carré d'un nombre négatif"
ERROR_OPERATION = "Veuillez rentrer une opération prises en charge !"

NUMBER = "Saisissez le nombre : "
FIRST_NUMBER = "Saisissez le premier nombre : "
SECOND_NUMBER = "Saisissez le second nombre : "
RESULT = "Voici votre résultat : "

class MathOperations:

    def __init__(self):

        self.run = True

        self.operation_choice = {
            "+": {
                "name": 'une addition',
                "calcul": self.addition
            },
            "-": {
                "name": 'une soustraction',
                "calcul": self.substraction
            },
            "*": {
                "name": 'une multiplication',
                "calcul": self.multiplication
            },
            "/": {
                "name": 'une division',
                "calcul": self.division
            },
            "**": {
                "name": 'une puissance',
                "calcul": self.power
            },
            "%": {
                "name": 'un modulo',
                "calcul": self.modulo
            },
            "sqrt": {
                "name": 'une racine carrée',
                "calcul": self.sqrt
            },
        }

        self.first_number = 0
        self.second_number = 0
        self.number = 0
        self.result = 0

    def addition(self, a, b):
        if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a + b
    
    def substraction(self, a, b):
        if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a - b
    
    def multiplication(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a * b
    
    def division(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b != 0:
            return a / b
        raise ValueError(ERROR_ZERO_DIVISION)
            
    def power(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if a < 0 and not isinstance(b, (int)):
            raise ValueError(ERROR_POWER)
        return a ** b
        
    def modulo(self, a, b):
        if not (isinstance(a, (int)) and isinstance(b, (int))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b == 0:
            raise ValueError(ERROR_ZERO_DIVISION)
        return a % b
    
    def sqrt(self, a):
        if type(a) not in [int, float]:
            raise ValueError(ERROR_INVALID_PARAMS)
        if a < 0:
            raise ValueError(ERROR_SQRT)
        return sqrt(a)
    
    def main(self):
        while self.run:
            print('Veuillez choisir une opération parmis les suivantes : ')
            for symbole, operation_info in self.operation_choice.items():
                print(f"Pour {operation_info['name']}, entrez '{symbole}'")
            self.calcul = input('')
            if self.calcul not in self.operation_choice:
                raise ValueError(ERROR_OPERATION)
            if self.calcul == "sqrt":
                print(NUMBER)
                self.number = float(input())
            else:
                print(FIRST_NUMBER)
                self.first_number = float(input())
                print(SECOND_NUMBER)
                self.second_number = float(input())
            self.calcul_choice(self.calcul)
            print('Souhaitez vous opérer une nouvelle fois ?')
            again = input('yes / no : ----> ')
            if again == 'no':
                self.run = False

    def calcul_choice(self, operation):
        if operation == "sqrt":
            self.result = self.operation_choice[operation]['calcul'](self.number)
        else:
            self.result = self.operation_choice[operation]['calcul'](self.first_number, self.second_number)
        print(self.result)
                

