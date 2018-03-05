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
    public partial class login : Form
    {
        public login()
        {
            InitializeComponent();
        }

        private void login_Load(object sender, EventArgs e)
        {
            foreach(Control item in this.Controls)
            {
                if (item is TextBox)
                {
                    item.BackColor = Color.Black;
                    item.ForeColor = Color.White;
                }
                else
                    item.BackColor = Color.White;
            }
        }
        private void updateTextBoxes()
        {
            foreach(Control item in this.Controls)
            {
                if(item is TextBox)
                {
                    if (((TextBox)item).Text == "")
                    {
                        Invoke((MethodInvoker)delegate ()
                        {
                            item.Text = item.Name;
                            item.ForeColor = Color.LightGray;
                        });
                    }
                    else if(((TextBox)item).Text!=item.Name)
                    {
                        Invoke((MethodInvoker)delegate () { item.ForeColor = Color.White; });
                    }
                }
            }
        }
    }
}
