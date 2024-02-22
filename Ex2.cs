using System;
using System.Collections.Generic;

class MainClass
{
    static List<string> GenerateStrings(int iteration, List<string> previousStrings)
    {
        List<string> newStrings = new List<string>();

        foreach (string str in previousStrings)
        {
            if (iteration == 1)
            {
                newStrings.Add(str + "aa" + str);
                newStrings.Add(str + "bb" + str);
                newStrings.Add("aa");
                newStrings.Add("bb");
            }
            else
            {
                newStrings.Add(str + "a" + str);
                newStrings.Add(str + "b" + str);
                newStrings.Add("a" + str);
                newStrings.Add("b" + str);
                newStrings.Add(str + "a");
                newStrings.Add(str + "b");
            }
        }

        if (iteration > 1)
        {
            newStrings.AddRange(GenerateStrings(iteration - 1, newStrings));
        }

        return newStrings;
    }

    public static void Main(string[] args)
    {
        int iterations = 3;
        List<string> initialStrings = new List<string> { "a", "b" };

        for (int i = 1; i <= iterations; i++)
        {
            List<string> generatedStrings = GenerateStrings(i, initialStrings);

            Console.WriteLine($"Iterația {i}:");
            foreach (string str in generatedStrings)
            {
                Console.WriteLine(str);
            }
            Console.WriteLine();
        }
    }
}
