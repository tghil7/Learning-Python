# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "Welcome to the receipt program!"
    total = 0
    while True:
        s = raw_input("Enter the value for the seat['q' for quit]:wq    ")        
        if  s == 'q':
            print total
            break
        elif s.isdigit():
            total += int (s)
            
        
