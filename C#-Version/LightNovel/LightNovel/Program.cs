using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LightNovel
{
    class Program
    {
        // Shows list of actions and get an action
        static void Actions()
        {
            // List of actions
            Console.WriteLine("\r\nOptions\r\n", SetColor(ConsoleColor.White));
            Console.WriteLine("- Add a novel: { add }");
            Console.WriteLine("- Read a novel: { read }");
            Console.WriteLine("- Remove a novel: { remove }");
            Console.WriteLine("- Get mp3 file: { mp3 }");
            Console.WriteLine("- Quit application: { q }");
            // Get action
            Console.Write("\r\nChoose an option from the above: ", SetColor(ConsoleColor.DarkGray));
            // Validate the action
            ValidateAction(Console.ReadLine());
        }

        // Check if an action is valid
        static void ValidateAction(string action)
        {
            // Empty line
            Console.Clear();
            // Check if action is valid
            switch (action)
            {
                case "add":
                    Add();
                    break;
                case "read":
                    Console.WriteLine("read");
                    break;
                case "remove":
                    Console.WriteLine("remove");
                    break;
                case "mp3":
                    Console.WriteLine("mp3");
                    break;
                case "q":
                    break;
                default:
                    Console.WriteLine("ERROR: Given action isn't valid, please try again", SetColor(ConsoleColor.Red));
                    Actions();
                    break;
            }
        }

        static void Main(string[] args)
        {
            Scraper collector = new Scraper()
            {
                Link = "Tensei-Shitara-Slime-Datta-Ken-WN"
            };

            NovelManager.AddNovelRoot();

            collector.Start();
            //// Welcoming message
            //Console.WriteLine("Welcome to the LightNovel reader", SetColor(ConsoleColor.Cyan));
            //// Get action of user
            //Actions();
        }

        // Method for changing the color in the terminal
        static ConsoleColor SetColor(ConsoleColor Color)
        {
            return Console.ForegroundColor = Color;
        }

        static void Add()
        {
            // Explanations for users
            Console.WriteLine("LightNovel uses a website named 'novelplanet' to obtain the novels", SetColor(ConsoleColor.Cyan));
            Console.WriteLine("\r\nUsage:\r\n", SetColor(ConsoleColor.White));
            Console.WriteLine("1. Go to novelplanet.com");
            Console.WriteLine("2. Search for your novel (Don't mind the ads)");
            Console.WriteLine("3. Click on the novel link");
            Console.WriteLine("4. Select the name from the link");
            Console.WriteLine("\r\nEXAMPLE:\r\n", SetColor(ConsoleColor.Yellow));
            Console.WriteLine("link: \"https://novelplanet.com/Novel/Tensei-Shitara-Slime-Datta-Ken-WN\"");
            Console.WriteLine("copy: \"Tensei-Shitara-Slime-Datta-Ken-WN\"\r\n");
            Console.WriteLine("5. Paste link in console", SetColor(ConsoleColor.White));
            Console.WriteLine("6. Press enter, a browser will now open and will go to the specified page and wil start collecting the chapters.");
            // Get link
            Console.Write("\r\nName of novel: ", SetColor(ConsoleColor.DarkGray));
            string link = Console.ReadLine();

            if (!string.IsNullOrWhiteSpace(link))
            {
                Scraper collector = new Scraper()
                {
                    Link = link
                };

                NovelManager.AddNovelRoot();
                collector.Start();
            }
            else
            {
                Console.Clear();
                Console.WriteLine("You've been sent back", SetColor(ConsoleColor.Cyan));
                Actions();
            }
        }


    }
}
