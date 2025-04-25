using System;
using System.Drawing;
using System.Windows.Forms;

namespace STT_lab12_part2 
{
    public partial class Form1 : Form
    {
        private System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
        private TimeSpan targetTime;
        private Random rand = new Random();

        public Form1()
        {
            InitializeComponent();
            timer.Interval = 1000; // 1 second
            timer.Tick += Timer_Tick;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (TimeSpan.TryParse(textBox1.Text, out targetTime))
            {
                timer.Start();
            }
            else
            {
                MessageBox.Show("Please enter time in HH:MM:SS format.");
            }
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            TimeSpan currentTime = DateTime.Now.TimeOfDay;

            this.BackColor = Color.FromArgb(rand.Next(256), rand.Next(256), rand.Next(256));

            if (currentTime.Hours == targetTime.Hours &&
                currentTime.Minutes == targetTime.Minutes &&
                currentTime.Seconds == targetTime.Seconds)
            {
                timer.Stop();
                MessageBox.Show("Alarm! Time matched.");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }
    }
}
