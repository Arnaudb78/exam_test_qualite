ERROR_INVALID_PARAMS = "Veuillez entrer des nombres valides"
ERROR_ZERO_DIVISION = "Division par zéro impossible"
ERROR_POWER = "Pas de puissances non entière pour les nombres négatifs"

NUMBER = "Saisissez le nombre : "
FIRST_NUMBER = "Saisissez le premier nombre : "
SECOND_NUMBER = "Saisissez le second nombre : "
RESULT = "Voici votre résultat : "

class MathOperations:

    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.number = 0
        self.calcul = ''

    def addition(self, a, b):
        if not isinstance(a, (int, float))or not isinstance(b, (int, float)):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a + b
    
    def substraction(self, a, b):
        if not (isinstance(a, (int, float))) or not (isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a - b
    
    def multiplication(self, a, b):
        if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a * b
    
    def division(self, a, b):
        if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b != 0:
            return a / b
        raise ValueError(ERROR_ZERO_DIVISION)
            
    def power(self, a, b):
        if not (isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if a < 0 and not isinstance(b, (int)):
            raise ValueError(ERROR_POWER)
        return a ** b
        
    def modulo(self, a, b):
        if not (isinstance(a, (int)) or not isinstance(b, (int))):
            raise ValueError(ERROR_INVALID_PARAMS)
        if b == 0:
            raise ValueError(ERROR_ZERO_DIVISION)
        return a % b
    
    def main(self):
        go = True
        while go:
            print('Veuillez choisir une opération parmis les suivantes : ')
            print('addition -> +')
            print('soustraction -> -')
            print('multiplication -> *')
            print('division -> /')
            print('puissance -> **')
            print('modulo -> %')
            self.calcul = input('')
            if self.calcul == "":
                print(NUMBER)
                self.number = input()
                print(self.number)
            else:
                print(FIRST_NUMBER)
                self.first_number = input()
                print(SECOND_NUMBER)
                self.second_number = input()
            self.calcul_choice(self.calcul)
            print('Souhaitez vous opérer une nouvelle fois ?')
            again = input('yes / no : ----> ')
            if again == 'no':
                go = False

    def calcul_choice(self, operation):
        if operation not in ['+', '-', '*', '/', '**', '', '%']:
            raise ValueError('wesh')
        if operation == "":
            print(self.number)
        else:
            if operation == "+":
                result = self.addition(self.first_number, self.second_number)
                
            elif operation == "-":
                result = self.substraction(self.first_number, self.second_number)
                
            elif operation == "*":
                result = self.multiplication(self.first_number, self.second_number)
                
            elif operation == "/":
                result = self.division(self.first_number, self.second_number)
                
            elif operation == "**":
                result = self.power(self.first_number, self.second_number)
                
            elif operation == "%":
                result = self.modulo(self.first_number, self.second_number)

            print(result)
                

