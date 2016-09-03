from stack import Stack
# to check balanced paranthesis
def balan_paren(str):
     s=Stack()
     balanced=True
     index=0
     while balanced and index<len(str):
          if str[index]=="(":
               s.push("(")
               balanced=True
          else:
               if s.isEmpty():
                    balanced=False
               else:
                    s.pop()
          index=index+1
     if balanced and s.isEmpty():
          return True
     else:
          return False
print(balan_paren("((())"))
