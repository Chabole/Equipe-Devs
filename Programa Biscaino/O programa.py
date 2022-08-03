#Este projeto visa saber as coordenadas onde o gráfico deixa de ser uma reta
import pandas as pd  
import numpy as np   
# Criando um objeto da tabela do excel (s) e aderindo as colunas às variáveis ''X'' e ''Y''
s = pd.read_excel('C:/Users/Leonardo/Documents/GitHub/Equipe-Devs/Estruturas/dados.xlsx')
X = (s['Deformação'])
Y = (s['Tensão'])  
X_log = []
Y_log = []
''' Comparando os coeficientes angulares dos pontos 
    Sendo: 
    var_reta: A diferença entre o coeficiente angular do ponto n+1 com o ponto n  
    coef_ang: Coeficiente angular das retas de comparação 
    pontos : Os pontos finais e o coeficiente angular final 
    '''  

var_reta= [0]
coef_ang = [0]   
pontos= []   
tangente = []
n = 0 
for n in range(801):  
    z = abs((Y[n+19]-Y[5])/(np.log(X[n+19])- (np.log(X[5]))))
    coef_ang.append(z) 
    var_reta.append(coef_ang[n+1]-coef_ang[n])     
    if var_reta[n+1] <= 0.1*var_reta[n]:  
        pontos.append(X[n]) 
        pontos.append(Y[n])
        tangente.append(var_reta[n+1]) 
print(len(tangente)) 
print(pontos)