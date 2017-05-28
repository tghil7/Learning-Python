# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
  def print_welcome(first, last, middle=''):
      print "Welcome, {} {} {}".format(first, middle, last)
      print "Enjoy your stay!"
      
  print_welcome(first= "Anicet", last="Akanza")
  
  def get_total(items):
      total = 0
      for item in items:
          total = total + item
      return total
  
  items =[2, 5, 7]
  items_total = get_total(items)
  print items_total
  
  def get_square_and_cube(number):
     square = number ** 2
     cube   = number ** 3
     return square, cube
	 
  result = get_square_and_cube(5)
  print result
  
  def get_five_things():
      return 1, 2, 3, 4, 5
  
  a,b, c, d, e = get_five_things()
  print a
  
  def check_year(year):
      if len(year) != 4:
          print "{} is invalid as a year".format(year)
          return
      print "Good, that seems to work as a year"
      
  check_year("84")
  
  def test_args(item_one, item_two, *args):
      print item_one
      print item_two
      print args
      
  print test_args("Hello, ", "can you ", "hear ", "me","?")

