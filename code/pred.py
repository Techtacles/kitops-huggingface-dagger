import joblib
import pandas as pd

# Load the model
model = joblib.load('models/model.pkl')

# Example input data
input_data = pd.DataFrame({
    'Truck_ID': [0],  # Use the numerical representation of the Truck ID(1,2,3)
    'Kms': [100000],  # Kilometers driven
    'Litros': [150]   # Fuel consumption in liters
})

# Predict fuel burn in kilograms
predicted_fuel_burn = model.predict(input_data)
print(f"Predicted fuel burn: {predicted_fuel_burn[0]:.2f} kg")
