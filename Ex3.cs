using System;
using System.Collections.Generic;

class MainClass
{
    static List<string> GenerateStringsGrammar1(int maxLength)
    {
        List<string> strings = new List<string>();
        GenerateStringsGrammar1Helper("AB", "", maxLength, strings);
        return strings;
    }

    static void GenerateStringsGrammar1Helper(string rule, string currentString, int maxLength, List<string> strings)
    {
        if (currentString.Length == maxLength)
        {
            strings.Add(currentString);
            return;
        }

        foreach (char c in rule)
        {
            if (c == 'A')
            {
                GenerateStringsGrammar1Helper("aA", currentString + 'a', maxLength, strings);
            }
            else if (c == 'B')
            {
                GenerateStringsGrammar1Helper("bB", currentString + 'b', maxLength, strings);
            }
            else
            {
                GenerateStringsGrammar1Helper("", currentString, maxLength, strings);
            }
        }
    }

    
    static List<string> GenerateStringsGrammar2(int maxLength)
    {
        List<string> strings = new List<string>();
        GenerateStringsGrammar2Helper("X", "", maxLength, strings);
        return strings;
    }

    static void GenerateStringsGrammar2Helper(string rule, string currentString, int maxLength, List<string> strings)
    {
        if (currentString.Length == maxLength)
        {
            strings.Add(currentString);
            return;
        }

        switch (rule)
        {
            case "X":
                GenerateStringsGrammar2Helper("0Y", currentString + '0', maxLength, strings);
                GenerateStringsGrammar2Helper("1Z", currentString + '1', maxLength, strings);
                break;
            case "Y":
                GenerateStringsGrammar2Helper("2", currentString + '2', maxLength, strings);
                GenerateStringsGrammar2Helper("X", currentString, maxLength, strings);
                break;
            case "Z":
                GenerateStringsGrammar2Helper("3", currentString + '3', maxLength, strings);
                GenerateStringsGrammar2Helper("4", currentString + '4', maxLength, strings);
                GenerateStringsGrammar2Helper("X", currentString, maxLength, strings);
                break;
        }
    }

    public static void Main(string[] args)
    {
        
        Console.WriteLine("Gramatica 1:");
        List<string> stringsGrammar1 = GenerateStringsGrammar1(5);
        foreach (string str in stringsGrammar1)
        {
            Console.WriteLine(str);
        }

        
        Console.WriteLine("\nGramatica 2:");
        List<string> stringsGrammar2 = GenerateStringsGrammar2(5);
        foreach (string str in stringsGrammar2)
        {
            Console.WriteLine(str);
        }
    }
}
