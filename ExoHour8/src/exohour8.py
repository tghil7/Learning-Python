# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    list_of_students= ["Yves", "Jastin", "Rocs", "Anicet"]
    print "Welcome to the student checker!"
    
    def student_print():
        while True:
                 name = raw_input("Please give the name of a student(enter 'q' to quit):")
                 if name =='q':
                    print "Goodbye!"
                    break
                    
                 elif name in list_of_students:
                    print "Yes, that student is enrolled in the class"
                    
                 elif name not in list_of_students:
                    print "No, that student is not in the class"
                    
                 
   
    student_print()
