import random
print("______________________________________")
destino = input("     Bienevenido a KrakeTraveles \n Escriba su destino: \n ")
velocidad_aleatoria = random.randint(1,120)

#Velocidad
zonaUrbanaMax = 0
zonaUrbanaMin = 0
zonaRuralMax = 0
zonaRuralMin = 0
zonaPerimetralMax = 0
zonaPerimetralMin = 0

if destino == "Ecuador" or destino == "Colombia" or destino == "Peru":
    print("______________________________________")
    print(f"        Usted esta en {destino}") 
    zona = input("   Indique en que zona se encuentra \n Recuerde que las zonas son \n Urbana \n Rural \n Perimetral \n : ")
    if destino == "Ecuador":
        print("______________________________________")
        print("La velocidad permitida en zona urbana \n MIN: 10km/h \n MAX: 50km/h")
        zonaUrbanaMin = 10
        zonaUrbanaMax = 50
        print("La velocidad permitida en zona rural \n MIN: 51km/h \n MAX: 70km/h")
        zonaRuralMin = 51
        zonaRuralMax = 70
        print("La velocidad permitida en zona perimetral \n MIN: 71km/h \n MAX: 90km/h")
        zonaPerimetralMin =71
        zonaPerimetralMax = 90
    elif destino == "Colombia":
        print("______________________________________")
        print("La velocidad permitida en zona urbana \n MIN: 10km/h \n MAX: 30km/h")
        zonaUrbanaMin = 10
        zonaUrbanaMax = 30
        print("La velocidad permitida en zona rural \n MIN: 31km/h \n MAX: 80km/h")
        zonaRuralMin = 31
        zonaRuralMax = 80
        print("La velocidad permitida en zona perimetral \n MIN: 81km/h \n MAX: 100km/h")
        zonaPerimetralMin =81
        zonaPerimetralMax = 100
    elif destino == "Peru":
        print("______________________________________")
        print("La velocidad permitida en zona urbana \n MIN: 10km/h \n MAX: 40km/h")
        zonaUrbanaMin = 10
        zonaUrbanaMax = 40
        print("La velocidad permitida en zona rural \n MIN: 41km/h \n MAX: 60km/h")
        zonaRuralMin = 41
        zonaRuralMax = 60
        print("La velocidad permitida en zona perimetral \n MIN: 61km/h \n MAX: 120km/h")
        zonaPerimetralMin =61
        zonaPerimetralMax = 120    
    if zona == "Urbana":
        print("______________________________________")
        print("             ZONA URBANA")
        if velocidad_aleatoria < zonaUrbanaMin:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos subir la velocidad \n")
        elif velocidad_aleatoria >= zonaUrbanaMin and velocidad_aleatoria <= zonaUrbanaMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Una excelente velocidad \n")
        elif velocidad_aleatoria > zonaUrbanaMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos bajar la velocidad \n a una adecuada \n")
    elif zona == "Rural":
        print("______________________________________")
        print("              ZONA RURAL")
        if velocidad_aleatoria < zonaRuralMin:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos subir la velocidad \n")
        elif velocidad_aleatoria >= zonaRuralMin and velocidad_aleatoria <= zonaRuralMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Una excelente velocidad \n")
        elif velocidad_aleatoria > zonaRuralMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos bajar la velocidad \n a una adecuada \n")
    elif zona == "Perimetral":
        print("______________________________________")
        print("           ZONA PERIMETRAL")
        if velocidad_aleatoria < zonaPerimetralMin:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos subir la velocidad \n")
        elif velocidad_aleatoria >= zonaPerimetralMin and velocidad_aleatoria <= zonaPerimetralMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Una velocidad adecuada \n")
        elif velocidad_aleatoria > zonaPerimetralMax:
            print(f"El conductor va a {velocidad_aleatoria}km/h \n Le recomendamos bajar la velocidad \n a una adecuada \n")
    else:
        print("Recuerde que las zonas son \n Urbana \n Rural \n Perimetral")
else:
    print("Lo sentimos, nuestros destinos solo son Ecuador, Peru y Colombia")