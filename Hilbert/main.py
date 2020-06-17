import numpy as np
import hilbert as hil
import image as ima

def main():
    order = 3
    hilbertMatrix = hil.hilbertCurve(order)
    directionMatrix = hil.directionCurve(order)

    rank = (2**order)**2
    x = (2**order)-1
    y = 0
    im = ima.scaleForRank(rank)
    hilbertTransformed = hil.hilbertTransform(im, directionMatrix, rank, x, y)
    
    print(hilbertTransformed)

    def normalizeRows(x: np.ndarray):
        return x/np.linalg.norm(x, ord=2, axis=0, keepdims=True)

    norm = normalizeRows(hilbertTransformed)
    normMax = np.amax(norm)
    normalized = norm * (1/normMax)


if __name__ == "__main__":
    main()
