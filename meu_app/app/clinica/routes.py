from flask import Blueprint, render_template
from flask_login import login_required

clinica_bp = Blueprint('clinica', __name__, url_prefix='/clinica')

@clinica_bp.route('/')
@login_required
def painel():
    return render_template('clinica/painel.html')

@clinica_bp.route('/animais')
@login_required
def animais():
    return render_template('clinica/animais.html')