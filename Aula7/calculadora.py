import math
from flask import render_template, request


def calcular():
    try:
        num1_str = request.form.get("num1", "").strip()
        if not num1_str:
            return render_template("calculadora.html",
                                   etapas="Informe o primeiro número.",
                                   resultados="")

        num1 = float(num1_str)
        operacao = request.form["operacao"]

        # ── Raiz quadrada (apenas num1) ──────────────────────────────
        if operacao == "sqrt":
            if num1 < 0:
                etapas = f"Não existe raiz real de {num1}."
                resultados = "Erro: número negativo"
            else:
                resultados = math.sqrt(num1)
                etapas = f"√{num1} = {resultados}"
            return render_template("calculadora.html",
                                   etapas=etapas, resultados=resultados)

        # ── Logaritmo natural (apenas num1) ─────────────────────────
        if operacao == "log":
            if num1 <= 0:
                etapas = f"Logaritmo indefinido para {num1}."
                resultados = "Erro: número deve ser positivo"
            else:
                resultados = math.log(num1)
                etapas = f"ln({num1}) = {resultados}"
            return render_template("calculadora.html",
                                   etapas=etapas, resultados=resultados)

        # ── Operações com dois operandos ─────────────────────────────
        num2_str = request.form.get("num2", "").strip()
        if not num2_str:
            return render_template("calculadora.html",
                                   etapas="Informe o segundo número para esta operação.",
                                   resultados="")

        num2 = float(num2_str)

        if operacao == "+":
            resultados = num1 + num2
            etapas = f"{num1} + {num2} = {resultados}"

        elif operacao == "-":
            resultados = num1 - num2
            etapas = f"{num1} - {num2} = {resultados}"

        elif operacao == "*":
            resultados = num1 * num2
            etapas = f"{num1} × {num2} = {resultados}"

        elif operacao == "/":
            if num2 == 0:
                return render_template("calculadora.html",
                                       etapas=f"{num1} ÷ 0 — divisão por zero é indefinida.",
                                       resultados="Erro: divisão por zero")
            resultados = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultados}"

        elif operacao == "**":
            resultados = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2} = {resultados}"

        else:
            return render_template("calculadora.html",
                                   etapas="Operação inválida.", resultados="")

        return render_template("calculadora.html",
                               etapas=etapas, resultados=resultados)

    except ValueError:
        return render_template("calculadora.html",
                               etapas="Erro: insira apenas números válidos.",
                               resultados="")
