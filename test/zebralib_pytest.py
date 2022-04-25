import ZebraLib as zb
from pytest import approx #https://docs.pytest.org/en/6.2.x/reference.html#pytest-approx

classe = zb.Airplane(        
        ano=2021,                    #Ano de fabricação
        name="Zb 2021",              #Nome do avião
        
        #AERODINÂMICA
        b=1.86,                      #Envergadura[m]
        S=0.843,                     #Área da asa [m^2]
        Af=0.601,                    #Afilamento
        CLn=1.080,                   # Coeficiente de sustentação com ângulo de incidencia         
        CLmax=1.5193,                # Coeficiente de sustentação máximo da aeronave, Cl de estol
        c=0.463,                     # *Corda média aerodinamica [m]
        ao=5,                        # *Ângulo de incidência da asa
        a_max=13,                    # *Ângulo mximo da asa (ângulo de estol)
        
        #ESTABILIDADE E CONTROLE
        St=0.2,                      # *Área da do profundor [m^2]
        CLt=1.2,                     # *CL do profundor
        zt=0,                        # *Altura do profundor (tail)
        xt=1.2,                      # *Distância entre o centro aerodinamico do profundor pro CG
        
        #DESEMPENHO
        Tc=(-0.001, -0.225, 35.225), # Coeficientes da curva de tração disponível dinâmica - 2021
        #Tc=(-0.002, -0.208, 37)     # Avião de 2018
        alt_Default=1212,            # Altitude-densidade que esta o avião por padrão 
        rho_ISA=1.14,                # Densidade do ar da international standard atmosphere
        mi=0.038,                    # Coeficiente de atrito com o solo
        Swet=10,  # ~C_D0=0.08       # Área molhada da aeronave
        
        #ESTRUTURAS
        Nmax=2.1,                    # Fator de carga estrutural máximo
        z=0.22,                      # Altura do avião
        mv=2.8,                      # Massa vazia [kg]
        Load=5.5,                    # Carga paga [kg]
        I=1,                         # *Momento de inercia do avião
        xw=0,                        # *Distância do centro aerodinamico em relação ao CG
        xm=0.25,                     # *Distância da bequilha em relação ao CG (centro gravidade)
        xn=0.15,                     # *Distância do trem de pouso em realçao ao CG
        file=None                    #Importar um arquivo por arquivo excel ou pelo ano no histórico da equipe
    )

def test_class_attrs():
    assert classe.S == 1
    assert classe.b == 2

def test_class_methods():
    assert classe.AR == approx(4.0172, rel=1e-2)
    assert classe.W == approx(82.4040, rel=1e-2)