import csv
from database.connect import crashes, beats
from services.date_service import parse_date


def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def init_crashes_db(file_path):
    if crashes.count_documents() > 0:
        return 'database is already initialized'
    crashes.drop()
    beats.drop()


    for row in read_csv(file_path):
        road = {
            'traffic_way_type': row['TRAFFICWAY_TYPE'],
            'lane_cnt': row['LANE_CNT'],
            'alignment': row['ALIGNMENT'],
            'roadway_surface_cond': row['ROADWAY_SURFACE_COND'],
            'road_defect': row['ROAD_DEFECT'],
        }

        beat = {
            'beat': row['BEAT_OF_OCCURRENCE'],
        }

        beat_id = beats.update_one({'beat': beat }, {"$setOnInsert": beat}, upsert=True).upserted_id()

        injury = {
            'most_severe_injury': row['MOST_SEVERE_INJURY'],
            'total_injuries': row['INJURIES_TOTAL'],
            'fatal_injuries': row['INJURIES_FATAL'],
            'injuries_incapacitating': row['INJURIES_INCAPACITATING'],
            'injuries_non_incapacitating': row['INJURIES_NON_INCAPACITATING'],
        }

        crash = {
            'crash_id': row['CRASH_RECORD_ID'],
            'crash_date': parse_date(row['CRASH_DATE']),
            'road': road,
            'damage': row['DAMAGE'],
            'prim_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
            'sec_cause': row['SEC_CONTRIBUTORY_CAUSE'],
            'beat_id': beat_id,
            'location': row['LOCATION'],
            'injuries': injury,
        }

        crash_id = crashes.insert_one(crash).inserted_id()
    return 'database is initialized'




