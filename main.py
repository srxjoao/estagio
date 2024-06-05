i = 1
while i > 0:
  primo = True
  for j in range  (2,i,1):
    if i%j == 0:
      primo = False
  if primo:
     print(i)
  i += 1
print('acabou')