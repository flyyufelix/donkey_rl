'''
file: donkey_env.py
author: Tawn Kramer
date: 2018-08-31
'''
from threading import Thread

import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from donkey_gym.envs.donkey_sim import DonkeyUnitySim

class DonkeyEnv(gym.Env):
    """
    Customized OpenAI Gym Environment for Donkey 
    """

    metadata = {
        "render.modes": ["human", "rgb_array"],
    }

    ACTION = ["steer", "throttle"]

    def __init__(self, level, time_step=0.05, frame_skip=2):

        # Start simulation thread
        self.viewer = DonkeyUnitySim(level, time_step)

        # Steering and Throttle
        self.action_space = spaces.Discrete(len(self.ACTION))

        # Camera sensor data
        self.observation_space = spaces.Box(0, 255, self.viewer.get_sensor_size())

        # Frame Skipping
        self.frame_skip = frame_skip

        # Simulation related variables.
        self.seed()

        # Start donkey sim thread communicator (Should be monkey-patched and run on greenlet)
        self.thread = Thread(target=self.viewer.communicator)
        self.thread.start()

        # Launch Unity environment
        file_name = "donkey" # file name to identify Unity application
        headless = False  # Set to True to render Unity environment. False for headless training
        platform = "linux" # linux or darwin (for MaxOS)
        self.viewer.executable_launcher(file_name, headless, platform)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        for i in range(self.frame_skip):
            self.viewer.take_action(action)
            observation, reward, done, info = self.viewer.observe()
        return observation, reward, done, info

    def reset(self):
        self.viewer.reset()
        observation, reward, done, info = self.viewer.observe()
        return observation

    def render(self, mode="human", close=False):
        if close:
            self.viewer.quit()

        return self.viewer.render(mode)

    def is_game_over(self):
        return self.viewer.is_game_over()


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

class GeneratedRoadsEnv(DonkeyEnv):

    def __init__(self):
        super(GeneratedRoadsEnv, self).__init__(level=0)

class WarehouseEnv(DonkeyEnv):

    def __init__(self):
        super(WarehouseEnv, self).__init__(level=1)

class AvcSparkfunEnv(DonkeyEnv):

    def __init__(self):
        super(AvcSparkfunEnv, self).__init__(level=2)
