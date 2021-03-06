import logging
import logging.config
from flask import Flask, Response
from flask import request, jsonify, make_response

from .db_connect import db_session
from .send_request import send_request
from .db_interplay import last_question, add_data


logging.basicConfig(filename="/opt/quiz_app/logs/logger_web.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)


@app.route("/quiz", methods=["POST"])
def read_request():
    resp_question = None

    try:
        resp_question = last_question()
        req_json = request.json
        count = req_json.get("questions_num")
        if count and isinstance(count, int) and count > 0:
            data = send_request(count)
            for item in data:
                add_data(**item)
        else:
            return Response(status=400)

    except Exception as error:
        logging.error(error, exc_info=True)

    if resp_question:
        text = resp_question.question.rstrip()
        return make_response(jsonify(question=text), 200)
    else:
        return make_response(jsonify({}),200)
        

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
