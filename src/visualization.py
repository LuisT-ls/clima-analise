import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Dict

class ClimateVisualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def plot_temperature_series(self) -> go.Figure:
        """Cria gráfico de série temporal de temperatura."""
        fig = px.line(
            self.data,
            x='data',
            y='temperatura',
            title='Série Temporal de Temperatura'
        )
        return fig
    
    def plot_precipitation_histogram(self) -> go.Figure:
        """Cria histograma de precipitação."""
        fig = px.histogram(
            self.data,
            x='precipitacao',
            title='Distribuição de Precipitação'
        )
        return fig
    
    def create_dashboard(self) -> None:
        """Cria dashboard interativo com Plotly Dash."""
        # Implementação do dashboard será adicionada aqui
        pass
