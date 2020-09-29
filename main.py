# Author: Dylan Ding dvd5567@psu.edu
# Collaborator: William O'Rourke wjo5083@psu.edu
# Collaborator: Adil Parikh axp592@psu.edu
# Collaborator: Christopher Kurcz cjk6056@psu.edu
# Section: 7
# Breakout: 8

def is_palindrome1(s):
  counter =0
  revste=s[::-1]
  for i in range (0,len(s),1):
    if revste[i]==s[i]:
      counter +=1
    else:
      counter +=0
  if counter == len(s):
    return True
  else:
   return False
   