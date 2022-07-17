from flask import Flask
from controller.reimbursement_controller import rc
from controller.users_contoller import uc
from flask_session import Session
from flask_cors import CORS

if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)  # It instructs our webserver to tell browser that any origin is allowed. By origin, we mean the source
    # where the HTML, CSS and JS are originating from
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    app.register_blueprint(rc)
    app.register_blueprint(uc)

    app.run(port=8080, debug=True)
