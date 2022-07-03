import pandas as pd
import warnings

def unir_arquivo(caminhos):
    final = pd.DataFrame()

    for caminho in caminhos:
        warnings.filterwarnings('ignore')
        df = pd.read_excel(caminho)
        
        final = final.append(df)
    
    return final