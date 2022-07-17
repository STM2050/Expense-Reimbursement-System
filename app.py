from flask import Flask
from controller.reimbursement_controller import rc
from controller.users_contoller import uc

if __name__ == "__main__":
    app = Flask(__name__)

    app.register_blueprint(rc)
    app.register_blueprint(uc)

    app.run(port=8080, debug=True)