import os
import tensorflow as tf
from tensorflow import keras

model_name = 'train_yes_conv_8_drop_yes_dense_64'

model = tf.keras.models.load_model('./' + model_name + '.h5')

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()

# Save the model.
with open(model_name + '.tflite', 'wb') as f:
  f.write(tflite_model)

def hex_to_c_array(hex_data, var_name):

  c_str = ''

  c_str += '#ifndef ' + var_name.upper() + '_H\n'
  c_str += '#define ' + var_name.upper() + '_H\n\n'
  c_str += '\nconst unsigned int ' + var_name + '_len = ' + str(len(hex_data)) + ';\n'

  c_str += 'const unsigned char ' + var_name + '[] = {'
  hex_array = []

  for i, val in enumerate(hex_data) :
    hex_str = format(val, '#04x')

    if (i + 1) < len(hex_data):
      hex_str += ','
    if (i + 1) % 12 == 0:
      hex_str += '\n'

    hex_array.append(hex_str)

  c_str += '\n ' + format(' '.join(hex_array)) + '\n};\n\n'

  c_str += '#endif //' + var_name.upper() + '_H'

  return c_str

with open(model_name + '.h', 'w') as file:
  file.write(hex_to_c_array(tflite_model, model_name))