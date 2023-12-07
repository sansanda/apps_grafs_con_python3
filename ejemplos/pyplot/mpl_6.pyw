import matplotlib.pyplot as plt


def main():
    X = list(range(11))

    Y1 = [x * 75 for x in X]
    Y2 = [x * 58 for x in X]

    plt.subplot2grid((1, 2), (0, 0))
    plt.title("HOMBRES")
    plt.xlabel("Numero de hombres")
    plt.ylabel("Peso acumulado medio")
    plt.ylim(0,800)
    plt.plot(X, Y1)

    plt.subplot2grid((1, 2), (0, 1))
    plt.title("MUJERES")
    plt.xlabel("Numero de mujeres")
    plt.ylabel("Peso acumulado medio")
    plt.ylim(0, 800)
    plt.plot(X, Y2)

    plt.show()


if __name__ == "__main__":
    main()
