"""
Create a menu driven app, where users can store their information in Python Dict and Lists, 
Users must be able to store
1. Personal Information (name, email , address, phone)
2. Academic Qualification(institution_name, passed_year, faculty)
3. Hobbies
4. Skills
5. Achievements

Menu Must look like
a. Show your full CV
b. Add/update personal information
c. Add/Update Hobbies
d. Add/Update Skills
e. Add/Update achievements
"""

student_data = {
    'personal_information' : {},
    'academic_qualification' : {},
    'hobbies' : [],
    'skills' : [],
    'achievements' : []
}

print("=====================Menu driven app=====================")

choice = input("Enter your choice [a-e]: ")

def show_cv():

    print("===============CV================")

    for key, value in student_data['personal_information'].items():
        print(f"{key}: {value}")

    for key, value in student_data['academic_qualification'].items():
        print(f"{key}: {value}")

    print("\nHobbies:, ",".join(student_data["hobbies"]) if student_data["hobbies"] else "No hobbies added."")
    print("\nSkills:, ",".join(student_data["skills"]) if student_data["skills"] else "No skills added."" )
    print("\nAchievements: ",".join(student_data["achievements"]) if student_data["achievements"] else "No achievements added."")

    print("=================================")

def update_personal_information():
    print("Enter personal information: ")
    student_data["personal_information"]["name"] = input("Name: ")
    student_data["personal_information"]["email"] = input("Email: ")
    student_data["personal_information"]["address"] = input("Address: ")
    student_data["personal_information"]["phone"] = input("Phone: ")
    print("Personal information updated.")

def update_academic_qualification():
    print("Enter academic qualification: ")
    student_data["academic_qualification"]["institution_name"] = input("Institution Name: ")
    student_data["academic_qualification"]["passed_year"] = input("Passed Year: ")
    student_data["academic_qualification"]["faculty"] = input("Faculty: ")
    print("Academic qualification updated.")

def update_hobbies():
    print("Enter your hobbies: ")
    print("Hobbies updated.")
    pass

def update_skills():
    print("Enter your hobbies: ")
    print("Hobbies updated.")
    pass

def update_achievements():
    print("Enter your hobbies: ")
    print("Hobbies updated.")
    pass

def menu():

while True:

    choice = input("Choose an option [a-e]: ")

    if choice == 'a':
        show_cv()
    elif choice == 'b':
        update_personal_information()
    elif choice == 'c':
        update_hobbies()
    elif choice == 'd':
        update_skills()
    elif choice == 'e':
        update_achievements()
    elif choice == 'e':
        exit()
        break
    else:
        print()
        
menu()









