
SIM_TIME = 3600
X_SIZE = 157
Y_SIZE = 157
GRID_SIZE = X_SIZE * Y_SIZE
MAX_DISTANCE = X_SIZE + Y_SIZE

N_PASSENGERS = 1000
TIME_OUT = 10
MAX_TIME_OUTS = 3

N_TAXI = 40
MAX_PASSENGERS = 4
SHARING_RATE = 0
NODES_LIMIT = 5
N_PUBLIC = round(N_TAXI * SHARING_RATE)
N_PRIVATE = round(N_TAXI * (1 - SHARING_RATE))



DEBUG_ID = 505
DEBUG_COUNT = 0