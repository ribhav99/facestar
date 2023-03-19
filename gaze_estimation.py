import os
import torch
import time
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

# indices = {1536, 8194, 9730, 7, 1543, 4103, 9231, 3092, 7704, 2078, 1572, 6183, 9786, 6716, 8252, 1598, 7229, 3649, 6222, 3161, 603, 3173, 5232, 8819, 7294, 6783, 4737, 8835, 9859, 10378, 7309, 3214, 9882, 3230, 7326, 10402, 4770, 3245, 9401, 4286, 3262, 205, 2771, 2262, 3291, 9435, 5855, 6376, 748, 9964, 8432, 7925, 4350, 7946, 9995, 5904, 6928, 279, 5920, 4389, 7974, 1320, 5933, 6958, 8007, 8009, 5454, 2385, 358, 8554, 9070, 3438, 881, 4467, 6516, 1914, 5498, 4986, 7040, 9608, 10135, 5015, 8605, 1443, 1959, 9643, 4012, 9138, 10162, 9652, 4019, 1459, 1469, 8640, 465, 3036, 6113, 1525, 6137, 5116}

# with open('temp/female_session1_fps20_smoothed.txt', 'r') as file:
#     info = file.readlines()
# pts = [i.split(' ') for i in info]
# preds = [i[0] for i in pts]
# pts = [[(int(i[1].strip()[1:-1]), int(i[2].strip()[:-1])), 
#         (int(i[3].strip()[1:-1]), int(i[4].strip()[:-1]))] for i in pts] 

# gaze_array = []
# no_gaze_array = []

# count = 0
# for i in indices:
#     if preds[i] == 'True':
#         gaze_array.append(pts[i])
#     else:
#         no_gaze_array.append(pts[i])
#     count += 1
#     if count == 20:
#         break

# gaze_array = np.array(gaze_array)
# no_gaze_array = np.array(no_gaze_array)
# gaze_array = gaze_array.flatten().tolist()
# no_gaze_array = no_gaze_array.flatten().tolist()
# gaze_array = ' '.join([str(i) for i in gaze_array])
# no_gaze_array = ' '.join([str(i) for i in no_gaze_array])

# startTime = time.time()

# fps = 20
# cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video train/female_session2_fps20.avi -o temp --fps {fps} --device {device} --no-screen'
# os.system(cmd)

# executionTime = (time.time() - startTime)
# print('Execution time in seconds (control): ' + str(executionTime))



# startTime = time.time()

# gaze_array = '-0.0429782 -0.05548361 0.48281293 -0.04505863 -0.04348324 0.43431898 -0.0212611 -0.04447967 0.46616865 -0.02198714 -0.03692097 0.41674862'
# no_gaze_array = '-0.03726508 -0.3792474 0.48640499 -0.03627558 -0.00343993 0.45021358 -0.02198972 -0.05679698 0.45034036 -0.04086373 -0.04784575 0.40491297 -0.01574556 -0.06379504 0.46180735 0.00333104 -0.05674005 0.41613121 -0.05309963 -0.02858958  0.47478823 -0.05173415  0.00725219  0.43995286 -0.03407786 -0.05126658  0.45401565 -0.03578434 -0.02661728  0.41054727 -0.03289039 -0.06354449  0.47361507 -0.04204437 -0.05824631  0.42474653'
# fps = 20
# cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video train/female_session2_fps20.avi -o temp --fps {fps} --device {device} --gaze_array {gaze_array} --no_gaze_array {no_gaze_array} --no-screen'
# os.system(cmd)

# executionTime = (time.time() - startTime)
# print('Execution time in seconds for algo: ' + str(executionTime))

folder = 'youtube_data'
for f in tqdm(os.listdir(folder)):
    os.rename(os.path.join(folder, f), os.path.join(folder, f.replace(" ", "_")))
    f = f.replace(" ", "_")
    if not os.path.isfile(os.path.join("youtube_data_gaze_direction", f)) or os.path.isfile(os.path.join('../gazeEstimation/assets/results/', f[:-3] + "avi")):
        continue
    cmd =  f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video {os.path.join(folder, f)} -o ../gazeEstimation/assets/results/ --fps 20 --z_val 0.375 --device {device} --no-screen --gaze_vector_file {os.path.join("youtube_data_gaze_direction", f[:-3] + "txt")}'
    os.system(cmd)
    break