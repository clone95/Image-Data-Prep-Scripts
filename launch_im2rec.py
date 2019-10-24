import mxnet as mx
import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import tarfile
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

im2rec_path = mx.test_utils.get_im2rec_path()
data_path = os.path.join('./data','/sagemaker_val')
prefix_path = os.path.join('./data','/val')

with open(os.devnull, 'wb') as devnull:
    subprocess.check_call(['python', im2rec_path, '--list', '--recursive', prefix_path, data_path],
                          stdout=devnull)