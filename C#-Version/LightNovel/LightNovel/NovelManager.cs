using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LightNovel
{
    class NovelManager
    {
        // TODO:
        // Add files
        // Add directories
        // Remove directories
        // Remove files

        public static void AddNovelRoot()
        {
            string path = "c:/LightNovels";

            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
        }

        public static void AddDirectory(string novel)
        {
            string path = $"c:/LightNovels/{novel}";

            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
        }

        public static void AddFile(string novel, string name, string text)
        {
            string path = $"c:/LightNovels/{novel}/{name}.txt";

            if (!File.Exists(path))
            {
                TextWriter textWriter = new StreamWriter(path);
                textWriter.WriteLine(text);
            }
           
        }
    }
}
