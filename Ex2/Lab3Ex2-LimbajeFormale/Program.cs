using System;
using System.IO;
using System.Reflection.Emit;
using System.Text.RegularExpressions;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Introduceti calea catre fisierul text de verificat:");
        string filePath = Console.ReadLine();
    
        try
        {
            string fileContent = File.ReadAllText(filePath);

            // Definirea expresiilor regulate pentru fiecare secțiune a facturii
            string clientInfoPattern = @"Client: .+";
            string productDetailsPattern = @"Produs: .+; Cantitate: \d+; Pret: \d+(\.\d+)?; TVA: \d+(\.\d+)?%";

            // Verificarea formatului utilizând expresii regulate
            bool clientInfoMatch = Regex.IsMatch(fileContent, clientInfoPattern);
            bool productDetailsMatch = Regex.IsMatch(fileContent, productDetailsPattern);

            // Identificarea și afișarea erorilor
            if (!clientInfoMatch)
            {
                Console.WriteLine("Eroare: Informatiile despre client nu respecta formatul specificat.");
            }
            if (!productDetailsMatch)
            {
                Console.WriteLine("Eroare: Detaliile produselor nu respecta formatul specificat.");
            }

            // Afișarea unui mesaj în cazul în care fișierul respectă formatul
            if (clientInfoMatch && productDetailsMatch)
            {
                Console.WriteLine("Fisierul respecta formatul specificat.");
            }
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Eroare: Fisierul nu a fost gasit.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Eroare necunoscuta: {ex.Message}");
        }
    }
}

