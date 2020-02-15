import matplotlib.pyplot as plt

labels = "Carros", "motos", "onibus", "caminhoes"
tam = [40, 30, 15, 20]

fig1, ax1 = plt.subplots()


ax1.pie(tam, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)


ax1.axis('equal')

plt.show()