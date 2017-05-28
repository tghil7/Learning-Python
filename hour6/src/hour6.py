# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":   
   toppings = []
   toppings.append('mango')
   toppings.append ('apple')
   toppings.append('grapes')
   toppings.append('orange')
   s = len(toppings)
   print s
   'mango' in toppings
   print toppings.count('orange')
   print toppings.index('orange')
   toppings.append('pineapple')
   toppings.append('pepperoni')
   print 'Please give me a topping:'
   s  = raw_input()
   if s in toppings:
        print 'Here are your toppings\n'
        print s
   else:
        print "Sorry we don't have"  + s
   print 'Please give me one more topping:'
   t = raw_input()
   if t in toppings:
        print 'Here are your toppings:'
        print t
   else:
        print "Sorry we don't have"  + t
   
        
       
   
   

