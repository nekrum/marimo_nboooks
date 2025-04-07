import marimo

__generated_with = "0.11.30"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Fundamentos básicos de Python

        ## Tipos de variables en Python

        En python las variables que pueden almacenar diferentes tipos de datos, 
        a diferencia de otros lenguajes con **Python** se encarga de adiviniar el tipo de dato
        automáticamente a partir de la información que guarda.

        ```python3
        variable_string = "Hola Mundo"
        variable_int = 42
        variable_float = 3.14
        variable_list = [1, 2, 3, 4, 5]
        variable_dict = {"key1": "value1", "key2": "value2"}
        variable_bool = True
        variable_none = None
        ```

        Sin embargo si que se puede definir con un **HINT** el tipo de dato de una variable:

        ```python3
        variable_string: str = "Hola Mundo"
        variable_int: int = 42
        variable_float: float = 3.14
        ```
        Aunque en este caso la definición de la variable no es determinante... sirve como una pista (**HINT**) para saber el tipo de variable que se espera

        ```python3
        variable_string: str = 4
        print(variable_string)
        ```

        Puedes revisar el tipo de dato de una variable con

        ```python3
        variable_int: int = 42
        type(variable_int)
        ```

        Define tus propias variables, revisa su tipo y prueba si al definir el **HINT** no se puede asignar otro tipo en la siguiente celda.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Control de flujo (if, for, while)

        Un control de flujo en Python (y en cualquier lenguaje de programación) se refiere a las estructuras que permiten dirigir la ejecución del código dependiendo de condiciones o repeticiones. Sirve para que el programa tome decisiones, repita acciones o se detenga según sea necesario.

        ### Condicionales (if, elif, else)

        Permiten ejecutar ciertas líneas de código solo si se cumple una condición.

        ```python3
        edad = 18
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
        ```

        La condicional `elif` se puede usar para revisar una condicion mas:

        ```python3
        calificacion = 9
        if calificacion == "NP": 
            print("No presento")
        elif calificacion >= 6:
            print('Pasaste!!')
        else:
            print("Reprobaste 😧")
        ```

        Prueba a cambiar calificaciones 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Bucles (for, while)

        Permiten repetir un bloque de código varias veces.

        - for: se usa para iterar sobre secuencias (listas, strings, etc.)

        ```python3
        for i in range(3):
            print("Hola", i)
        ```


        - while: repite mientras una condición sea verdadera.

        ```python3
        contador = 0
        while contador < 3:
            print("Hola", contador)
            contador += 1
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Palabras clave de control

        Estas ayudan a modificar el flujo dentro de bucles o condicionales.
        	•	break: termina un bucle
        	•	continue: salta a la siguiente iteración
        	•	pass: no hace nada, se usa como marcador de posición

        ```python3
        for i in range(5):
            if i == 3:
                break
            print(i)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""
        ## Librerías Clave

        ### NumPy: Álgebra y operaciones numéricas

        ```python3
        import numpy as np

        # Crear datos simulados con distribución normal
        np.random.seed(42)
        x = np.random.normal(loc=5, scale=2, size=100)
        y = 2 * x + np.random.normal(0, 1, 100)
        ```
        {mo.callout("Con este código se **generan variables** que usaras en los siguientes ejemplos, no olvides generarlas antes que el resto", kind="warn")}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### pandas: Manipulación de datos tabulares

        ```python3
        import pandas as pd

        # Organizar los datos en un DataFrame
        df = pd.DataFrame({'x': x, 'y': y})
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Matplotlib y Seaborn: Visualización de datos

        ```python3
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Graficar la relación entre x e y
        sns.scatterplot(data=df, x='x', y='y')
        plt.title("Relación entre x y y")
        plt.show()
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Pingouin: Estadística avanzada amigable con ciencia de datos

        ```python3
        import pingouin as pg

        # Usar Pingouin para análisis de regresión lineal
        regresion = pg.linear_regression(df[['x']], df['y'])
        print(regresion)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### SciPy: Pruebas estadísticas

        ```python3
        from scipy import stats

        # Prueba de correlación de Pearson
        corr, p = stats.pearsonr(df['x'], df['y'])
        print(f"Correlación de Pearson: {corr:.2f}, p-valor: {p:.4f}")
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Statsmodels: Modelado estadístico

        ```python3
        import statsmodels.api as sm

        # Ajustar un modelo de regresión lineal
        X = sm.add_constant(df['x'])  # Agregar constante (intercepto)
        modelo = sm.OLS(df['y'], X).fit()

        # Mostrar resumen del modelo
        print(modelo.summary())
        ```
        """
    )
    return


if __name__ == "__main__":
    app.run()
