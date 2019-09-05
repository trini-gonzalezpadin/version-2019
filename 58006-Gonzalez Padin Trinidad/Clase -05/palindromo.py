def palindromo(palabra):
  #  a,b=list(palabra.replace(" ","")) ,list(palabra.replace(" ",""))
   # b.reverse()
   # print(a)
    #print(b)
    #return a==b
    b=list(palabra.replace(" " ,""))
    b.reverse()
    return list(palabra.replace(" ",""))==b

if __name__ == "__main__":
    print("Ingrese frase")
    palabra=input()
    print(palindromo(palabra))