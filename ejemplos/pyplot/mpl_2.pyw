
import matplotlib.pyplot as plt

def main():
    X = list(range(50))
    print(X)

    Y1 = [1/(x+5) for x in X]
    Y2 = [x**2 for x in X]

    plt.subplot2grid((1,2),(0,0),colspan=1, rowspan=1)
    plt.plot(X,Y1)

    plt.subplot2grid((1, 2), (0, 1), colspan=1, rowspan=1)
    plt.plot(X, Y2)

    plt.show()

if __name__ == "__main__":
    main()