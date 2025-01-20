import pandas as pd
import numpy as np
from typing import Dict, List

class ClimateDataProcessor:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = None
    
    def load_data(self) -> pd.DataFrame:
        """Carrega os dados climáticos do arquivo."""
        self.data = pd.read_csv(self.data_path)
        return self.data
    
    def clean_data(self) -> pd.DataFrame:
        """Limpa e prepara os dados para análise."""
        if self.data is None:
            raise ValueError("Dados não carregados. Execute load_data() primeiro.")
        
        # Remove valores nulos
        self.data = self.data.dropna()
        
        # Converte coluna de data para datetime
        if 'data' in self.data.columns:
            self.data['data'] = pd.to_datetime(self.data['data'])
        
        return self.data
    
    def calculate_statistics(self) -> Dict:
        """Calcula estatísticas básicas dos dados climáticos."""
        if self.data is None:
            raise ValueError("Dados não carregados. Execute load_data() primeiro.")
        
        stats = {
            'temperatura_media': self.data['temperatura'].mean(),
            'temperatura_max': self.data['temperatura'].max(),
            'temperatura_min': self.data['temperatura'].min(),
            'precipitacao_total': self.data['precipitacao'].sum(),
        }
        
        return stats
