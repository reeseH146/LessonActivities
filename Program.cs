using System;

namespace FizzBuzz{
    class FizzBuzz
    {
        public static int InputValidator(string Text){
            string? Input; // Temp var which stores user input
            int Result; // Stores value to return
            bool Valid = false; // Forces loop until conditions met
            do {
                Console.WriteLine(Text); // Prompts user to give input
                Input = Console.ReadLine(); // Reads input
                // Attempts to convert input and check if above -1 before ending loop
                try{
                    int Temp = Convert.ToInt32(Input); // Converts input to int and stores in Temp to work with
                    // Checks if the converted input is above -1 and ends loop if so
                    if (Temp >= 0){
                        Valid = true;
                    }
                    // Tells user input is not above -1
                    else{
                        Console.WriteLine("Input must be >= 0.");
                    }
                }
                // Cannot convert input to number
                catch{
                    Console.WriteLine("Input must be a number >= 0.");
                }
            }
            while (!Valid);
            Result = Convert.ToInt32(Input);
            return Result;
        }

        // Takes in a range of start and end of FizzBuzz program
        public static void FizzBuzzProced(int Start, int End){
            // Loops through range of numbers provided
            for (int i = Start; i <= End; i++){
                // Fizzbuzz
                if ((i % 3 == 0) && (i % 5 == 0)){
                    Console.WriteLine("FizzBuzz");
                }
                // Fizz
                else if (i % 3 == 0){
                    Console.WriteLine("Fizz");
                }
                // Buzz
                else if (i % 5 == 0){
                    Console.WriteLine("Buzz");
                }
                // Number if not FizzBuzz or Fizz or Buzz
                else{
                    Console.WriteLine(i);
                }
            }
        }
        // Main program which takes range of fizz buss and produces the output
        public static void Main(){
            Console.WriteLine("FizzBuzz program : Please enter the range you want to go through."); // Shows user what the program is
            int Start = InputValidator("Start number : ");
            int End = InputValidator("End number : ");
            FizzBuzzProced(Start, End);
        }
    }
}