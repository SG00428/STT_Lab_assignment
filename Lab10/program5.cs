using System;

class Calculate
{
    private double num1;
    private double num2;

    public Calculate(double num1, double num2)
    {
        this.num1 = num1;
        this.num2 = num2;
    }

    public double GetSum() => num1 + num2;
    public double GetDifference() => num1 - num2;
    public double GetProduct() => num1 * num2;
    public double GetQuotient()
    {
        try           // exception handling
        {
            if (num2 == 0)
                throw new DivideByZeroException("Cannot divide by zero.");
            return num1 / num2;
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
            return double.NaN;
        }
    }

    public void DisplayResults()
    {
        double sum = GetSum();
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {GetDifference()}");
        Console.WriteLine($"Product: {GetProduct()}");
        Console.WriteLine($"Quotient: {GetQuotient()}");

        // If-else to check even or odd
        if ((int)sum % 2 == 0)
            Console.WriteLine("Sum is even.");
        else
            Console.WriteLine("Sum is odd.");
    }
}

class Progrm
{
    static void Main()
    {
        try
        {
            Console.Write("Enter first number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter second number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            Calculate calc = new Calculate(num1, num2);
            calc.DisplayResults();
        }
        catch (FormatException)
        {
            Console.WriteLine("Error: Invalid input! Please enter numeric values.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Unexpected Error: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Execution completed.");
        }
    }
}


