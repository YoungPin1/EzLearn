import query_db


def load_words(module_id):
    left, learned = [], []
    all_words = query_db.Database().get_all_data_module(module_id)
    for i in all_words:
        if i[4] == 2:
            learned.append(i)
        else:
            left.append(i)
    return all_words, learned, left
