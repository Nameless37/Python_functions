def zeros(s):
    d={"first_name":"","last_name":"","id":""}
    l=[]
    a=""
    for x in range(len(s)):
        if(s[x]!='0'):
            a=a+s[x]
        if(s[x]=='0' and s[x+1]!='0'):
            l.append(a)
            a=""
    l.append(a)        
    d={"first_name":l[0],"last_Name":l[1],"id":l[2]}
    print(d)
zeros("John000Doe000123")                