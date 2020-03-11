using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.IO;
using System.Threading.Tasks;

namespace LightNovel
{
    class Scraper
    {
        private IList<string> Links = new List<string>();
        private IList<IWebElement> RowChapters = new List<IWebElement>();
        private IWebDriver Driver = new ChromeDriver();
        public string Link { get; set; }

        private string GetText()
        {
            // Select the text
            var text = Task.Run(() =>
            {
                return SelectText();
            });
            // Wait for the task to complete
            var await = text.GetAwaiter();
            // Get the result of the task
            return await.GetResult();
        }

        private string SelectText()
        {
            return Driver.FindElement(By.XPath("//*[@id='divReadContent']")).Text;
        }

        public void Start()
        {
            // Go to novelplanet.com
            Driver.Navigate().GoToUrl($"https://novelplanet.com/Novel/{Link}");
            // Pause for 7 seconds to by pass the cloudflare
            Thread.Sleep(7000);
            // Get all rowchapter elements and put the in a list
            RowChapters = Driver.FindElements(By.XPath("//*[@class='rowChapter']"));
            // Get all the links of the chapters and put them in an array
            foreach(IWebElement rowChapter in RowChapters)
            {
                Links.Add(rowChapter.FindElement(By.XPath(".//a")).GetAttribute("href"));
            }
            // Create a directory for the novel
            NovelManager.AddDirectory(Link);
            int i = 0;
            foreach(string link in Links.Reverse<string>())
            {
                Console.WriteLine(link);
                Driver.Navigate().GoToUrl(link);
                
                Thread.Sleep(10000);
                NovelManager.AddFile(Link, i.ToString(), text);
                i++;
            }



        }

        public void CreateFile(string text)
        {
            TextWriter tw = new StreamWriter("C:/LightNovel/LightNovel.txt", true);
            tw.WriteLine(text);
            tw.Close();
        }
    }
}
