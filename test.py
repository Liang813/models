import tensorflow as tf
import sys
import os
import subprocess


interpreter_path = sys.executable
print("Running at: ", interpreter_path)

assert tf.__version__ == "1.8.0"


def get_target_dir():
    for x in os.listdir(os.path.dirname(os.path.abspath(__file__))):
         return x
print(
    "Cautious: this subject can only be triggered with certain protobuf vetsion! See https://github.com/tensorflow/models/issues/1617")
subprocess.call(
    [interpreter_path, "./%s/object_detection/builders/hyperparams_builder_test.py" % get_target_dir()])
