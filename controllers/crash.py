from flask import Blueprint, jsonify
from repository.crash_repo import get_crashes_by_beat, get_crashes_by_prime_cause, get_crash_stats, get_data_type
from services.date_service import convert_time_span, convert_time

crash_bp = Blueprint('crash_bp', __name__)




@crash_bp.route('/crashes/<string:beat>', methods=['GET'])
def crashes_by_beat(beat):
    crashes = get_crashes_by_beat(beat)
    if not crashes:
        return jsonify({'message': 'No crashes found'}), 404
    return jsonify({'crashes': crashes}), 200




@crash_bp.route('/crashes/<string:beat>/<string:date>/<string:time_span>', methods=['GET'])
def crashes_by_date(beat, date, time_span):
    date = convert_time(date)
    res = convert_time_span(date, time_span)
    if not res:
        return jsonify({'message': 'Invalid time span'}), 404
    crashes = get_crashes_by_beat(beat)
    filtered_crashes = list(filter(lambda crash: date < crash['crash_date'] < res, crashes))
    return jsonify({'crashes': filtered_crashes}), 200



@crash_bp.route('/crashes/cause/<string:beat>', methods=['GET'])
def crashes_by_prime_cause(beat):
    crashes = get_crashes_by_prime_cause(beat)
    if not crashes:
        return jsonify({'message': 'No crashes found'}), 404
    return jsonify({'crashes': crashes}), 200



@crash_bp.route('/crashes/stats/<string:beat>', methods=['GET'])
def crashes_stats(beat):
    crashes = get_crash_stats(beat)
    if not crashes:
        return jsonify({'message': 'No crashes found'}), 404
    return jsonify({'stats': crashes}), 200





