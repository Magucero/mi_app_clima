@app.route("/clima")
def clima():
    return render_template(
        "clima.html"
    )

@app.route("/users")
def users():
    cant = request.args.get('cantidad','5',int)
    response = requests.get(f"https://randomuser.me/api/?results={cant}")
    data = response.json()
    usersList = data.get('results')
    print(usersList)
    return render_template(
        "users.html",
        listadoUsuarios = usersList
    )