class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage:
if __name__ == "__main__":
    print("Sum:", Calculator.add(5, 3))
    print("Product:", Calculator.multiply(5, 3))