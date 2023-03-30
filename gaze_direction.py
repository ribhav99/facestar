import os
import torch
from tqdm import tqdm

if torch.cuda.is_available():
    print('Using GPU')
    device = 'cuda'
elif torch.backends.mps.is_available():
    print('Using MPS')
    device = 'mps'
else:
    print('Using CPU')
    device = 'cpu'

# if not os.path.isdir('gaze_direction_train'):
#     os.mkdir('gaze_direction_train')
# if not os.path.isdir('gaze_direction_test'):
#     os.mkdir('gaze_direction_test')

# args = []
# folder = 'train'
# for f in os.listdir('train'):
#     cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
#     args.append(cmd)

# folder = 'test'
# for f in os.listdir('test'):
#     cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video {os.path.join(folder, f)} -o gaze_direction_{folder} --no-screen'
#     args.append(cmd)

# for c in tqdm(args):
#     os.system(c)
# cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --fps 20 --device {device} --video train/female_session1_fps20.avi -o gaze_direction_train --no-screen'
# os.system(cmd)
folder = 'youtube_data'
save_folder = 'youtube_data_gaze_direction'
for f in tqdm(os.listdir(folder)):
    os.rename(os.path.join(folder, f), os.path.join(folder, f.replace(" ", "_")))
    f = f.replace(" ", "_")
    print(f)
    if not os.path.isfile(os.path.join(save_folder, f)):
        cmd =  f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video {os.path.join(folder, f)} -o {save_folder} --fps 20 --z_val 0.375 --device {device} --no-screen -e mp4 --write_file'
        os.system(cmd)