import gym
import numpy as np


ActionSpace: gym.Space = gym.spaces.Dict(
    {
        "action_type": gym.spaces.Discrete(5),
        "selected_units": gym.spaces.Discrete(5),
        "target": gym.spaces.MultiDiscrete([2, 3]),
        "queued": gym.spaces.Discrete(2),
        "repeat": gym.spaces.Discrete(3),
        "delay": gym.spaces.Box(low=0.0, high=5.0, shape=(1,), dtype=np.float32),
    }
)
