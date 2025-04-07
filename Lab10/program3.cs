using System;

class LoopsAndFunctions {
    static void PrintNumbers() {
        for (int i = 1; i <= 10; i++) {
            Console.Write(i + " ");
        }
        Console.WriteLine();
    }

    static void Main() {
        PrintNumbers();

        while (true) {
            Console.Write("Enter a number (or type 'exit' to stop): ");
            string input = Console.ReadLine();
            if (input.ToLower() == "exit") break;

            if (int.TryParse(input, out int num)) {
                Console.WriteLine($"Factorial of {num} is {Factorial(num)}");
            } else {
                Console.WriteLine("Invalid input! Please enter a number.");
            }
        }
    }

    static long Factorial(int n) {
        if (n <= 1) return 1;
        return n * Factorial(n - 1);
    }
}