import numpy as np

class lstm:
    def __init__(self, hidden_size, concat_size):
        self.hidden_size = hidden_size
        self.concat_size = concat_size

        #forget gate
        self.w_f = np.random.randn(hidden_size, concat_size)
        self.b_f = np.zeros((hidden_size, 1))

        #input gate
        self.w_i = np.random.randn(hidden_size, concat_size)
        self.b_i = np.zeros((hidden_size, 1))

        #output gate
        self.w_o = np.random.randn(hidden_size, concat_size)
        self.b_o = np.zeros((hidden_size, 1))

        #cell candidate
        self.w_c = np.random.randn(hidden_size, concat_size)
        self.b_c = np.zeros((hidden_size, 1))
\
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
