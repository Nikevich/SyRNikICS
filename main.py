from flask import Flask, render_template, request, flash, redirect, url_for
from print_parquet import *
from dataset_process import *
from user_grafic import *
import markdown

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

@app.route("/", methods=["GET"])
def index():
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()
        html_content = markdown.markdown(content)
    except FileNotFoundError:
        html_content = "<p style='color: red;'>README.md файл не найден.</p>"
    return render_template("index.html", html_content=html_content)

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

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "GET":
        return render_template("settings.html")
    elif request.method == "POST":
        if request.form.get("renew") == "true":
            if clearDataset():
                if makeUserTraffic():
                    flash("Операция успешно завершена!")
                    return redirect(url_for("settings"))
            else:
                flash("Ошибка при выполнении операций.")
                return redirect(url_for("settings"))
        else:
            flash("Некорректный запрос.")
            return redirect(url_for("settings"))
        
@app.route("/subs", methods=["GET"])
def sub():
    # Путь к каталогу
    directory = "processed/subs"
    
    # Получение списка файлов
    files = [
        {"name": file, "path": os.path.join(directory, file)}
        for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))
    ]

    # Рендер шаблона и передача списка файлов
    return render_template("subs.html", files=files)

@app.route("/plot", methods=["GET"])
def plot():
    graph_url_up = getUpTx(request.args.get('id'))
    graph_url_down = getDownTx(request.args.get('id'))
    # Передаем график на страницу
    return render_template("plot.html", graph_url_up=graph_url_up, graph_url_down=graph_url_down)

if __name__ == "__main__":
    app.run(debug=True)