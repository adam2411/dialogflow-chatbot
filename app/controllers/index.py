"""
* @author: Aditya Aman (aditya.aman@keito.works)
"""
from flask import Blueprint, request, render_template
import dialogflow
from . import Constants


bp = Blueprint('index', __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    return render_template('index/index.html')
