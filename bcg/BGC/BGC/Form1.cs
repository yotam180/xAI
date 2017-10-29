using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BGC
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            new System.Threading.Thread(() =>
            {
                while (true)
                {
                    System.Threading.Thread.Sleep(20000);
                    UpdateBG();
                }
            }).Start();
        }

        void UpdateBG ()
        {
            string cur = File.Exists("bg.txt") ? File.ReadAllText("bg.txt") : "";
            string to = GET("http://geofs-plugins.appspot.com/load.php?ids=wallpaper").Trim();
            if (cur != to)
            {
                File.WriteAllText("bg.txt", to);
                Wallpaper.Set(new Uri(to), Wallpaper.Style.Stretched);
            }
        }

        string GET(string url)
        {
            string html = string.Empty;

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                html = reader.ReadToEnd();
            }

            return html;
        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            Hide();
        }
    }
}
