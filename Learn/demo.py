def spell(txt):
    #your code goes here
    i = len(txt) - 1
    while i >= 0:
      print(txt[i])
      i -= 1
    
    

txt = input()
spell(txt)
