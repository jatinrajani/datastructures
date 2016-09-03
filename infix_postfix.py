from stack import Stack
def infix_postfix(str):
     s=Stack()
     l=""
     y=[]
     index=0
    
     while index <len(str):
          symbol=str[index]
          if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
               y.append(symbol)
          else:
               if symbol in "*/+-" and higprece(s.peek(),symbol) and not s.isEmpty() :
                    s.push(symbol)
               else:
                    y.append(s.pop())
                    
          index =index+1
     print y
def higprece(open,close):
     x=dict()
     x["*"]=3
     x["/"]=3
     x["+"]=2
     x["-"]=1
     if x[open]>x[close]:
          return true
     else:
          return false
          
infix_postfix("A+B")
