import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.animation as animation

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

mu, sigma = 0, 1
max_points = 100000

# создаёт кадр в зависимости от момента анимации
def animate(frame):
    n_points = (frame + 1) * 10
    if n_points > max_points:
        n_points = max_points
    
    # Генерация данных
    np.random.seed(42)
    data = np.random.normal(0, 1, n_points)

    ax1.clear()
    ax2.clear()
    
    ax1.hist(data, bins=30, density=True, alpha=0.7, color='lightblue', 
             edgecolor='black', linewidth=0.5)
    
    ax1.plot(np.linspace(-4, 4, 1000), data, 'r-')

    # рисует Гаусса
    ax1.plot(np.linspace(-4, 4, 1000), norm.pdf(np.linspace(-4, 4, 1000), mu, sigma), 'r-', linewidth=2)
    
    ax1.set_title(f'Гистограмма (n = {n_points})')
    ax1.set_xlabel('Значение')
    ax1.set_ylabel('Частота')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    ax2.scatter(range(len(data)), data, s=1, color='blue')
    ax2.set_title(f'Точек (n = {n_points})')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()

anim = animation.FuncAnimation(fig, animate, frames=1000, interval=1, repeat=False)
plt.show()