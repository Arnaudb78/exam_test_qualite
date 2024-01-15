class MathOperations :

    def addition(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Veuillez entrer des nombres valides")

        return a + b
    
    def substraction(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Veuillez entrer des nombres valides")

        return a - b
    
    def multiplication(self,a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Veuillez entrer des nombres valides")

        return a * b
    
    def division(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Veuillez entrer des nombres valides")
        else:
            if b != 0:
                return a / b
            else:
                raise ValueError("Division par zéro impossible")
            
    def power(self, a : float, b : float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Veuillez entrer des nombres valides")
        if a < 0 and not isinstance(b, (int)):
            raise ValueError("Pas de puissances non entière pour les nombres négatifs")
        else:
            return a ** b