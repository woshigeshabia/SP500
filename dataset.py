import numpy as np

def make_dataset(data,
                 seq_len=30):

    X=[]
    y=[]

    for i in range(
        len(data)-seq_len-1
    ):

        X.append(
            data[i:i+seq_len]
        )

        y.append(
            data[i+seq_len]
        )

    return (
        np.array(X),
        np.array(y)
    )
