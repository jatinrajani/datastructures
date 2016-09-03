from stack import Stack
def balenparen(str):
     balanced=True
     index=0
     s=Stack()
     if balanced and index<len(str):
          symbol=str[index]
          if symbol in'{[(':
               balanced=True
               s.push(symbol)
          else:
               if s.isEmpty():
                    balanced =False
               else:
                    top=s.pop()
                    if not matches(top,symbol):
                         balanced=False
          index=index+1
     
     if balanced and s.isEmpty():
           return True
     else:
          return False
def matches(open,close):
     opens="{(["
     closers="})]"
     return opens.index(open)==closers.index(close)
print (balenparen('{{{]]]'))
