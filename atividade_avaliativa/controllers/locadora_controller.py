from datetime import date

from flask import Blueprint, redirect, render_template, request, url_for

from models import ClienteLocadora, Locacao, Veiculo, db

locadora_bp = Blueprint("locadora", __name__, url_prefix="/locadora")


@locadora_bp.route("/")
def index():
    locacoes = Locacao.listar_com_detalhes()
    return render_template("locadora/lista.html", locacoes=locacoes)


@locadora_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    clientes = ClienteLocadora.listar()
    veiculos = Veiculo.listar()

    if request.method == "POST":
        cliente_id = int(request.form.get("cliente_id", 0))
        veiculo_id = int(request.form.get("veiculo_id", 0))
        data_inicio = date.fromisoformat(request.form.get("data_inicio"))
        data_fim = date.fromisoformat(request.form.get("data_fim"))
        valor_total = float(request.form.get("valor_total", 0))

        locacao = Locacao(
            cliente_id=cliente_id,
            veiculo_id=veiculo_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=valor_total,
        )
        db.session.add(locacao)
        db.session.commit()
        return redirect(url_for("locadora.index"))

    return render_template(
        "locadora/formulario.html",
        clientes=clientes,
        veiculos=veiculos,
    )
