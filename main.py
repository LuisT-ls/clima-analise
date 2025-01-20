from src.data_processing import ClimateDataProcessor
from src.visualization import ClimateVisualizer
from src.prediction import ClimatePrediction

def main():
    # Inicializa o processador de dados
    processor = ClimateDataProcessor('data/climate_data.csv')
    
    # Carrega e limpa os dados
    data = processor.load_data()
    data = processor.clean_data()
    
    # Calcula estatísticas
    stats = processor.calculate_statistics()
    print("Estatísticas climáticas:", stats)
    
    # Cria visualizações
    visualizer = ClimateVisualizer(data)
    temp_fig = visualizer.plot_temperature_series()
    temp_fig.show()
    
    # Inicializa modelo preditivo
    prediction = ClimatePrediction(data)
    prediction.prepare_data()
    prediction.train_model()

if __name__ == "__main__":
    main()