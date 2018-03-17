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

namespace xAIDesktop
{
    public partial class gameSolo : Form
    {
        public string url = @"http://localhost:8080/xAI/";
        public string count = "";
        List<string> files;
        public gameSolo()
        {
            InitializeComponent();
            timer1.Enabled = false;
        }

        private void gameSolo_Load(object sender, EventArgs e)
        {
            textBox1.Text = "Enter waht you see...";
            textBox1.GotFocus += RemoveText;
            textBox1.LostFocus += AddText;
            files = new List<string>();
            files = ExtractJSON(new StreamReader(HttpGet(url + "getFiles.php?count=" + count)).ReadToEnd());
            timer1.Enabled = true;
        }
        
        public void RemoveText(object sender,EventArgs e)
        {
            textBox1.Text = "";
        }
        public void AddText(object sender, EventArgs e)
        {
            if (String.IsNullOrWhiteSpace(textBox1.Text))
                textBox1.Text = "Enter what you see...";
        }
        public void SetPicture()
        {
            if (files.Count == 0)
                return;
            Stream s = HttpGet(url + files[0]);
            pictureBox1.Image = Image.FromStream(s);
            files.RemoveAt(0);
        }
        public static List<string> ExtractJSON(string json)
        {
            char empty = (char)(0);
            json = json.Replace('[', empty);
            return new List<string>(json.Split(",".ToCharArray()));
        }
        public static Stream HttpGet(string url)j
        {
            string html = string.Empty;
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamRea)
            {
                return stream;
            }
            

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            SetPicture();
        }
    }
}
