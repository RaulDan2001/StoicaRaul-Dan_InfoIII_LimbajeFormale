using System;
using System.Collections.Generic;

class Program
{
    static List<string> GeneratePalindromes(int length)
    {
        if (length == 1)
        {
            return new List<string> { "0", "1", "2" };
        }
        else if (length == 2)
        {
            return new List<string> { "00", "11", "22", "01", "10", "12", "21", "02", "20" };
        }
        else
        {
            List<string> palindromes = new List<string>();
            List<string> smallerPalindromes = GeneratePalindromes(length - 2);
            foreach (string palindrome in smallerPalindromes)
            {
                palindromes.Add("0" + palindrome + "0");
                palindromes.Add("1" + palindrome + "1");
                palindromes.Add("2" + palindrome + "2");
                palindromes.Add("0" + palindrome + "1");
                palindromes.Add("1" + palindrome + "0");
                palindromes.Add("1" + palindrome + "2");
                palindromes.Add("2" + palindrome + "1");
                palindromes.Add("0" + palindrome + "2");
                palindromes.Add("2" + palindrome + "0");
            }
            return palindromes;
        }
    }

    static void Main(string[] args)
    {
        for (int length = 1; length <= 5; length++)
        {
            List<string> palindromes = GeneratePalindromes(length);
            Console.WriteLine($"Palindroame de lungime {length}:");
            foreach (string palindrome in palindromes)
            {
                Console.WriteLine(palindrome);
            }
            Console.WriteLine();
        }
    }
}
