using System;
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
    public partial class gameEnter : Form
    {
        public string username = "";
        public gameEnter()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            gameSolo gs = new gameSolo();
            gs.count = textBox1.Text;
            this.Hide();
            gs.ShowDialog();
            this.Close();
        }

        private void gameEnter_Load(object sender, EventArgs e)
        {
            gameSolo gs = new gameSolo();
            textBox1.GotFocus += gs.RemoveText;
            textBox1.LostFocus += gs.AddText;
        }
    }
}
