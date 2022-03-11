import matplotlib.pyplot as plt
import numpy as np

ITERATION_COUNT = 25
N = 100

def mandelbrotCount(z):
  # let z be a complex number

  c = z

  for i in range(ITERATION_COUNT):
    # If the complex number multiplied by its complex conjugate
    # is greater than 4, that means that z is greater than 2
    # Which means it's no longer part of the circle
    if (z * z.conjugate()).real >= 4:
      return 255 - i

    z = z * z + c
  
  return 0
  
def main():
  mx = 2.48 / (N - 1)
  my = 2.26 / (N - 1)

  mapper = lambda x, y: complex(mx * x - 2, my * y - 1.13)
  img = np.full(tuple(N for _ in range(2)), 255)

  for y in range(N):
    for x in range(N):
      img[x][y] = mandelbrotCount(mapper(y, x))
  
  plt.imshow(img, cmap='plasma')
  plt.axis('off')
  plt.show()

if __name__ == '__main__':
  main()