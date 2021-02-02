import tensorflow as tf
import sys
import os
import subprocess


interpreter_path = sys.executable
print("Running at: ", interpreter_path)

assert tf.__version__ == "1.8.0"

subprocess.call(
    [interpreter_path, "./%s/object_detection/builders/hyperparams_builder_test.py"])
