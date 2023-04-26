using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("What is this new place?");
            Console.WriteLine("Oh and who might you be?");
            string name = Console.ReadLine();
            Console.WriteLine("Why, hello there General " + name + "!");

        }
    }
}