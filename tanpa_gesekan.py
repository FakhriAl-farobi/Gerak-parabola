import math
import matplotlib.pyplot as plt
import numpy as np


# Fungsi untuk melakukan plot data
def graph(x_analytic, y_analytic, x_numeric, y_numeric):
    plt.title('Lintasan Gerakan Parabola (Analitik vs Numerik)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.plot(x_analytic, y_analytic, label="Analitik", linestyle='-', color='blue')
    plt.plot(x_numeric, y_numeric, label="Numerik (Euler)", linestyle='--', color='orange')
    plt.grid()
    plt.legend()
    plt.show()

# Fungsi untuk menghitung solusi analitik
def analytical_solution(v, theta):
    theta = math.radians(theta)
    g = 9.81
    t_total = 2 * v * math.sin(theta) / g  # Total time of flight
    
    # Menggunakan numpy untuk interval waktu
    t_values = np.linspace(0, t_total, num=500)
    
    x_analytic = []
    y_analytic = []
    
    for t in t_values:
        x = v * math.cos(theta) * t
        y = v * math.sin(theta) * t - 0.5 * g * t ** 2
        x_analytic.append(x)
        y_analytic.append(y)
    
    return x_analytic, y_analytic

# Fungsi untuk menghitung solusi numerik
def numerical_solution(v, theta, dt):
    theta = math.radians(theta)
    g = 9.81
    
    x = 0  # posisi awal x
    y = 0  # posisi awal y
    vx = v * math.cos(theta)  # kecepatan awal di sumbu x
    vy = v * math.sin(theta)  # kecepatan awal di sumbu y
    
    x_numeric = [x]
    y_numeric = [y]
    
    while y >= 0:  # loop sampai proyektil menyentuh tanah
        x = x + vx * dt
        vy = vy - g * dt
        y = y + vy * dt
        
        x_numeric.append(x)
        y_numeric.append(y)
    
    return x_numeric, y_numeric

if __name__ == "__main__":
    v = float(input("Masukkan kecepatan awal (m/s): "))
    theta = float(input("Masukkan sudut elevasi (derajat): "))
    dt = float(input("Masukkan interval waktu untuk metode Euler (s): "))
    
    # Penyelesaian Analitik
    x_analytic, y_analytic = analytical_solution(v, theta)
    
    # Penyelesaian Numerik (Euler)
    x_numeric, y_numeric = numerical_solution(v, theta, dt)
    
    # Menampilkan grafik hasil analitik vs numerik
    graph(x_analytic, y_analytic, x_numeric, y_numeric)
