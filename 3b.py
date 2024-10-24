class Calculator:
    def add(self, a, b=0, c=0):
        """Adds up to three numbers."""
        return a + b + c

# Example usage:
calc = Calculator()

print(calc.add(5, 10))         # Output: 15
print(calc.add(5, 10, 15))     # Output: 30
print(calc.add(5))             # Output: 5
