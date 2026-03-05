# Function Visualization (NumPy + Matplotlib)

Tento projekt vizualizuje vybrané matematické funkce pomocí knihoven **NumPy** a **Matplotlib**.
Program vygeneruje samostatné grafy pro jednotlivé funkce a také kombinovaný graf (minimálně 3 funkce),
vše uložené do složky `images/`.

## Struktura repozitáře

```
function-visualization/
├── main.py
├── functions.py
├── README.md
└── images/
```

## Instalace

```bash
pip install numpy matplotlib
```

## Spuštění

Vykreslení všech grafů:

```bash
python main.py
```

Výběr konkrétní funkce (pokročilejší část – možnost A):

```bash
python main.py sin
python main.py quadratic
python main.py exp
```

Volitelně můžeš změnit interval a počet bodů (experimentování):

```bash
python main.py all --xmin -5 --xmax 5 --n 2000
```

## Jaké funkce program vykresluje

- Lineární funkce: `f(x) = a·x + b`
- Kvadratická funkce: `f(x) = a·x² + b·x + c`
- Sinus: `f(x) = sin(k·x)`
- Kosinus: `f(x) = cos(k·x)`
- Exponenciální funkce: `f(x) = e^(k·x)`
- Vlastní funkce: `f(x) = x·sin(a·x)`

## Výstupy

Vygenerované soubory v `images/`:

- `linear.png`
- `quadratic.png`
- `sin.png` (obsahuje vyznačené maximum a minimum – pokročilejší část, možnost C)
- `cos.png`
- `exponential.png`
- `custom.png`
- `multiple_functions.png` (kombinovaný graf)

## Experimentování (co jsem změnil)

Parametry můžeš snadno měnit:
- interval `--xmin`, `--xmax`
- počet bodů `--n`
- koeficienty funkcí (v `main.py` v sekci „Parametry“)

Příklad: Zmenšením intervalu na `[-5, 5]` a zvýšením `--n` na 2000 dostaneš jemnější průběh a detailnější zobrazení kolem nuly.
