from typing import Final

# Settings ( You can change the settings if you wish)

SIMULATION_PROTOCOL = 'TOR'  # [TOR, I2P]
MAX_ITERATION_NUMBER: Final[int] = 10
MAX_ROUND_NUMBER: Final[int] = 10

# --------------------------------------------------

# Constants

TEST_ID_NODE_COUNT_MAPPINGS = {'TOR': 4, 'I2P': 5}

MIN_SEED_NODEID: Final[int] = 0
MAX_SEED_NODEID: Final[int] = 99

MIN_COMMUNICATION_INTERVAL_VALUE: Final[int] = 10
MAX_COMMUNICATION_INTERVAL_VALUE: Final[int] = 100

MIN_SEED_LATENCY: Final[int] = 1
MAX_SEED_LATENCY: Final[int] = 100
