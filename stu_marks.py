import os
import csv

#Field names
fieldnames=["Name", "Math", "Science", "English", "Total", "Result(Pass/Fail)"]

#if file does'nt exist
if not os.path.exists("stu_marks.csv"):
    with open("stu_marks.csv", "w", newline="") as f:
        writer=csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

while True:
    choice=print("Choose one operation \n 1.Add Student \n 2.View All Students \n 3.Update Student \n 4.Delete Student \n 5.View only PASSED students \n 6.View Top scored Student \n 7.Search a Student \n 8.Sorted List by Total \n 9.Exit")
    option=int(input("Enter your Option(1,2,3,4,5,6,7,8,9): "))

    if option == 1:
        name= input("Enter Name: ")
        math= int(input("Enter Math Marks: "))
        science= int(input("Enter Science Marks: "))
        english= int(input("Enter English Marks: "))
        total= math + science + english
        result= "Pass" if total/3 >= 35 else "Fail"

        with open("stu_marks.csv", "a", newline="") as f:
            writer=csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({"Name":name, "Math":math, "Science":science, "English":english, "Total":total, "Result(Pass/Fail)":result})
            


    elif option == 2:
        with open("stu_marks.csv" , "r") as f:
            reader= csv.DictReader(f)
            for i in reader:
                print("-----Report-----")
                print("Name:",i["Name"], "\nMath:", i["Math"], "\nScience:",i["Science"], "\nEnglish:",i["English"], "\nTotal:",i["Total"], "\nResult:",i["Result(Pass/Fail)"] )
                print("----------------")
                


    elif option == 3:
        update_name=input("Enter the name of the student to update: ")
        found=False
        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            data=list(reader)
            for i in data:
                if i["Name"] == update_name:
                    found=True
                    new_math = int(input("Enter new Math Marks: "))
                    new_science = int(input("Enter new Science Marks: "))
                    new_english = int(input("Enter new English Marks: "))
                    new_total = new_math + new_science + new_english
                    new_result = "Pass" if new_total / 3 >= 35 else "Fail"


                    i["Math"]=str(new_math)
                    i["Science"]=str(new_science)
                    i["English"]=str(new_english)
                    i["Total"]=str(new_total)
                    i["Result(Pass/Fail)"]=str(new_result)
                    break

        if found:
            with open("stu_marks.csv", "w", newline="") as f:
                writer=csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
                print("Student record updated successfully.")

        else:
            print("No Student With That Name")


    elif option == 4:
        delete_name=input("Enter the name of student to delete: ")
        found=False

        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            data=list(reader)

        new_data=[]
        for i in data:
            if i["Name"] != delete_name:
                new_data.append(i)
            else:
                found= True

        if found:
            with open("stu_marks.csv", "w", newline="") as f:
                writer=csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_data)
                print("Student Deleted")
        else:
            print("Student Not Found")


    elif option == 5:
        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            p_f=list(reader)


        pass_stu=[]
        for i in p_f:
            if["Result(Pass/Fail)"] != "Fail":
                pass_stu.append(i)

        if pass_stu:
            for stu in pass_stu:
                print("-----Passed Students-----")
                print("Name:", stu["Name"], "\nMath:", stu["Math"], "\nScience:", stu["Science"], "\nEnglish:", stu["English"], "\nTotal:", stu["Total"])
                print("----------------------")
        else:
            print("No Passed Students")


    elif option ==  6:
        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            t_s=list(reader)

        max_total= max(int(i["Total"]) for i in t_s)

        print(f"Top Scoring Students With Total = {max_total}: \n")
        for i in t_s:
            if int(i["Total"]) == max_total:
                print("-----Topper-----")
                print("Name:", i["Name"], "\nMath:", i["Math"], "\nScience:", i["Science"], "\nEnglish:", i["English"], "\nTotal:", i["Total"])
                print("----------")

    elif option == 7:
        search_name=input("Enter a student name to search: ")
        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            stu_data=list(reader)
            found=False
        search=[]
        for i in stu_data:
            if i["Name"] == search_name:
                found=True
                search.append(i)
        for stud in search:
            print("----------")
            print("Name:",stud["Name"], "\nMath:",stud["Math"], "\nScience:",stud["Science"], "\nEnglish:",stud["English"], "\nTotal:",stud["Total"], "\nResult:",stud["Result(Pass/Fail)"])
            print("----------")
        if not found:
            print("Student Not Found")
    

        
    elif option == 8:
        with open("stu_marks.csv", "r") as f:
            reader=csv.DictReader(f)
            stu_data=list(reader)
        for i in stu_data:
            sort_data=sorted(stu_data, key=lambda i: int(i["Total"]), reverse=True)
        for s_m in sort_data:
            print("----------")
            print("Name:",s_m["Name"], "\nMath:",s_m["Math"], "\nScience:",s_m["Science"], "\nEnglish:",s_m["English"], "\nTotal:",s_m["Total"], "\nResult:",s_m["Result(Pass/Fail)"])
            print("----------")

    elif option == 9:
        break

    else:
        print("Invalid Option Entered. Enter Correct Option (1,2,3,4,5,6,7,8,9)")