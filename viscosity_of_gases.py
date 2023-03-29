# exercise 6.8

#load viscosity_of_gases.dat into a nested list
mu_data = {
    'air': {'C': 120,
        'T_0': 291.15,
        'mu_0': 18.27},
    'nitrogen': {'C': 111,
        'T_0': 300.55,
        'mu_0': 17.81},
    'oxygen': {'C': 127,
        'T_0': 292.25,
        'mu_0': 20.18},
    'carbon dioxide': {'C': 240,
        'T_0': 293.15,
        'mu_0': 14.8},
    'carbon monoxide': {'C': 118,
        'T_0': 288.15,
        'mu_0': 17.2},
    'hydrogen': {'C': 72,
        'T_0': 293.85,
        'mu_0': 8.76},
    'ammonia': {'C': 370,
        'T_0': 293.15,
        'mu_0': 9.82},
    'sulphur dioxide': {'C': 416,
        'T_0': 293.65,
        'mu_0': 12.54}
          }

#make a function mu(T, gas, mu_data)
def mu(T, gas, mu_data):
    """
# Computes the viscosity of a gas at a given temperature using the data provided.
    
# Parameters:
        T (float): Temperature in Kelvin
        gas (str): Name of the gas to compute viscosity for
        data (dict): Dictionary containing viscosity constants for different gases
    
# Returns:
        float: Viscosity of the gas at the given temperature
    """
    C = mu_data[gas]['C']
    T_0 = mu_data[gas]['T_0']
    mu_0 = mu_data[gas]['mu_0']
    
    return mu_0 * (T_0 + C) / (T + C) * (T/T_0)**1.5


 
# plot μ(T) for air, carbon dioxide, and hydrogen with T ∈ [223, 373]
import matplotlib.pyplot as plt
import numpy as np

# Define the range of temperatures to plot
T_range = np.linspace(223, 373, 100)

# Define the gases to plot
gases = ['air', 'carbon dioxide', 'hydrogen']

# Create a plot for each gas
for gas in gases:
    # Compute the viscosity for the given range of temperatures
    mu_vals = [mu(T, gas, data) for T in T_range]
    
    # Plot the viscosity as a function of temperature
    plt.plot(T_range, mu_vals, label=gas)

# Set the plot title, axis labels, and legend
plt.title('Viscosity of Different Gases')
plt.xlabel('Temperature (K)')
plt.ylabel('Viscosity (Pa s)')
plt.legend()

# Show the plot
plt.show()
