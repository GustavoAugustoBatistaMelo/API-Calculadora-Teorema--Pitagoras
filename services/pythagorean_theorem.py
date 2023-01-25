import math

class PythagoreanTheorem():
    @staticmethod
    def calculate_hypotenuse(a, b):
        # h² = a² + b²
        
        return math.sqrt((a ** 2) + (b ** 2))
    
    @staticmethod
    def calculate_collared_peccary(x, h):
        # a² + b² = h²
        
        return math.sqrt((h ** 2) - (x ** 2))