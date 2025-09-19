a=int(input("Enter 1 to turn Text→Binary\nEnter 2 to turn Binary→Text\n:"))
#Text to Binary#
if a==1:
    n=input("Enter Text: ")
    l=len(n)
    x=""
    for i in range(l):
        s=bin(ord(n[i]))[2:]
        while len(s)<8:
            s="0"+s
        print(n[i], ":", s)
        x+=s+" "
    print(x)
#Binary to Text#
elif a==2:
    b=input("Enter Binary: ")
    n=b.split()
    l=len(n)
    x=""
    for i in range(l):
          s=chr(int(n[i], 2))
          print(n[i], ":", s)
          x+=s
    print(x)
