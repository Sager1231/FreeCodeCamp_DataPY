import numpy as np

def calculate(numbers):
    calculations = {}
    if (len(numbers)) != 9 :
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array([numbers.copy()])
        a = np.reshape(a, (3,3))
    

        b = np.mean(a, axis=0).tolist()
        c = np.var(a, axis=0).tolist()
        d = np.std(a, axis=0).tolist()
        e = np.max(a, axis=0).tolist()
        f = np.min(a, axis=0).tolist()
        g = np.sum(a, axis=0).tolist()
        
        h = np.mean(a, axis=1).tolist()
        i = np.var(a, axis=1).tolist()
        j = np.std(a, axis=1).tolist()
        k = np.max(a, axis=1).tolist()
        l = np.min(a, axis=1).tolist()
        m = np.sum(a, axis=1).tolist()

        n = np.mean(a).tolist()
        o = np.var(a).tolist()
        p = np.std(a).tolist()
        q = np.max(a).tolist()
        r = np.min(a).tolist()
        s = np.sum(a).tolist()

        calculations = {
            'mean': [b, h, n],
            'variance': [c, i, o],
            'standard deviation': [d, j, p],
            'max': [e, k, q],
            'min': [f, l, r],
            'sum': [g, m, s]
        }


    return calculations