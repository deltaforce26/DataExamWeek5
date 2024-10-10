import os

from flask import Blueprint, jsonify, current_app

from repository.csv_repository import init_crashes_db

index_bp = Blueprint('index', __name__)


@index_bp.route('/init', methods=['GET'])
def index():
    file_path = os.path.join(current_app.root_path, 'data', 'Traffic_Crashes_-_Crashes - 20k rows.csv')
    res = init_crashes_db(file_path)
    if res:
        return jsonify({'status': 'success', 'message': 'Database initialized successfully.'}), 200
    return jsonify({'status': 'failed', 'message': 'Database already initialized.'}), 400