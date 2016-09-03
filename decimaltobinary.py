# converting decimal to binary number
from stack import Stack
def dec_binary(num):
     s=Stack()
     while num>0:
          rem=num%2
          s.push(rem)
          num=num//2
     while not s.isEmpty():
          x=""
          y=str(s.pop)
          x=x+y
     return x
print (dec_binary(10))
