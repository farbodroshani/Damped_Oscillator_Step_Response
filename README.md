# Damped_Oscillator_Step_Response
This repository contains a Python script that uses the Duhamel integral to calculate the step response of a damped harmonic oscillator with different damping ratios. The script allows the user to input system parameters and then computes the response of the system over a specified simulation time.

# Overview
The provided Python script analyzes the step response of a damped harmonic oscillator by:

Calculating the displacement response over time.

Plotting the dynamic response factor for different damping ratios.

# User Guide
1. Initialization and Input Data
Import the necessary libraries: numpy for numerical computations and matplotlib.pyplot for plotting graphs.

2. System Parameters
Input the System Parameters: The script will prompt the user to input the following parameters:

Natural frequency (rad/s)

Mass (kg)

3. Damping Ratios
The script uses a predefined list of damping ratios to analyze the system's response.

4. Ideal Step Force
The script defines an ideal step force, which can be modified as needed.

5. Calculate Damped Natural Frequency
The script calculates the damped natural frequency based on the natural frequency and damping ratio.

6. Impulse Response Function
The script defines the impulse response function for the damped harmonic oscillator.

7. Numerical Integration Using Duhamel Integral
The script uses numerical integration to calculate the step response of the system at each time step using the Duhamel integral.

8. Plot Results
The script plots the following graphs using matplotlib.pyplot:

Force Definition: A plot showing the step force over time.

Response of SDOF to Ideal Step Force: A plot showing the dynamic response factor for different damping ratios over time.

# Example Usage
To run the script, execute it in a Python environment and follow the prompts to input the system parameters. The script will then display the force definition and response plots based on the inputs provided.
