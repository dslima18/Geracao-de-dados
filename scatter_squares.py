import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)
# Define o título do g´rafico e nomeia os eixos 
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square os Value", fontsize=14)
# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()