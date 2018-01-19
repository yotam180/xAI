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
    public partial class Form1 : Form
    {
        const string CATPATH = "catagories.txt";
        public Form1()
        {
            InitializeComponent();
        }
        /// <summary>
        /// this function adds the new catagory to the .txt file and to the listbox indicator
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
            if (exist(textBox1.Text))
                return;
            string fileCont="";
            string[] arr = File.ReadAllText(CATPATH).Split("\r\n".ToCharArray());
            List<string> items = new List<string>();
            for(int i=0;i<arr.Length;i++)
            {
                items.Add(arr[i]);
            }
            items.Add(textBox1.Text);
            File.WriteAllText(CATPATH, string.Empty);
            fileCont = items[0];
            //MessageBox.Show(items[0]);
            for(int i=1;i<items.Count;i++)
            {
                fileCont += "\n";
                fileCont += items[i];
            }
            File.WriteAllText(CATPATH, fileCont);
            LoadCatagories();
        }
        public bool exist(string st)
        {
            foreach(char i in st)
            {
                if(i<'a'||i>'z')
                {
                    return true;
                }
            }
            foreach (string i in listBox1.Items)
            {
                if (i.Equals(st))
                    return true;
            }
            return false;
        }
        private void LoadCatagories()
        {
            listBox1.Items.Clear();
            string content = File.ReadAllText(CATPATH);
            string[] arr = content.Split("\r\n".ToCharArray());
            foreach(string a in arr)
            {
                if(a.Length>0)
                {
                    listBox1.Items.Add(a);
                }
            }
            /*for(int i=0;i<listBox1.Items.Count;i++)
            {
                if(listBox1.Items[i].ToString().Length==0)
                {
                    listBox1.Items.RemoveAt(i);
                }
            }*/
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadCatagories();
            foreach(Control c in this.Controls)
            {
                if(c is Button)
                {
                    c.BackColor = Color.White;
                }
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Test t = new Test();
            this.Hide();
            t.ShowDialog();
            this.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Train t = new Train();
            this.Hide();
            t.ShowDialog();
            this.Close();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if(listBox1.SelectedItem!=null)
            {
                button4.Visible = true;
            }
            else
            {
                button4.Visible = false;
            }
        }
        public void updateCatagories()
        {
            string content = "";
            foreach(object item in listBox1.Items)
            {
                content += item.ToString()+"\r\n";
            }
            File.WriteAllText(CATPATH, content);
        }
        private void button4_Click(object sender, EventArgs e)
        {
            listBox1.Items.RemoveAt(listBox1.SelectedIndex);
            updateCatagories();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //listBox1.Items.Remove(listBox1.SelectedItem);
            //MessageBox.Show(listBox1.SelectedItem.ToString()+":"+listBox1.SelectedItem.ToString().Length);
        }
        ~Form1()
        {
            updateCatagories();
        }
    }
}
