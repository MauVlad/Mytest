from time import sleep

def cal(importe, descuento):
	return importe - (importe * descuento / 100)

datos = [1500, 10]
print cal(*datos)
sleep(2)

def calcular(importe, descuento):
	return importe - (importe * descuento / 100)

datos = {"descuento": 10, "importe": 1500}
print calcular(**datos)
sleep(2)

