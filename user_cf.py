import common
import math
import operator
from collections import defaultdict
import tensorflow as tf

def build_similarity_matrix(data_list):
    # build item-user dict
    item_users = dict()
    for _data in data_list:
        if _data[0] not in item_users:
            item_users[_data[0]] = set()

        item_users[_data[0]].add(_data[1])

    print('build item-user done, size: ' + str(len(item_users)))
    # calculate co-rated items between users
    N = dict()
    C = dict()
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 0

            N[u] += 1
            for v in users:
                if u != v:
                    if u not in C:
                        C[u] = dict()

                    if v not in C[u]:
                        C[u][v] = 0

                    C[u][v] += 1

    print('build N done, size: ' + str(len(N)))
    print('build C done, size: ' + str(len(C)))
    # calculate finally similarity matrix
    W = dict()
    for u, relate_u in C.items():
        for v, cuv in relate_u.items():
            n = math.sqrt(N[u] * N[v])
            if n > 0:
                if u not in W:
                    W[u] = dict()

                if v not in W[u]:
                    W[u][v] = 0

                W[u][v] = cuv / n

    print('build_similarity_matrix W done, size: ' + str(len(W)))
    return W, item_users

def recommand(W, item_users, u):
    num_k = 3
    rank = dict()
    for i, users in item_users.items():
        if u in users:
            continue

        if u not in W:
            continue

        for v, cuv in sorted(W[u].items(), key=operator.itemgetter(1), reverse=True)[:num_k]:
            if i not in rank:
                rank[i] = 0

            rank[i] += cuv

    print('recommand done, size: ' + str(len(rank)))
    return rank


data_list = common.get_data()
print('get_data done 2, size: ' + str(len(data_list)))
w_matrix, iu_matrix = build_similarity_matrix(data_list)
rank_test = recommand(w_matrix, iu_matrix, 2213)
for i, r in sorted(rank_test.items(), key=operator.itemgetter(1), reverse=True)[:10]:
    print('recommand item: ' + str(i) + ', rank: ' + str(r))

