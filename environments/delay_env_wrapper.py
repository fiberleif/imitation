# Delay reward wrapper for dense mujoco environment.


class DelayRewardWrapper():
    def __init__(self, env, reward_freq, max_path_length):
        self._wrapped_env = env
        self._reward_freq = reward_freq
        self._max_path_length = max_path_length
        self._current_step = 0
        self._delay_step = 0
        self._delay_r_ex = 0.0

    def reset(self):
        obs = self._wrapped_env.reset()
        self._current_step = 0
        self._delay_step = 0
        self._delay_r_ex = 0.0
        return obs

    def step(self, action):
        next_obs, reward, done, info = self._wrapped_env.step(action)
        self._current_step += 1
        self._delay_r_ex += reward
        if done or self._current_step >= self._max_path_length or self._delay_step == self._reward_freq:
            delay_reward = self._delay_r_ex
            self._delay_step = 0
            self._delay_r_ex = 0.0
        else:
            delay_reward = 0.0
            self._delay_step += 1
        return next_obs, delay_reward, done, info




