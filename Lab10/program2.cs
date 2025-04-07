using System;

class Calci
{
    private double num1;
    private double num2;

    public Calci(double num1, double num2)
    {
        this.num1 = num1;
        this.num2 = num2;
    }

    public double GetSum() => num1 + num2;
    public double GetDifference() => num1 - num2;
    public double GetProduct() => num1 * num2;
    public double GetQuotient() => num2 != 0 ? num1 / num2 : double.NaN;

    public void DisplayResults()
    {
        double sum = GetSum();
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {GetDifference()}");
        Console.WriteLine($"Product: {GetProduct()}");
        Console.WriteLine($"Quotient: {GetQuotient()}");

        // If-else to check even or odd
        if ((int)sum % 2 == 0)
        {
            Console.WriteLine("Sum is even.");
        }
        else
        {
            Console.WriteLine("Sum is odd.");
        }
    }
}

class Program1
{
    static void Main()
    {
        Console.Write("Enter first number: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter second number: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        Calculate calc = new Calculate(num1, num2);
        calc.DisplayResults();
    }
}