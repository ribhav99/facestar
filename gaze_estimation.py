import os
import torch

if torch.cuda.is_available():
    print('Using GPU')
    device = 'cuda'
else:
    print('Using CPU')
    device = 'cpu'
gaze_array = '539 633 537 650 493 623 479 651 514 625 493 646 479 618 477 633 709 683 699 707'
gaze_array = '476 673 468 699 434 633 475 670 493 650 482 674 669 653 663 671 664 656 671 669 581 645 585 658'
fps = 20
cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video train/female_session1_fps20.avi -o temp --no-screen --fps {fps} --device {device} --gaze_array {gaze_array}'
os.system(cmd)