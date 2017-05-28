# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "Hello World"
    name = input("Please enter the number of cookies you ate:")
    print name;
    year = raw_input("What year were you born [ex; 1980]")
    if len(year) != 4 or not year.isdigit():
          print "I'm sorry, I don't like that number"
    else:
          print "That's good, moving on"