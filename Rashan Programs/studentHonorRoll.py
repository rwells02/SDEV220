'''
Author: Rashan Wells
Date: 01/26/2025
Version: 1.0
Program: studentHonorRoll.py // This app accepts student names and GPAs and will test if a student qualifies for
                                the dean's list or honor roll.
'''

def main():
    print("Student Honor Roll Qualification Check")
    while True:
        lastName = input("Please enter student's last name or 'ZZZ' to quit: ").capitalize()
        if lastName.upper() == 'ZZZ':
            print('Program Ended')
            break
        
        firstName = input("Enter the student's first name: ").capitalize()
        
        gpa = float(input("Enter the student's GPA: "))
        
        if gpa >= 3.5:
            print(f"Congratulations, {firstName} {lastName}! You have made the Dean's List!")
        elif gpa >= 3.25:
            print(f'Congratulations, {firstName} {lastName}! You have made Honor Roll!')
        else:
            print(f"Keep up the hard work, {firstName} {lastName}! You did not qualify for Honor Roll or the Dean's list at this time.")
main()
        

