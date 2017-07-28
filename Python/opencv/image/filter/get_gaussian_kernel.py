#-*- coding:utf-8 -*-
import numpy as np

def get_gaussian_kernel(ksize=3, sigma=1.3):
    ax = np.arange(-ksize // 2 + 1., ksize // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = 0.5 * (1/3.14*sigma*2) * np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)

def main():
    print(get_gaussian_kernel(3, 1.3))
    
if __name__ == "__main__":
    main()
