import gym
import numpy as np

# the following is a purely illustrative proof of concept observation space
ObservationSpace: gym.Space = gym.spaces.Dict(
    {
        "entities": gym.spaces.Dict(
            {
                "unit_type": gym.spaces.Discrete(5),
                "owner": gym.spaces.Discrete(5),
                "status": gym.spaces.Discrete(5),
            }
        ),
        "map": gym.spaces.Dict(
            {
                "height": gym.spaces.Discrete(5),
                "visibility": gym.spaces.Discrete(5),
            }
        ),
        "player": gym.spaces.Dict(
            {
                "race": gym.spaces.MultiDiscrete([3, 3]),  # random?
                "upgrades": gym.spaces.Discrete(5),
            }
        ),
        "game": gym.spaces.Dict(
            {
                "camera": gym.spaces.MultiDiscrete([32, 20]),
                "time": gym.spaces.Box(
                    low=0.0, high=9999.99, shape=(1,), dtype=np.float32
                ),
            }
        ),
    }
)
