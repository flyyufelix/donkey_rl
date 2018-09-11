import gym
import donkey_gym
import time

NUM_EPISODES = 10
MAX_T = 1000

def simulate(env):

    start = time.time()

    for episode in range(NUM_EPISODES):

        print("Episode: " + str(episode))

        # Reset the environment
        obv = env.reset()

        for t in range(MAX_T):
            # Select an action
            action = select_action(t)

            # execute the action
            obv, reward, done, _ = env.step(action)
            print(obv, reward, done)

            if done:
                print("Time: ", time.time() - start)
                break

def select_action(t):
    #return (0.1, 0.1)
    return (t%10, t%10) # Dummy Actions for testing

if __name__ == "__main__":

    # Initialize the donkey environment
    env = gym.make("donkey-warehouse-v0")
    #env = gym.make("donkey-generated-roads-v0")
    simulate(env)
