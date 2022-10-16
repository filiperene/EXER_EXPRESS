#!/usr/bin/env python
# coding: utf-8

# ## EXERCICIO 1

# In[2]:


a = float(input("Insira o valor da incognita A: "))
if(a<0):
    print("NÚMERO INVÁLIDO ")
else:
    b = float(input("Insira o valor da incognita B: "))
    if(b<0):
        print("NÚMERO INVÁLIDO ")
    else:
        c = float(input("Insira o valor da incognita C: "))
        if(c<0):
            print("NÚMERO INVÁLIDO ")
        else:
            d = (b**2)-(4*a*c)
            print("O valor de DELTA é: ",d )
            e = 1/((1+a)**3)
            f = 1/(1+e)
            g = 1+f
            print("O valor da expressão é ",g)


# ## EXERCICIO 2
# 

# In[ ]:


import math 
a = 1/(2*math.log(2016,2))
b = 1/(5*math.log(2016,3))
c = 1/(10*math.log(2016,7))
print(a+b+c)


# In[4]:


import math
a = (7**(math.cos(25*(math.pi))))*(math.log(2))+(1/(math.sqrt(65)))
b = (75**8)*math.sin(36*math.pi)
print(a/b)


# In[5]:


a = 1/(1+(1/4))
b = 1/(2+a)
c = 1/(1+b)
d = 2+c
print(d)


# ## EXERCICIO 3

# In[8]:


import math
x1 = float(input("Digite a coordenada x do primeiro ponto "))
y1 = float(input("Digite a coordenada y do primeiro ponto "))
x2 = float(input("Digite a coordenada x do segundo ponto "))
y2 = float(input("Digite a coordenada y do segundo ponto "))
d = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print("A distância entre os pontos é de: ", d)


# ## EXERCICIO 4

# In[ ]:


seg = float(input("Digite quantos segundos deseja converter "))
minuto = seg//60
minr = seg%60
hor = minr//60
print("horas: " , hor)
print("minutos: " , minuto)
print("segundos: ", seg)


# ## EXERCICIO 5

# In[ ]:


cm = float(input("Digite quantos cm deseja converter: "))
m = cm//100
mr = cm%100

