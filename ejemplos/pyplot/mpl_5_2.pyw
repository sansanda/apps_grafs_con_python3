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
    plt.grid(True, ls="-", color="0.5")
    plt.text(4.2, 30, "y = x ** 2")

    plt.subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
    plt.title("Dos funciones representadas simultaneamente", fontsize=10)
    plt.plot(X, Y1, label="Curva 1")
    plt.plot(X, Y2, label="Curva 2")
    plt.grid()
    plt.legend()
    plt.annotate("y = x", xytext=(1.5, 7), xy=(5.5, 5.6), ha="right", va = "bottom",
                 arrowprops={'facecolor':"blue", "shrink":0.02})
    plt.annotate("y = x ** 0.5", xytext=(7, 5), xy=(6, 2.6), ha="center", va="center",
                 arrowprops={'arrowstyle': "->", "color": "red"})
    plt.show()


if __name__ == "__main__":
    main()
