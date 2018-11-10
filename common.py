import pandas

def get_data():
    # load data from csv
    data_file = 'F:\\work\\ML\\ml-20m\\ratings.csv'
    # data_file = 'F:\\work\\ML\\ml-20m\\yzc_test.csv'
    csv = pandas.read_csv(data_file).sample(frac=0.1).values
    data_list = list()
    for row in csv:
        user_id, item_id = row[0], row[1]
        data_list.append((user_id, item_id))

    print('get_data done, size: ' + str(len(data_list)))
    return data_list