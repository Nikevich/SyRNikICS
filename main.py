from flask import Flask, render_template, request
import pandas as pd
import pyarrow.parquet as pq
from print_parquet import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    records_per_page = 100
    page = request.args.get("page", 1, type=int)
    fil = {"range": page, "records_per_page": records_per_page}
    status, clients, count = getClients(fil)

    total_pages = -(-count // records_per_page)

    return render_template(
        "index.html",
        data=clients.to_dict(orient="records"),
        total_pages=total_pages,
        current_page=page
    )

@app.route("/clients", methods=["GET"])
def clients():
    records_per_page = 100
    page = request.args.get("page", 1, type=int)
    fil = {"range": page, "records_per_page": records_per_page}
    status, clients, count = getClients(fil)

    total_pages = -(-count // records_per_page)

    return render_template(
        "clients.html",
        data=clients.to_dict(orient="records"),
        total_pages=total_pages,
        current_page=page
    )

if __name__ == "__main__":
    app.run(debug=True)