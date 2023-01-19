import os
import torch
import numpy as np

if torch.cuda.is_available():
    print('Using GPU')
    device = 'cuda'
else:
    print('Using CPU')
    device = 'cpu'

indices = {1536, 8194, 9730, 7, 1543, 4103, 9231, 3092, 7704, 2078, 1572, 6183, 9786, 6716, 8252, 1598, 7229, 3649, 6222, 3161, 603, 3173, 5232, 8819, 7294, 6783, 4737, 8835, 9859, 10378, 7309, 3214, 9882, 3230, 7326, 10402, 4770, 3245, 9401, 4286, 3262, 205, 2771, 2262, 3291, 9435, 5855, 6376, 748, 9964, 8432, 7925, 4350, 7946, 9995, 5904, 6928, 279, 5920, 4389, 7974, 1320, 5933, 6958, 8007, 8009, 5454, 2385, 358, 8554, 9070, 3438, 881, 4467, 6516, 1914, 5498, 4986, 7040, 9608, 10135, 5015, 8605, 1443, 1959, 9643, 4012, 9138, 10162, 9652, 4019, 1459, 1469, 8640, 465, 3036, 6113, 1525, 6137, 5116}

with open('temp/female_session1_fps20_smoothed.txt', 'r') as file:
    info = file.readlines()
pts = [i.split(' ') for i in info]
preds = [i[0] for i in pts]
pts = [[(int(i[1].strip()[1:-1]), int(i[2].strip()[:-1])), 
        (int(i[3].strip()[1:-1]), int(i[4].strip()[:-1]))] for i in pts] 

gaze_array = []
no_gaze_array = []

count = 0
for i in indices:
    if preds[i] == 'True':
        gaze_array.append(pts[i])
    else:
        no_gaze_array.append(pts[i])
    count += 1
    if count == 20:
        break

gaze_array = np.array(gaze_array)
no_gaze_array = np.array(no_gaze_array)
gaze_array = gaze_array.flatten().tolist()
no_gaze_array = no_gaze_array.flatten().tolist()
gaze_array = ' '.join([str(i) for i in gaze_array])
no_gaze_array = ' '.join([str(i) for i in no_gaze_array])


# gaze_array = '671 608 675 623 476 673 468 699 434 633 475 670 493 650 482 674 669 653 663 671 664 656 671 669 581 645 585 658 622 618 615 624 609 679 618 649'
# no_gaze_array = '496 691 476 779 551 731 549 848 495 617 455 624 643 662 602 697 625 644 689 639 608 621 552 636 567 608 587 598 579 644 528 657 563 640 493 657'
fps = 20
cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video train/female_session1_fps20.avi -o temp --no-screen --fps {fps} --device {device} --gaze_array {gaze_array} --no_gaze_array {no_gaze_array}'
os.system(cmd)