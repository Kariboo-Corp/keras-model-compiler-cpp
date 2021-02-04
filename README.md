# How to use

*converter_keras.py* is used to create a .tflite model from a .h5 keras model. It's also create a .h cpp library with model coefficient.

*Note : Change the variable **model_name** with your model name.*

#Inference the tflite model
git clone --depth 1 https://github.com/tensorflow/tensorflow.git
cd tensorflow
make -f tensorflow/lite/micro/tools/make/Makefile generate_projects


