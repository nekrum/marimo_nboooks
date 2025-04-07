import marimo

__generated_with = "0.11.30"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from pathlib import Path
    import pandas as pd
    import matplotlib.pyplot as plt
    import altair as alt

    file_path = "screen_time.csv"

    mo.md("# Análisis exploratorio de Datos")
    return Path, alt, file_path, mo, pd, plt


@app.cell(hide_code=True)
def _(Path, file_path, mo, pd):
    if Path("data/screen_time.csv").exists():
        df = pd.read_csv(
            "data/screen_time.csv",
        )
    mo.stop(
        Path("data/screen_time.csv").exists(),
        mo.md(
            f"""
            Cargando datos del archivo: {file_path}

            Si los datos no estan localmente, se descargaran de [Kaggle](https://www.kaggle.com/).
            """
        ),
    )

    import kagglehub
    from kagglehub import KaggleDatasetAdapter

    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "ak0212/average-daily-screen-time-for-children",
        file_path,
    )
    df.to_csv("data/screen_time.csv", index=False)
    return KaggleDatasetAdapter, df, kagglehub


@app.cell(hide_code=True)
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(df, mo):
    with mo.capture_stdout() as out_info:
        mo.as_html(df.info())
    with mo.capture_stdout() as out_types:
        mo.as_html(print(df.dtypes))
    _types = out_types.getvalue()
    _info = out_info.getvalue()
    _desc = df.describe()
    mo.ui.tabs(
        {
            "DF describe": _desc,
            "Tipo de Datos": _types,
            "DF Info": _info,
        }
    )
    return out_info, out_types


@app.cell(hide_code=True)
def _(df, mo):
    mo.ui.dataframe(df)
    return


@app.cell(hide_code=True)
def _(df, mo):
    mo.ui.table(df)
    return


@app.cell(hide_code=True)
def _(df, plt):
    tipos = df["Screen Time Type"].unique()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

    # Generar un histograma por tipo
    for i, tipo in enumerate(tipos):
        subset = df[df["Screen Time Type"] == tipo]
        subset["Average Screen Time (hours)"].hist(ax=axes[i], bins=15)
        axes[i].set_title(tipo)
        axes[i].set_xlabel("Horas")
        axes[i].set_ylabel("Frecuencia")

    plt.tight_layout()
    plt.show()
    return axes, fig, i, subset, tipo, tipos


@app.cell
def _(df):
    df.groupby("Screen Time Type")["Average Screen Time (hours)"].mean()
    return


@app.cell
def _(df):
    df.groupby(["Gender", "Screen Time Type"])["Average Screen Time (hours)"].mean()
    return


@app.cell(hide_code=True)
def _(alt, df, mo):
    def jitter_plot():
        _chart = (
            alt.Chart(df)
            .mark_circle(size=80)
            .encode(
                x="Screen Time Type",
                y="Average Screen Time (hours)",
                xOffset="jitter:Q",
                color="Gender",
            )
            .transform_calculate(jitter="sqrt(-2*log(random()))*cos(2*PI*random())")
        )
        chart = mo.ui.altair_chart(
            _chart, legend_selection=True, label="Average Screen Time"
        )
        return chart


    jitter_plot()
    return (jitter_plot,)


@app.cell(hide_code=True)
def _(alt, df, mo):
    def boxplot_chart():
        _chart = (
            alt.Chart(df)
            .mark_boxplot(size=15)
            .encode(
                x=alt.X("Screen Time Type:N", axis=alt.Axis(title=None)),
                y=alt.Y("Average Screen Time (hours):Q", title="Horas promedio"),
                color=alt.Color("Gender:N", scale=alt.Scale(scheme='category10'), legend=None) 
            )
            .facet(
                column=alt.Column("Gender:N", title=None),
                spacing=30
            )
            .configure_view(
                stroke=None
            )
            .properties(
                title="Distribución de uso de pantalla por género",
                bounds="flush"
            )
        )
        _chart = _chart.resolve_scale(y='shared').configure_axisX(labelAngle=90).properties(width=190)

        chart = mo.ui.altair_chart(
            _chart,
            legend_selection=True,
            label="Distribución de uso de pantalla por género"
        )
        return chart


    boxplot_chart()
    return (boxplot_chart,)


if __name__ == "__main__":
    app.run()
