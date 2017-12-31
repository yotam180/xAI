﻿using System;
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
            foreach(string i in listBox1.Items)
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
            string[] arr = content.Split("\n".ToCharArray());
            foreach(string a in arr)
            {
                listBox1.Items.Add(a);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadCatagories();
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
    }
}