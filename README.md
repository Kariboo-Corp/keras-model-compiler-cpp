# How to use

To use this model converter you should have a .h5 keras model (trained) and a C++ compiler active (g++ > 8, make > 4.2, pip > 20.0 & python > 3.6).
If these prerequisite are fulfill run these commands :

`git clone https://gitlab.com/eg-julien/keras-model-compiler-cpp.git`

`cd keras-model-compiler-cpp`

`pip install requirements.txt`

Change the content of the variable `model_name` to fulfill your requirements and then run :

`python3 converter_keras.py`

`converter_keras.py` is used to create a .tflite model from a .h5 keras model. It's also create a .h cpp library with model coefficient.

# Inference the tflite model

First of all you'll need to clone and compile tensorflow lite. For that you just have to run these commands :

`git clone --depth 1 https://github.com/tensorflow/tensorflow.git`

`cd tensorflow`

`make -f tensorflow/lite/micro/tools/make/Makefile generate_projects`

Then you'll have to copy your models in your mbed project (maybe create a folder named `models` ?) after that you'll have to create a folder named `tensorflow_lite` and then copy `tensforflow` & `third_party` folders from `tensorflow/lite/micro/tools/make/gen/$youros/prj/hello_world/mbed/` in it.

Add those folders to the path compiler and implements the inference.


