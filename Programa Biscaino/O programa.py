#Este projeto visa saber as coordenadas onde o gráfico deixa de ser uma reta
import pandas as pd   
# Criando um objeto da tabela do excel (s) e aderindo as colunas às variáveis ''X'' e ''Y''
s = pd.read_excel('C:/Users/Leonardo/Documents/GitHub/Equipe-Devs/Estruturas/dados.xlsx')
X = (s['Deformação'])
Y = (s['Tensão'])  


''' Comparando os coeficientes angulares dos pontos 
    Sendo: 
    var_reta: A diferença entre o coeficiente angular do ponto n+1 com o ponto n  
    coef_ang: Coeficiente angular das retas de comparação 
    pontos : Os pontos finais e o coeficiente angular final 
    ''' 


var_reta=[0]
coef_ang = [0]   
pontos= []
for n in range(len(s)-1): 
    coef_ang.append(abs((Y[n+1]- Y[0])/(X[n+1]-X[0]))) 
    var_reta.append(coef_ang[n+1]-coef_ang[n])   
    if var_reta[n+1]>0.1*var_reta[n]: 
        break  

print(coef_ang)