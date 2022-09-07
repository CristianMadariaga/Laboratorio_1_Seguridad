#Laboratorio 1 Seguridad Informática
#Alumno: Cristian Madariaga
#Profesor: Manuel Alba Escobar

#Abecedario en lista
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
       'P','Q','R','S','T','U','V','W','X','Y','Z']

#Funcion encriptado ROT(8)
def rot8(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 8 > 25:
                x = i - 26 + 8
                return a[x]
            elif i + 8 <= 25:
                x = i + 8
                return a[x]
        return v
    return''.join(map(lookup, s))
    
#Funcion desencriptado ROT(-8)
def des_rot8(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 8 > 25:
                x = i - 26 - 8
                return a[x]
            elif i + 8 <= 25:
                x = i - 8
                return a[x]
        return v
    return''.join(map(lookup, s))


#Funcion encriptado ROT(12)
def rot12(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 12 > 25:
                x = i - 26 + 12
                return a[x]
            elif i + 12 <= 25:
                x = i + 12
                return a[x]
        return v
    return''.join(map(lookup, s))
    
#Función desencriptado ROT(-12)
def des_rot12(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 12 > 25:
                x = i - 26 - 12
                return a[x]
            elif i + 12 <= 25:
                x = i - 12
                return a[x]
        return v
    return''.join(map(lookup, s))

#Función Vigenere (Colocar en tipo E para encriptar, D para desencriptar)
def vigenere(mensaje, llave, tipo):
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''
    t = mensaje.replace(" ","")
    k = llave.upper()
    for i in range(len(t)):
        letra_n = alfabeto.index(t[i])
        llave_n = alfabeto.index(k[i % len(k)])

        if tipo == "e" or tipo == "E":
            valor = (letra_n + llave_n) % len(alfabeto)
        elif tipo == "d" or tipo == "D":
            valor = (letra_n - llave_n) % len(alfabeto)
        else:
            return print("No valido")

        resultado += alfabeto[valor]

    return resultado
    