'''
This program counts "words" and, Print words in the
each line with the words count
               coded by Sarath Sreedhar (https://www.instagram.com/_sarath_sreedhar)
'''
w= input("Enter sentence :")
print("Character count :",len(w))
d= len(w.split())
print("Word count :",d)
print("Letters count(including punchuations) :", len(w)-d-1)
f= w.split()
for k in range(1,d+1):
    for i in f :
        print(i,k)
        k+=1
        continue
    break
    