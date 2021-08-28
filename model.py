import pickle
import numpy as np
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))
data = 550
x = np.array(data)
x = x.reshape((1,-1))
#predict = model.predict([[550]])




def marks_prediction(hrs):
    x_test = np.array(hrs)
    x_test = x_test.astype(np.float64)
    x_test = x_test.reshape((1,-1))

    return model.predict(x_test)