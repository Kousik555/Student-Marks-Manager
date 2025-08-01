# Student Marks Manager

A command-line Python project to manage student marks using a CSV file. This project is beginner-friendly and helps understand core Python concepts like file handling, conditionals, loops, and CSV operations with DictWriter and DictReader.

---

## 📌 Features

- Add a student with marks in Math, Science, and English
- Automatically calculates total and pass/fail result
- View all student records
- Update an existing student's marks
- Delete a student by name
- View only students who passed
- Find top-scoring student(s)
- Search for a student by name
- View sorted list of students by total marks
- Menu-driven interface
- CSV-based persistent storage

---

## 🛠 Technologies Used

- Python 3
- CSV module (csv.DictWriter, csv.DictReader)
- File handling (os.path.exists())

---

## ▶ How to Run

1. Clone this repository  
   
   git clone https://github.com/your-username/student-marks-manager.git
   

2. Navigate to the folder  
   
   cd student-marks-manager
   

3. Run the Python script  
   
   python student_marks_manager.py
   

---

## 📂 Output Preview


Choose one operation 
 1.Add Student 
 2.View All Students 
 3.Update Student 
 4.Delete Student 
 5.View only PASSED students 
 6.View Top scored Student 
 7.Search a Student 
 8.Sorted List by Total 
 9.Exit


---

## 📄 File Structure


student-marks-manager/
│
├── student_marks_manager.py
├── stu_marks.csv  ← (auto-created after first run)
└── README.md


---

## 💡 Improvements You Can Add

- Input validation and error handling
- Unique student IDs
- Password-protected admin access
- Save scores by subject-wise toppers
- Export passed/failed students into separate files

---

## 🧑‍💻 Author

*[Your Name]*  
Feel free to fork and enhance the project. Contributions welcome!

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
