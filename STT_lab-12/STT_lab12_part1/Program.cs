using System;
using System.Threading;

namespace AlarmConsoleApp
{
    class Alarm
    {
        public delegate void AlarmEventHandler();
        public event AlarmEventHandler raiseAlarm;

        public void StartChecking(TimeSpan userTime)
        {
            while (true)
            {
                TimeSpan currentTime = DateTime.Now.TimeOfDay;
                Console.WriteLine("Current Time: " + currentTime.ToString(@"hh\:mm\:ss"));

                if (currentTime.Hours == userTime.Hours &&
                    currentTime.Minutes == userTime.Minutes &&
                    currentTime.Seconds == userTime.Seconds)
                {
                    raiseAlarm?.Invoke(); // Trigger the event
                    break;
                }

                Thread.Sleep(1000); // Check every second
            }
        }
    }

    class Program
    {
        static void Ring_alarm()
        {
            Console.WriteLine("Alarm! The time has been reached!");
        }

        static void Main(string[] args)
        {
            Console.Write("Enter time in HH:MM:SS format: ");
            string input = Console.ReadLine();

            if (TimeSpan.TryParse(input, out TimeSpan userTime))
            {
                Alarm alarm = new Alarm();
                alarm.raiseAlarm += Ring_alarm; // Subscribe the event
                alarm.StartChecking(userTime);  // Start the checking loop
            }
            else
            {
                Console.WriteLine("Invalid time format!");
            }
        }
    }
}
