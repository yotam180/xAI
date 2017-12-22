using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace xAIDesktop
{
    public partial class Test : Form
    {
        PictureBox picture = null;
        public Test()
        {
            InitializeComponent();
        }

        private void Test_Load(object sender, EventArgs e)
        {

            System.IO.Directory.GetFiles(System.IO.Directory.GetCurrentDirectory());
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                //string FilePath = textBox1.Text;
                DialogResult result = openFileDialog1.ShowDialog();
                string FilePath = openFileDialog1.FileName;
                Point p = new Point(Start.Location.X, Start.Location.Y);
                PictureBox pb = new PictureBox();
                pb.Name = textBox1.Text;
                pb.Location = p;
                pb.Image = Image.FromFile(FilePath);
                pb.Size = new Size(200, 285);
                pb.SizeMode = PictureBoxSizeMode.StretchImage;
                Controls.Add(pb);
                picture = pb;
            }
            catch {; }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //TODO: implement test part
        }
    }
}
