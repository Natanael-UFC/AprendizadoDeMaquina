import numpy as np

def split_train_test(n_elem, perc_train, seed):
    vector_train = []
    vector_test = []
    vector = [i for i in range(n_elem)]
    np.random.seed(seed)
    np.random.shuffle(vector)
    calc = n_elem * perc_train
    for i in range(int(calc)):
        vector_train.append(vector[i])
    for i in range(int(calc), n_elem):
        vector_test.append(vector[i])
    return vector_train, vector_test
                   