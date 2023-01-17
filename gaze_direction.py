import os
import torch

if torch.cuda.is_available():
    print('Using GPU')
    device = 'cuda'
else:
    print('Using CPU')
    device = 'cpu'

if not os.path.isdir('gaze_direction_train'):
    os.mkdir('gaze_direction_train')
if not os.path.isdir('gaze_direction_test'):
    os.mkdir('gaze_direction_test')

args = []
folder = 'train'
for f in os.listdir('train'):
    cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
    args.append(cmd)

folder = 'test'
for f in os.listdir('test'):
    cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
    args.append(cmd)

# for c in tqdm(args):
    # os.system(c)
cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video train/female_session1_fps20.avi -o gaze_direction_train --no-screen'
os.system(cmd)