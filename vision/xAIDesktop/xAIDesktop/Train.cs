﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xAIDesktop
{
    public partial class Train : Form
    {
        const int ROWLEN = 5;
        List<PictureBox> pictures = new List<PictureBox>();
        public Train()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string FilePath = textBox2.Text;
            //FileStream fs = new FileStream(FilePath, FileMode.Open);
            Point p;
            if (pictures.Count < ROWLEN)
                p = new Point(Start.Location.X + pictures.Count * 70, Start.Location.Y);
            else
                p = new Point(Start.Location.X + (pictures.Count % ROWLEN) * 70 ,Start.Location.Y + ((pictures.Count / ROWLEN) * 100));
            PictureBox pb = new PictureBox();
            string[] temp = FilePath.Split(@"\".ToCharArray());
            temp = temp[temp.Length - 1].Split(@".".ToCharArray());
            int c = getNameCount(temp[0]);
            pb.Name = c == 0 ? temp[0] : temp[0] + c;
            pb.Image = Image.FromFile(FilePath);
            pb.Location = p;
            pb.Size = new Size(62, 90);
            pb.SizeMode = PictureBoxSizeMode.StretchImage;
            this.Controls.Add(pb);
            pictures.Add(pb);
        }
        private int getNameCount(string name)
        {
            int count = 0;
            foreach (PictureBox p in pictures)
                if (p.Name == name)
                    count++;
            return count;
        }
        private void button2_Click(object sender, EventArgs e)
        {
            //TODO: add the training part
        }
    }
}
