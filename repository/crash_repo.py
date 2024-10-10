from database.connect import crashes


def get_crashes_by_beat(beat):
    crashes_list = list(crashes.aggregate([{"$lookup": {'from': 'beats', 'localField': 'beat_id', 'foreignField': '_id', 'as': 'beat'}},
                       {'$match': {'beat.beat': beat}}, { "$project": { "_id": 0  ,"beat_id": 0, "beat._id": 0}}]))
    return crashes_list



def get_crashes_by_date(date):
    crashes_list = list(crashes.find({'crash_date': date}))
    return crashes_list


def get_crashes_by_prime_cause(beat):
    crashes_list = list(crashes.aggregate([{"$lookup": {'from': 'beats', 'localField': 'beat_id', 'foreignField': '_id', 'as': 'beat'}},
                       {'$match': {'beat.beat': beat}},{'$group':{'_id':'$prim_cause', 'count':{'$sum':1}}}]))
    return crashes_list