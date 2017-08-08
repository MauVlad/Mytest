import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
 
COUNT = 100
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim([-1.5, 1.5])
ax.set_xlim(0, COUNT)
xdata = []
ydata = []

def next():
	i = 0
	while i <= COUNT:
		i += 1
		yield i
def update(i):
	xdata.append(i)
	y = np.sin(i / 10.)
	ydata.append(y)
	line.set_data(xdata, ydata)
	return line,

if __name__ == '__main__':
	a = animation.FuncAnimation(fig, update, next, blit = False, interval = 60,repeat = False)

	plt.show ()
#	plt.savefig("seno.jpg")
"""import numpy as np
import matplotlib.pyplot as plt

plt.ion() # decimos de forma explícita que sea interactivo

y = [] # los datos que vamos a dibujar y a actualizar

# el bucle infinito que irá dibujando
while True:
    y.append(np.random.randn(1)) # añadimos un valor aleatorio a la lista 'y'

    # Estas condiciones las he incluido solo para dibujar los últimos 
    # 10 datos de la lista 'y' ya que quiero que en el gráfico se 
    # vea la evolución de los últimos datos
    if len(y) <= 10:
        plt.plot(y)
    else:
        plt.plot(y[-10:])

    plt.pause(0.05) # esto pausará el gráfico
    plt.cla() # esto limpia la información del axis (el área blanca donde
              # se pintan las cosas.
"""

