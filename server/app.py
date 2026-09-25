from flask import Flask

app = Flask(__name__)

existing_models = ["Civic", "Model S", "Mustang", "Corolla", "Crossroads"]

@app.route('/')
def index():
    # Default route — confirms the API is running
    return "Welcome to Flatiron Cars"

@app.route('/<model>')
def car_model(model):
    # Checks whether the requested model exists in our fleet
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
