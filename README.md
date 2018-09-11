# Train Donkey Car in Unity Simulator with Reinforcement Learning

[Donkey Car](http://www.donkeycar.com) is an open source DIY self driving platform for small scale RC cars. This repo includes implementation of a **Donkey Car simulator that is reinforcement learning friendly**. You can interact with the Donkey environment using the familiar OpenAI gym like interface. The code was modified from [Tawn Kramer sdsandbox repo](https://github.com/tawnkramer/sdsandbox).

As a simple demo, I've implemented Double Deep Q Learning (DDQN) and used it to train Donkey car to drive itself in the simulator. The below screencast shows the trained Donkey car (after ~100 episodes) in action. 

<img src="/resources/ddqn_demo.gif" width="500">

My goal is to use reinforcement learning to train Donkey Car to compete in a real car race. This involved having the Donkey car trained in simulation first and transfer the learned policy to the real world. 

For more information about this project, please check out my blog post at
https://flyyufelix.github.io/2018/09/11/donkey-rl-simulation.html.

## Usage

### Download Donkey Unity Environment
The Donkey Car simulator is created with Unity. There are 3 Unity scenes available (created by Tawn Kramer) for training now, which are generated roads, warehouse, and Sparkfun AVC. Before we run the RL training script, we have to either build the Donkey Car Unity environment ourselves (need to install Unity) or download the pre-built environment executables below:

Linux: [donkey.x86_64](https://drive.google.com/file/d/1p5Sn27o7YJC2SUBatCfUSlt9t-8xatDw/view?usp=sharing) | MacOS: [donkey.app](https://drive.google.com/drive/folders/1qfFkxlBy-nST3qcJzSQboVpIquzPHmsL?usp=sharing)

Then place the executable inside the `donkey_rl/src` folder. 

Alternatively, if you wish to build the Donkey Unity environment yourself. You need to first download [Unity](https://store.unity.com/). You can find the Donkey Unity project at `donkey_rl/sdsim`. 

Notice that I do have the Windows executable available for download. If you are Windows users, please go ahead and build the environment yourself.

### Train Donkey car with Reinforcement Learning

First, we have to install `donkey_gym` python package, which extends the OpenAI gym class to allow RL developers to interact with Donkey environment using the familiar OpenAI gym like interface. 

To install the package, navigate to `donkey_rl/src/donkey_gym` folder and type the follow command:
```
$ cd donkey_rl/src/donkey_gym
$ pip install -e .
```

After installing `donkey_gym`, we can go ahead to test the environment by running the DDQN script that I've implemented:
```
$ cd donkey_rl/src
$ python ddqn.py
```
If the script runs successfully, you should see some printouts in the command prompt with the training statistics (e.g. episode number, action, reward, etc). 

Notice that by default a Unity GUI will be launched where you can see the Donkey car being trained. If you want to train in headless mode (i.e. no GUI), you can edit `donkey_rl/src/donkey_gym/donkey_gym/envs/donkey_env.py`and set `headless` flag to `True`.

## Dependencies

* [python 3.4+ 64 bit](https://www.python.org/)
* [tensorflow-1+](https://github.com/tensorflow/tensorflow)
* [keras-2+](https://github.com/fchollet/keras)
* [h5py](http://www.h5py.org/)
* [pillow](https://python-pillow.org/)
* [skimage](http://scikit-image.org/docs/dev/install.html)
* [opencv-python](https://pypi.org/project/opencv-python/)
* [python-socketio](https://pypi.python.org/pypi/python-socketio)
* [flask](https://pypi.python.org/pypi/Flask)
* [eventlet](https://pypi.python.org/pypi/eventlet)
* [Unity 5.5+](https://unity3d.com/get-unity/download)

