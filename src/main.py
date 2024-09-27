import sys
import os

# The project's root directory - sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.cnn_lstm
import src.lstm


def runner():
    print('LSTM network is running ...')
    src.lstm.run()
    print('LSTM network is finished!')
    print('------------------------------------')
    print('Now, CNN-LSTM network is running ...')
    src.cnn_lstm.run()
    print('CNN-LSTM network is finished!')


if __name__ == '__main__':
    runner()