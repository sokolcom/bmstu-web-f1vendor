from flask import Flask, request, send_from_directory, make_response
from flask.json import jsonify
from flask_cors import CORS

from Repository.factory import RepositoryFactory
from Domain.user import User
from Domain.gp import GrandPrix, GrandPrixDomain2DTOConverter
from Domain.ticket import Ticket, TicketDomain2DTOConverter


app = Flask(__name__)
cors = None

repository_factory = None
user_repository = None
gp_repository = None
ticket_repository = None


def send_ok():
    response = {
        "ok": True,
        "status_code": "200",
    }
    return jsonify(response), 200


def send_error(error_code):
    error_message = None
    if error_code == 400:
        error_message = "Invalid request"
    else:
        error_message = "Internal error"

    error = {
        "ok": False,
        "status_code": f"{error_code}",
        "message": error_message,
    }
    return jsonify(error), error_code


@app.route("/")
def hello():
    return make_response(jsonify({ "ok": True, "result": "OH MY LORD MAX, OH MY LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORD!!!!!!!!!!!!!!" }), 200)


@app.route("/api/v1/users", methods=['POST'])
def register_user():
    req = request.json
    if (not req) or ((not "username" in req) or (not "password" in req) or (not "role" in req)):
        return send_error(400)

    users = user_repository.get()
    matches = list(map(lambda x: x.username == req["username"], users))
    if any(matches):
        return send_error(400)

    new_user = User(
        req["username"],
        req["password"],
        req["role"]
    )

    try:
        user_repository.create(new_user)
    except:
        return send_error(500)
    return send_ok()


@app.route("/api/v1/users/login", methods=['POST'])
def login_user():
    req = request.json
    if (not req) or ((not 'username' in req) or (not 'password' in req)):
        return send_error(400)

    username = req["username"]
    password = req["password"]
    users = user_repository.get()
    for user in users:
        if (user.username == username) and (user.password == password):
            return send_ok()

    return send_error(400)

#################################

@app.route("/api/v1/grands-prix", methods=['GET'])
def get_grandsprix():
    gps = gp_repository.get()

    converter = GrandPrixDomain2DTOConverter()
    dto_gps = list(map(lambda x: converter.convert(x).to_dict(), gps))

    return jsonify({ "result": dto_gps, "ok": True }), 200


@app.route("/api/v1/grands-prix", methods=['POST'])
def create_grandprix():
    req = request.json
    if (not req) or (not "title" in req) or (not "date" in req) or (not "vendor_id" in req):
        return send_error(400)

    gps = gp_repository.get()
    matches = list(map(lambda x: x.title == req["title"], gps))
    if any(matches):
        return send_error(400)
    
    new_gp = GrandPrix(
        None,
        req["title"],
        req["date"],
        req["vendor_id"]
    )

    try:
        gp_repository.create(new_gp)
    except:
        return send_error(500)
    return send_ok()


@app.route("/api/v1/grands-prix/<int:gp_id>", methods=['DELETE'])
def delete_grandprix(gp_id):
    try:
        gp_repository.delete(gp_id)
    except:
        return send_error(500)

    return send_ok()

#################################

@app.route("/api/v1/tickets/<int:gp_id>", methods=['GET'])
def get_gp_tickets(gp_id):
    tickets = ticket_repository.get(gp_id)

    converter = TicketDomain2DTOConverter()
    dto_tickets = list(map(lambda x: converter.convert(x).to_dict(), tickets))

    return jsonify({ "result": dto_tickets, "ok": True }), 200


@app.route("/api/v1/tickets", methods=['POST'])
def create_ticket():
    req = request.json
    if (not req) or (not "price" in req) or (not "session" in req) or (not "gp_id" in req):
        return send_error(400)

    new_ticket = Ticket(
        None,
        req["price"],
        req["session"],
        req["gp_id"],
        True
    )

    try:
        ticket_repository.create(new_ticket)
    except:
        return send_error(500)
    
    return send_ok()


@app.route("/api/v1/tickets/<int:ticket_id>", methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        ticket_repository.delete(ticket_id)
    except:
        return send_error(500)

    return send_ok()


@app.route("/api/v1/tickets/buy", methods=['PATCH'])
def buy_ticket():
    req = request.json
    if (not req) or (not "ticket_id" in req):
        return send_error(400)

    ticket_id = req["ticket_id"]
    try:
        in_stock = ticket_repository.get(id=ticket_id)[0].in_stock
        if in_stock:
            ticket_repository.buy(ticket_id)
        else:
            return send_error(400)
    except:
        return send_error(500)

    return send_ok()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({ "result": "404 - not found", "ok": False }), 404)


@app.errorhandler(500)
def server_error():
    return jsonify({ "result": "500 - internal error", "ok": False })


def run_app(args):
    global user_repository, gp_repository, ticket_repository, cors  # I'm sorry

    repository_factory = RepositoryFactory(args.db_port, True if args.readonly == "false" else False)
    user_repository = repository_factory.create_user_repository()
    gp_repository = repository_factory.create_gp_repository()
    ticket_repository = repository_factory.create_ticket_repository()

    cors = CORS(app)
    app.logger.disabled = True
    app.run(debug=True, port=int(args.server_port))
