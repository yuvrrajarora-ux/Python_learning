a = True
t = type (a) #class <bool>

print(t)

b = 31
g = type (b) #class <int>

print(g)

c = 31.6
j = type (c) #class <float>

print(j)

d = "31.6" 
k = type (d) #class <string>

print(k)

a = "31.2"
b =  float (a) #a but the type should be float
t = type (b)

print(t)