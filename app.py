from application import app



if __name__ == "__main__":
    app.run(debug=True, port=4006)

    # MVC - MODULE VIEW CONTROLLER
    # Separation of concerns
    # Templates - Visual, presentation, UI (User interface):VIEWS
    # routes.py - Controller, control the flow of logics
    # Model: data, CRUD: Create Read Update Delete