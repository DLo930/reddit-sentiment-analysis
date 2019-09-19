# Code for checking solutions to the last part of 2a
# run with "python -i 2a.py"
# check(-1, -1, -1)

# Mods something into range of a 32-bit 2s complement the hard way
def tinymod(z):
   while z > (2**31 - 1): z = z - 2**32
   while z < -(2**31): z = z + 2**32
   return z

# C0-style addition
def add(x, y):
   z = x + y
   return tinymod(z)

# Re-implementation of safeadd in C0
def safeadd(a,b,c):
   if (a > 0 and b > 0 and c > 0 and add(add(a,b),c) < 0): return False
   if (a < 0 and b < 0 and c < 0 and add(add(a,b),c) > 0): return False
   return True

# Checks for answers to 2a
def check(a,b,c):
   a = tinymod(a)
   print("a = "+str(a))
   b = tinymod(b)
   print("b = "+str(b))
   c = tinymod(c)
   print("c = "+str(c))
   print("a+b+c = "+str(add(add(a,b),c)))

   if a+b+c == add(add(a,b),c):
       print("Addition is actually safe...")
       if safeadd(a,b,c):
          print("But safeadd returns true... INCORRECT AS A COUNTEREX")
       else:
          print("And safeadd returns false... CORRECT COUNTEREX")
   else:
       print("Addition is not actually safe...")
       if safeadd(a,b,c):
          print("And safeadd returns true... CORRECT COUNTEREX")
       else:
          print("But safeadd returns false... INCORRECT AS A COUNTEREX")
