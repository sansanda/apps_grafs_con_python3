import matplotlib.pyplot as plt


def main():
    X = list(range(50))
    print(X)

    Y1 = [x ** 0.5 for x in X]
    Y2 = [x ** 1 for x in X]
    Y3 = [x ** 1.5 for x in X]
    Y4 = [x ** 2 for x in X]

    plt.suptitle("Ejemplo de funciones simultaneas", fontsize=24)

    plt.subplot2grid((2, 2), (0, 0), colspan=2, rowspan=1)
    plt.title("Cuatro funciones representadas simultaneamente", fontsize=10)
    plt.plot(X, Y1, X, Y2, X, Y3, X, Y4)

    plt.subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
    plt.title("Dos funciones representadas simultaneamente", fontsize=10)
    plt.plot(X, Y1, X, Y2)

    plt.show()


if __name__ == "__main__":
    main()
