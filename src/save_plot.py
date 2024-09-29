import os
import matplotlib.pyplot as plt

def save_plot(fig, name, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        plt.savefig(os.path.join(save_dir, name+'.png'))
    except Exception as e:
        print(f"Error saving figure: {e}")