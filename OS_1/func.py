import queue

A = [{"cpu": 20}, {"io": 30}, {"cpu": 10}]
B = [{"cpu": 40}, {"io": 20}, {"cpu": 10}]
C = [{"cpu": 10}, {"io": 30}, {"cpu": 20}]


def get_key(dict_object):
    return list(dict_object.keys())[0]


q = queue.Queue(9)

for i in range(9):
    if get_key(A[0]) == "cpu":
        q.put(A[0])
        del A[0]
        
        continue
