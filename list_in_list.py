def print_lol(lol):
   # base case: list is empty.
   if not lol:
       return

   # break into first element (which might be a list)
   # and the rest of the list.
   first = lol[0]
   rest = lol[1:]

# do work...
   if type(first) == list:
#       if the first element is a list, print it as a list.
      print_lol(first)
   else:
#       otherwise, just print the first element
      print(first)

#now print the rest of the list
       print_lol(rest)
