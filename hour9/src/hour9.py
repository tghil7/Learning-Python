# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

student_grade = {}
def add_student_grade():
    while True: 
               name = raw_input("Please give me the name of the student (q to quit):")              
               if name == 'q':
                       print "Ok, printing grades!"
                       for key, value in student_grade.iteritems():
                              print key, value
                       break
               grade = raw_input("Please give me their grade:")
               student_grade[name] = grade



if __name__ == "__main__":
    add_student_grade()
    
    
    
