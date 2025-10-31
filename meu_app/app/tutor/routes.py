from flask import Blueprint, render_template
from flask_login import login_required

tutor_bp = Blueprint('tutor', __name__, url_prefix='/tutor')

@tutor_bp.route('/meus_animais')
@login_required
def meus_animais():
    return render_template('tutor/meus_animais.html')