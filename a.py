import numpy as np
import pandas as pd
import streamlit as st

jogadores = ['Claudinho', 'Danilo', 'Igor', 'Douglas', 'Emerson', 'Gui', 'Danilo Santista', 'Andrade',
'Renan', 'Caique', 'Kauê', 'João', 'Tom', 'Jé', 'Fernandinho', 'Luiz', 'Elton', 'Tiaguinho', 'Paraíba']

st.header('Futebol de Terça')
    
jogadores_hoje = st.multiselect('Quem ta aqui hoje', options=jogadores)

times = st.radio('Numero de times', [2, 3])
jog_port_time = st.radio('Jogadores por time', [4, 5, 6])

def times_f(jogadores_hoje, times, jog_port_time):
    out = pd.DataFrame(columns=np.arange(1, times+1,1), index=np.arange(1, jog_port_time+1))
    jog_sorteados = []
    while len(jogadores_hoje) > 0:
        i = len(jogadores_hoje)
        jog = np.random.randint(0, i)
        jog_sorteados.append(jogadores_hoje[jog])
        jogadores_hoje = np.delete(jogadores_hoje,jog) 
    for i in range(jog_port_time*times - len(jog_sorteados)):
        jog_sorteados.append('')
    for i in range(times):
        out[i+1] = jog_sorteados[i*jog_port_time:(i+1)*jog_port_time]
    return out


if st.button('Tirar times'):
    out = times_f(jogadores_hoje, times, jog_port_time)
    st.dataframe(out)