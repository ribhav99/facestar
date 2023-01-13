import os
from tqdm import tqdm

if not os.path.isdir('gaze_direction_train'):
    os.mkdir('gaze_direction_train')
if not os.path.isdir('gaze_direction_test'):
    os.mkdir('gaze_direction_test')

args = []
folder = 'train'
for f in os.listdir('train'):
    cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
    args.append(cmd)

folder = 'test'
for f in os.listdir('test'):
    cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
    args.append(cmd)

for c in tqdm(args):
    os.system(c)