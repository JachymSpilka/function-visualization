"""main.py
Vykreslení matematických funkcí pomocí NumPy a Matplotlib.
Ukládá jednotlivé grafy do složky images/ a vytváří i kombinovaný graf.

Pokročilejší část:
  - Možnost A: výběr funkce přes CLI (např. python main.py sin)
  - Možnost C: nalezení maxima/minima a vyznačení v grafu (u sin)
"""

import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

import functions


def ensure_images_dir(path="images"):
    os.makedirs(path, exist_ok=True)
    return path


def x_values(xmin=-10, xmax=10, n=1000):
    return np.linspace(xmin, xmax, n)


def save_single_plot(x, y, title, xlabel, ylabel, label, out_path,
                     mark_extrema=False):
    plt.figure()
    plt.plot(x, y, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if mark_extrema:
        max_i = int(np.argmax(y))
        min_i = int(np.argmin(y))
        plt.scatter([x[max_i]], [y[max_i]], label=f"maximum ({x[max_i]:.2f}, {y[max_i]:.2f})")
        plt.scatter([x[min_i]], [y[min_i]], label=f"minimum ({x[min_i]:.2f}, {y[min_i]:.2f})")

    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def save_multiple_plot(x, series, title, xlabel, ylabel, out_path):
    """series: list of (y, label)"""
    plt.figure()
    for y, label in series:
        plt.plot(x, y, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Vizualizace matematických funkcí pomocí NumPy a Matplotlib"
    )
    parser.add_argument(
        "choice",
        nargs="?",
        default="all",
        choices=["all", "linear", "quadratic", "sin", "cos", "exp", "custom"],
        help="Kterou funkci vykreslit (default: all)"
    )
    parser.add_argument("--xmin", type=float, default=-10.0, help="Spodní mez intervalu (default: -10)")
    parser.add_argument("--xmax", type=float, default=10.0, help="Horní mez intervalu (default: 10)")
    parser.add_argument("--n", type=int, default=1000, help="Počet bodů (default: 1000)")

    args = parser.parse_args()

    images = ensure_images_dir("images")
    x = x_values(args.xmin, args.xmax, args.n)

    # Parametry (jsou proměnné, ne pevně zadané v definici funkcí)
    a_lin, b_lin = 2.0, 1.0
    a_q, b_q, c_q = 1.0, 0.0, -4.0
    k_trig = 1.0
    k_exp = 0.2
    a_custom = 1.5

    # Připravené série
    y_linear = functions.linear(x, a=a_lin, b=b_lin)
    y_quadratic = functions.quadratic(x, a=a_q, b=b_q, c=c_q)
    y_sin = functions.sine(x, k=k_trig)
    y_cos = functions.cosine(x, k=k_trig)
    y_exp = functions.exponential(x, k=k_exp)
    y_custom = functions.custom(x, a=a_custom)

    # Jednotlivé grafy (uložení do images/)
    if args.choice in ("all", "linear"):
        save_single_plot(
            x, y_linear,
            "Lineární funkce",
            "x", "y",
            f"{a_lin}x + {b_lin}",
            os.path.join(images, "linear.png"),
        )

    if args.choice in ("all", "quadratic"):
        save_single_plot(
            x, y_quadratic,
            "Kvadratická funkce",
            "x", "y",
            f"{a_q}x² + {b_q}x + {c_q}",
            os.path.join(images, "quadratic.png"),
        )

    if args.choice in ("all", "sin"):
        # Pokročilejší část (C): max/min v grafu
        save_single_plot(
            x, y_sin,
            "Sinus",
            "x", "y",
            f"sin({k_trig}x)",
            os.path.join(images, "sin.png"),
            mark_extrema=True
        )

    if args.choice in ("all", "cos"):
        save_single_plot(
            x, y_cos,
            "Kosinus",
            "x", "y",
            f"cos({k_trig}x)",
            os.path.join(images, "cos.png"),
        )

    if args.choice in ("all", "exp"):
        save_single_plot(
            x, y_exp,
            "Exponenciální funkce",
            "x", "y",
            f"e^({k_exp}x)",
            os.path.join(images, "exponential.png"),
        )

    if args.choice in ("all", "custom"):
        save_single_plot(
            x, y_custom,
            "Vlastní funkce",
            "x", "y",
            f"x·sin({a_custom}x)",
            os.path.join(images, "custom.png"),
        )

    # Kombinovaný graf (minimálně 3 funkce)
    if args.choice == "all":
        save_multiple_plot(
            x,
            [
                (y_linear, "linear"),
                (y_quadratic, "quadratic"),
                (y_sin, "sin"),
            ],
            "Kombinovaný graf: více funkcí",
            "x", "y",
            os.path.join(images, "multiple_functions.png"),
        )

    print("Hotovo. Grafy najdeš ve složce images/.")


if __name__ == "__main__":
    main()
