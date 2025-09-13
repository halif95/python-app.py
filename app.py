from flask import Flask, render_template, request

app = Flask(__name__)

# Данные о комплектующих (в реальном приложении лучше использовать БД)
processors = [
    {"id": 1, "name": "Intel Core i9-13900K", "cores": 24, "threads": 32, "speed": "3.0-5.8 GHz", "price": 58999},
    {"id": 2, "name": "AMD Ryzen 9 7950X", "cores": 16, "threads": 32, "speed": "4.5-5.7 GHz", "price": 54999},
    {"id": 3, "name": "Intel Core i7-13700K", "cores": 16, "threads": 24, "speed": "3.4-5.4 GHz", "price": 42999},
    {"id": 4, "name": "AMD Ryzen 7 7800X3D", "cores": 8, "threads": 16, "speed": "4.2-5.0 GHz", "price": 39999},
    {"id": 5, "name": "Intel Core i5-13600K", "cores": 14, "threads": 20, "speed": "3.5-5.1 GHz", "price": 31999}
]

gpus = [
    {"id": 1, "name": "NVIDIA GeForce RTX 4090", "memory": "24 GB", "speed": "2.52 GHz", "price": 159999},
    {"id": 2, "name": "AMD Radeon RX 7900 XTX", "memory": "24 GB", "speed": "2.3 GHz", "price": 99999},
    {"id": 3, "name": "NVIDIA GeForce RTX 4080", "memory": "16 GB", "speed": "2.51 GHz", "price": 89999},
    {"id": 4, "name": "AMD Radeon RX 7900 XT", "memory": "20 GB", "speed": "2.0 GHz", "price": 79999},
    {"id": 5, "name": "NVIDIA GeForce RTX 4070 Ti", "memory": "12 GB", "speed": "2.61 GHz", "price": 69999}
]

coolers = [
    {"id": 1, "name": "Noctua NH-D15", "type": "Воздушное", "noise": "24.6 dB", "price": 8999},
    {"id": 2, "name": "Corsair iCUE H150i Elite", "type": "Жидкостное", "noise": "10-30 dB", "price": 14999},
    {"id": 3, "name": "be quiet! Dark Rock Pro 4", "type": "Воздушное", "noise": "24.3 dB", "price": 7999},
    {"id": 4, "name": "NZXT Kraken Z73", "type": "Жидкостное", "noise": "21-36 dB", "price": 17999},
    {"id": 5, "name": "Deepcool AK620", "type": "Воздушное", "noise": "28 dB", "price": 4999}
]

cases = [
    {"id": 1, "name": "Lian Li PC-O11 Dynamic", "type": "Mid-Tower", "fans": "3", "price": 12999},
    {"id": 2, "name": "Fractal Design Meshify C", "type": "Mid-Tower", "fans": "2", "price": 8999},
    {"id": 3, "name": "Corsair 4000D Airflow", "type": "Mid-Tower", "fans": "2", "price": 7999},
    {"id": 4, "name": "NZXT H710i", "type": "Mid-Tower", "fans": "4", "price": 14999},
    {"id": 5, "name": "Phanteks Eclipse P500A", "type": "Mid-Tower", "fans": "3", "price": 11999}
]

monitors = [
    {"id": 1, "name": "Samsung Odyssey G9", "size": "49\"", "resolution": "5120x1440", "refresh_rate": "240 Hz", "price": 89999},
    {"id": 2, "name": "LG UltraGear 27GP850", "size": "27\"", "resolution": "2560x1440", "refresh_rate": "180 Hz", "price": 34999},
    {"id": 3, "name": "ASUS ROG Swift PG279Q", "size": "27\"", "resolution": "2560x1440", "refresh_rate": "165 Hz", "price": 59999},
    {"id": 4, "name": "Dell S2721DGF", "size": "27\"", "resolution": "2560x1440", "refresh_rate": "165 Hz", "price": 31999},
    {"id": 5, "name": "Acer Predator X38", "size": "38\"", "resolution": "3840x1600", "refresh_rate": "175 Hz", "price": 99999}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare')
def compare():
    category = request.args.get('category', 'processors')
    components = []
    if category == 'processors':
        components = processors
    elif category == 'gpus':
        components = gpus
    elif category == 'coolers':
        components = coolers
    elif category == 'cases':
        components = cases
    elif category == 'monitors':
        components = monitors
        
    return render_template('compare.html', components=components, category=category)

@app.route('/build')
def build():
    return render_template('build.html', 
                         processors=processors,
                         gpus=gpus,
                         coolers=coolers,
                         cases=cases,
                         monitors=monitors)

@app.route('/components')
def components():
    return render_template('components.html',
                         processors=processors,
                         gpus=gpus,
                         coolers=coolers,
                         cases=cases,
                         monitors=monitors)

if __name__ == '__main__':
    app.run(debug=True)