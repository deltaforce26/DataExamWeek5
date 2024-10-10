from database.connect import crashes


def get_crashes_by_beat(beat):
    crashes_list = list(crashes.aggregate([
        {"$lookup": {'from': 'beats', 'localField': 'beat_id', 'foreignField': '_id', 'as': 'beat'}},
                       {'$match': {'beat.beat': beat}},
        { "$project": { "_id": 0  ,"beat_id": 0, "beat._id": 0}}
    ]))
    return crashes_list



def get_crashes_by_date(date):
    crashes_list = list(crashes.find({'crash_date': date}))
    return crashes_list



def get_crashes_by_prime_cause(beat):
    crashes_list = list(crashes.aggregate([
        {"$lookup": {'from': 'beats', 'localField': 'beat_id', 'foreignField': '_id', 'as': 'beat'}},
                       {'$match': {'beat.beat': beat}},
        {'$group':{'_id':'$prim_cause', 'count':{'$sum':1}}}
    ]))
    return crashes_list




def get_crash_stats(beat):
    crashes_list = list(crashes.aggregate([
        {"$lookup": {'from': 'beats', 'localField': 'beat_id', 'foreignField': '_id', 'as': 'beat'}},
        {'$match': {'beat.beat': beat}},
        {'$group':{'_id':None,
                   'total_injuries':{'$sum':'$injuries.total_injuries'},
                   'total_fatal_injuries': {'$sum': '$injuries.fatal_injuries'},
                   'total_non_fatal_injuries': {'$sum': {'$subtract': ['$injuries.total_injuries', '$injuries.fatal_injuries']}}}},
        {'$project':{'_id':0}}
    ]))
    return crashes_list






def get_data_type():
    res = list(crashes.aggregate(
        [
            {"$project": {"fieldType": {"$type": "$injuries.total_injuries"}}}
        ]
    ))
    print(res)