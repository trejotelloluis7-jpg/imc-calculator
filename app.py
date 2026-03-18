from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("incex.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    altura = float(request.form.get("altura"))
    peso = float(request.form.get("peso"))

    IMC = peso / (altura ** 2)
    if IMC >= 40:
        resultado = "Tienes obesidad tipo III"
        color = "red"
    elif IMC >= 35:
        resultado = "Tienes obesidad tipo II"
        color = "orange"
    elif IMC >= 30:
        resultado = "Tienes obesidad tipo I"
        color = "orange"
    elif IMC >= 25:
        resultado = "Estas en sobrepeso"
        color = "gold"
    elif IMC >= 22:
        resultado = "Estas en el peso correcto"
        color = "green"
    elif IMC >= 18.5:
        resultado = "Estas en bajo peso"
        color = "blue"
    else:
        resultado = "ESTAS EN DESNUTRICION"
        color = "black"

    return render_template("incex.html", imc=round(IMC, 2), resultado=resultado, color=color)


if __name__ == "__main__":
    app.run(debug=True)
