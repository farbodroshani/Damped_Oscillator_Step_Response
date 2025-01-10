import numpy as np
import matplotlib.pyplot as plt


def duhamel_integral_step_response(m, zeta, wn, f, t, dt):

    
    # Damped natural frequency
    wd = wn * np.sqrt(1 - zeta**2)
    
    # Impulse response function
    h = np.exp(-zeta * wn * t) * np.sin(wd * t) / (m * wd)
    
    # Convolution using the Duhamel integral
    x = np.convolve(f, h)[:len(t)] * dt

    return x

def main():
    # Parameters
    damping_ratios = [0, 0.02, 0.05, 0.1, 0.2]  # Damping ratios
    wn = float( input("Natural frequency (rad/s):"))* np.pi  # Natural frequency (rad/s)
    m = float(input("Mass (kg):")) # Mass (kg)

    ts = 0.002  # Sampling period (s)
    N = 1000  # Sampling points
    t = np.arange(0, N * ts, ts)  # Time array

    # Ideal step force
    f = np.ones_like(t)*10

    # Plot the force
    plt.figure(1)
    plt.plot(t, f, label='Step Force')
    plt.xlabel('Time (s)')
    plt.ylabel('Force')
    plt.title('Force Definition')
    plt.grid(True)

    plt.figure(2)
    for zeta in damping_ratios:
        # Compute the response
        x = duhamel_integral_step_response(m, zeta, wn, f, t, ts)
        
        # Scaled response (dynamic response factor)
        R = np.abs(x) * wn**2
        
        # Plot the dynamic response factor
        plt.plot(t / (2 * np.pi / wn), R, label=f'ρ={zeta*100:.1f}%')

    plt.xlabel('t / Tn')
    plt.ylabel('R(D)')
    plt.title('Response of SDOF to Ideal Step Force')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
