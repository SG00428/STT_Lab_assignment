using System;

class Student {
    public string Name { get; set; }
    public int ID { get; set; }
    public double Marks { get; set; }

    // Constructor
    public Student(string name, int id, double marks) {
        Name = name;
        ID = id;
        Marks = marks;
    }

    // Copy Constructor
    public Student(Student s) {
        Name = s.Name;
        ID = s.ID;
        Marks = s.Marks;
    }

    public string GetGrade() {
        if (Marks >= 90) return "A";
        if (Marks >= 75) return "B";
        if (Marks >= 60) return "C";
        return "D";
    }

    public void Display() {
        Console.WriteLine($"Name: {Name}, ID: {ID}, Marks: {Marks}, Grade: {GetGrade()}");
    }
}

// Derived class
class StudentIITGN : Student {
    public string Hostel_Name_IITGN { get; set; }

    public StudentIITGN(string name, int id, double marks, string hostel)
        : base(name, id, marks) {
        Hostel_Name_IITGN = hostel;
    }

    public new void Display() {
        base.Display();
        Console.WriteLine($"Hostel: {Hostel_Name_IITGN}");
    }
}

class Prog {
    static void Main() {

        Student s1 = new Student("Sita", 101, 88.5);
        s1.Display();

        StudentIITGN student = new StudentIITGN("Geeta", 102, 92, "Ijokha");   // new attribute
        student.Display();
    }
}