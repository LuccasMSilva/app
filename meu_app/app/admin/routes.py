from flask import Blueprint, render_template
from flask_login import login_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/relatorios')
@login_required
def relatorios():
    return render_template('admin/relatorios.html')