def get_middle(s):
    return s[(len(s)//2)-1:(len(s)//2)+1] if len(s) % 2 == 0 else s[(len(s)//2)]


print(get_middle("test"))


'''Best Practices'''
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]