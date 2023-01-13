import os
from pqdm.processes import pqdm
import multiprocessing

if not os.path.isdir('gaze_direction_train'):
    os.mkdir('gaze_direction_train')
if not os.path.isdir('gaze_direction_test'):
    os.mkdir('gaze_direction_test')

def run_gaze_estimation(folder, f):
    cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video {os.path.join(folder, f)} -o gaze_direction_{folder}'
    os.system(cmd)

args = []
for f in os.listdir('train'):
    d = {'folder': 'train', 'f': f}
    args.append(d)

for f in os.listdir('test'):
    d = {'folder': 'test', 'f': f}
    args.append(d)

result = pqdm(args, run_gaze_estimation, n_jobs=multiprocessing.cpu_count(), argument_type='kwargs')
