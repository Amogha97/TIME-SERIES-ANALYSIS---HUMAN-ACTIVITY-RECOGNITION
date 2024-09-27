class Data:
    BASE_ADDRESS = '/Users/amoghagadde/Desktop/Amogha/Projects/Data_Science/Time_Series/human_activity_recognition/Dataset/'
    DIMENSION = ['_x_', '_y_', '_z_']
    FEATURE_TYPE = ['body_acc', 'body_gyro', 'total_acc']


class Model:
    DROPOUT_RATE = 0.5
    TEST_ITERATIONS = 1
    N_NODES = 150

    N_STEPS = 8
    N_LENGTH = 16
