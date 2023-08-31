import argparse

class Fibonacci:
    """
    A class to represent the Fibonacci sequence.

    This class generates the Fibonacci sequence based on user-defined starting values.
    By default, the Fibonacci sequence starts with 0 and 1, but this implementation allows 
    the user to specify any two starting values.

    Attributes:
    ----------
    a : int
        The first number in the Fibonacci sequence.
    b : int
        The second number in the Fibonacci sequence.
    n : int
        The number of terms to be generated in the sequence.

    Methods:
    --------
    generate_sequence():
        Returns the Fibonacci sequence up to the nth term.
    display_sequence():
        Prints the Fibonacci sequence up to the nth term.
    """
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def generate_sequence(self):
        sequence = [self.a, self.b]
        for i in range(2, self.n):  # start from 2 because we already have 2 numbers
            c = sequence[-1] + sequence[-2]
            sequence.append(c)
        return sequence

    def display_sequence(self):
        sequence = self.generate_sequence()
        for num in sequence:
            print(num)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci Sequence")
    parser.add_argument("a", type=int, help="The first number of the Fibonacci sequence")
    parser.add_argument("b", type=int, help="The second number of the Fibonacci sequence")
    parser.add_argument("n", type=int, help="The number of terms to be displayed in the sequence")

    args = parser.parse_args()

    fibonacci = Fibonacci(args.a, args.b, args.n)
    fibonacci.display_sequence()