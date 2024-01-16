ERROR_INVALID_PARAMS = "Veuillez entrer des nombres valides"
ERROR_ZERO_DIVISION = "Division par zéro impossible"
ERROR_POWER = "Pas de puissances non entière pour les nombres négatifs"

class MathOperations :

    def addition(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a + b
    
    def substraction(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError(ERROR_INVALID_PARAMS)
        return a - b
    
    def multiplication(self,a : float, b : float):
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