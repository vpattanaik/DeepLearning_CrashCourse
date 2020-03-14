# :question:Read Me:exclamation:

Please read through this file! The file contains the list of software packages (and guides on how to install) which would used during the (IS Group) Deep Learning Crash Course.

## Required Software Packages

* [Anaconda](#Anaconda)
    * [Python](#Python) 3.x
    * [Conda](#Conda)
    * [Tensorflow](#Tensorflow) > 1.10
    * [Keras](#Keras)
    * [Jupyter](#Jupyter) Lab & Notebook

    * [MatplotLib](#MatplotLib)
    * [OpenCV](#OpenCV)
    * [Pillow](#Pillow)

    * [Pandas](#Pandas)
    * [NumPy](#NumPy)
    * [scikit-learn](#scikit-learn) (or, sklearn)
    * [tqdm](#tqdm)
    * [Wheel](#Wheel)


* [Pycharm IDE](#Pycharm-IDE)

*If you have an Nvidia GPU, you can also [install](https://towardsdatascience.com/setup-an-environment-for-machine-learning-and-deep-learning-with-anaconda-in-windows-5d7134a3db10):*

> For now, its okay to SKIP these!

* NVIDIA GPU Driver 4xx.x
* CUDA 10.0
* cuDNN

---
---

## How to Install

### Anaconda

Download and install Anaconda (for Python 3.x [here](https://www.anaconda.com/distribution/#download-section)).

Right before the Anaconda installation is complete, you will be prompted to download `PyCharm for Anaconda`; so go ahead and download that. Here's the [link](https://www.jetbrains.com/pycharm/promo/anaconda/), just in case.

* Update Anaconda

Open Anaconda Prompt to type the following command(s):

~~~
conda update conda
conda update --all
~~~

> You can find the **Anaconda Prompt** in the start menu (in Windows) or in the `Environments` tab in the Anaconda.

* Create an Anaconda Environment

Open the Anaconda Prompt and type the following command to create a new anaconda environment:

~~~
conda create -n deeplearning pip python=3.6
~~~

* Activating Anaconda Environment

> If you are prompted to install NEW packages, type `y` and press Enter.

Then type the following command to activate the new environment:

~~~
activate deeplearning
~~~

> Doing so would change the Anaconda environment from **(base)** to **(deeplearning)**.

* [Getting Started with Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)


To update conda to the current version:

~~~
conda update conda
~~~

To see a list of all your environments:

~~~
conda info --envs
~~~

To check the list of installed program is in this environment:

~~~
conda list
~~~

---

### Python

> To check the Python version type this command in the Anaconda Prompt.

~~~
python --version
~~~

We choose Python 3.6, as Keras is compatible with Python 2.7 and 3.6.

* Installing Packages

You can use either **conda** or **pip** for installing packages in an virtual environment created with conda. They are both open source package managers. For now we will use **conda**.

### Conda

[Conda](https://docs.conda.io/en/latest/) is an open source package management system and environment management system that runs on Windows, macOS and Linux. It is a cross platform package and environment manager that installs and manages conda packages from the Anaconda repository as well as from the Anaconda Cloud.

`pip` on the other hand is the [package installer](https://packaging.python.org/guides/tool-recommendations/) for Python. You can either use conda or pip or other indexes to install packages into your Anaconda environment.

To install/upgrade `pip`, type this in the Anaconda Prompt:

~~~
conda install --upgrade pip
~~~

### Tensorflow

To install/upgrade Tensorflow, type this in the Anaconda Prompt:

~~~
conda install -c conda-forge tensorflow
~~~

> [conda-forge](https://anaconda.org/conda-forge/tensorflow)

### Keras

> Please make sure you have installed Tensorflow, before you do this step.

To install/upgrade Tensorflow, type this in the Anaconda Prompt:

~~~
conda install keras
~~~

> The [conda-forge](https://anaconda.org/conda-forge/keras) version of Keras gives **VS140COMNTOOLS** `WARNING`, so we opt for the default channel.

### Jupyter

To install Jupyter Lab & Notebook, open the Anaconda Navigator. Click on the environments dropdown menu (that says `Applications on`). Select *deeplearning*. Wait until all packages are loaded (watch the progress bar on the bottom right). Click on the `Install` button under JupyterLab. Once Jupyter Lab & Notebook are installed, `Install` buttons will get replaced by `Launch` buttons.

* Check Tensorflow Installation

`Launch` Jupyter Lab. This should open Jupyter Lab in your default browser. The URL being, *http://localhost:8889/lab*.

Now click on the `Python3` button under `Console`.

Type the following commands in the box [ ] at the bottom of the browser screen.

~~~
import tensorflow as tf
print ("TensorFlow version: " + tf.__version__)
~~~

Press **Shift + Enter**.

This should print the following:

~~~
TensorFlow version: 2.1.0
~~~

### **Install the remaining packages by typing the following commands in the Anaconda Prompt:**

### MatplotLib

~~~
conda install -c conda-forge matplotlib
~~~

> [conda-forge](https://anaconda.org/conda-forge/matplotlib)

### OpenCV

~~~
conda install -c conda-forge opencv
~~~

> [conda-forge](https://anaconda.org/conda-forge/opencv)

### Pillow

~~~
conda install -c conda-forge pillow
~~~

> [conda-forge](https://anaconda.org/conda-forge/pillow)

### **Some more packages we might have to install:**

### Pandas

~~~
conda install -c conda-forge pandas
~~~
> [conda-forge](https://anaconda.org/conda-forge/pandas)


### NumPy

~~~
conda install -c conda-forge numpy
~~~

> [conda-forge](https://anaconda.org/conda-forge/numpy)

### scikit-learn

~~~
conda install -c conda-forge scikit-learn
~~~

> [conda-forge](https://anaconda.org/conda-forge/scikit-learn)

### tqdm

~~~
conda install -c conda-forge tqdm
~~~

> [conda-forge](https://anaconda.org/conda-forge/tqdm)

### Wheel

~~~
conda install -c conda-forge wheel
~~~

> [conda-forge](https://anaconda.org/conda-forge/wheel)

---

### Pycharm IDE

Make sure you [download](https://www.jetbrains.com/pycharm/promo/anaconda/) the PyCharm for Anaconda **Community Edition** i.e., the free version.

Once the download is complete, simply run the installer and follow the wizard steps.

* Setup Anaconda Virtual Environment

Select a folder where you would like to save your PyCharm projects. Create a new file named `demo.py` in the folder. Type the following code in the python file and save.

~~~
import tensorflow as tf
print(tf.__version__)
print("Hello World!")
~~~

Now open PyCharm. Click on the `Open` button (under `Create New Project`). And open the project folder you created in the previous step.

Now, goto `File` > `Settings` > `Project` > `Project Interpreter`.

In the dropdown menu beside `Project Interpreter` you will find an option `Show All...`. Click on button and a new window will popup.

On the right side of said window, you will find a **+** symbol. Click on the + and a new window `Add Python Interpreter` will popup.

Select `Conda Environment` > `Existing environment`. Now, click on the `...` button beside the Interpreter dropdown.

Goto the *folder where you installed Anaconda* -> `envs` -> `deeplearning`. Select `python.exe` and click OK.

Check (tick) the `Make available to all projects` and click `OK`, `OK` and `OK`.
You should be back to your `demo.py` file. At the top-right corner, you will find a green play button. Click on that, and the program should print the following.

> `...\envs\deeplearning\python.exe E:/DevProjects/PycharmProjects/FirstDemo/demo.py`

> 2020-03-10 10:04:59.599689: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found

> 2020-03-10 10:04:59.599896: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.

> `2.1.0`

> `Hello World!`

> `Process finished with exit code 0`

**PyCharm is now setup with Anaconda Environment.**

* Set Default Interpreter (for future projects)

Launch PyCharm. If you redirected directly to a project folder, goto `File` and click `Close Project`.

You should see the welcome screen titled `Welcome to PyCharm`. Go to the lower right of the window and select `Configure` -> `Settings` -> `Project Interpreter`.

In the dropdown menu beside `Project Interpreter`, select `Python 3.6. (deeplearning)` and click `Apply`. Click `OK` to return to the welcome screen.

---
---

# Course Syllabus

* Introduction to Neural Networks
    * ML vs. AI
    * What are NNs?
        * Inputs / Outputs
        * Weights & Biases
        * Transfer Functions
        * Activation Functions
    * How does NNs work?
    * What are Deep NNs?

> *Some insights into data preparation*

* Introduction to Keras
    * Pima Indians Diabetes Demo
    * MNIST Demo

* Introduction to CNNs
    * Processing for CNNs
    > KerasExample (VGGNet)
    * Yolo Demo

* Introduction to RNNs/LSTMs
    > Image Caption Generation Demo
    * Developing LSTMs in Keras

