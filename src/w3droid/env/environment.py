"""Module for handling Python Environment definitions based off OpenAPI `gym` and `pysc2`."""

import gym
import numpy as np

from ..spaces import ActionSpace, ObservationSpace


# the following is a purely illustrative proof of concept custom OpenAI gym environment
class BaseEnv(gym.Env):
    """Custom Python RL Environment that follows the OpenAI gym interface.

    See the following for example references:
        - https://stable-baselines.readthedocs.io/en/master/guide/custom_env.html#using-custom-environments
    """

    metadata = {"render.modes": ["human"]}

    def __init__(self, render_mode: str | None = None):
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        self.action_space: gym.spaces.Spaces = ActionSpace
        self.observation_space: gym.spaces.Spaces = ObservationSpace

    def reset(self, seed: int | np.random.Generator | None = None):
        super().reset(seed=seed)  # to seed self.np_random
        # observations = get_observations()
        observations: object = None
        return observations

    def step(self, action) -> tuple[object, float, bool, dict]:
        """Updates the environment according to the action."""
        # placeholder
        observations: object = None
        reward: float = None
        done: bool = None
        info: dict = None
        return observations, reward, done, info
