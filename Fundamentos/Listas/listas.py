#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

# print(planetas[-4])
# print(planetas[2: ])
# print(len(planetas))

#TRABAJAR CON UNA LISTA DE NUMEROS
gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 123054 #Newtons

print(f"En la Tierra, un autobus de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas[0]} N")

print(f"Lo mas Liviano que seria un autobus en el sistmeta solar es {peso_bus * min(gravedad_en_planetas)} N")
print(f"Lo mas pesado que seria un autosbus en el sistema solar es  {peso_bus * max(gravedad_en_planetas)} N")