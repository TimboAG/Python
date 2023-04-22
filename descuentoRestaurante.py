# un restaurante ofrece un descuento del 10% para consumo de hasta s/ 100.00 y un descuento del 20% para consumos mayores pero menor a 300, y para consumo mayores a 300 el 30% de descuento, para los casos se aplica un impuesto del 19%. Determinar el monto del descuento, el impuesto y el importe apagar 

importe = float(input("Ingrese el monto del consumo: "))
descuento=0
cantidadDescuento=None
if importe > 0:

  if importe <= 100.00 :
   cantidadDescuento= "10%"
   descuento= importe * 0.10
  elif importe >= 200 and importe < 300:
   cantidadDescuento= "20%"
   descuento= importe * 0.20
  else:
     cantidadDescuento= "30%"
     descuento= importe * 0.20

  importeConDescuento=  importe- descuento 
  impuesto= importeConDescuento * 0.19
  total=  importeConDescuento+impuesto
  print("-" * 30)
  print(f"El consumo fue de: ${importe} \nEl descuento es de: {cantidadDescuento} \nEl importe con el descuento es:  ${importeConDescuento}\nImpuesto del 19%: ${impuesto} \nTotal a pagar: ${total} ")
  print("-" * 30)
else:
  print("El importe no puede ser menor o igual a 0")