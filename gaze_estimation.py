import os
import torch

if torch.cuda.is_available():
    print('Using GPU')
    device = 'cuda'
else:
    print('Using CPU')
    device = 'cpu'

gaze_array = '671 608 675 623 476 673 468 699 434 633 475 670 493 650 482 674 669 653 663 671 664 656 671 669 581 645 585 658 622 618 615 624 609 679 618 649'
no_gaze_array = '496 691 476 779 551 731 549 848 495 617 455 624 643 662 602 697 625 644 689 639 608 621 552 636 567 608 587 598 579 644 528 657 563 640 493 657'
fps = 20
cmd = f'python3 ../gazeEstimation/ptgaze/__main__.py --mode eth-xgaze --video train/female_session1_fps20.avi -o temp --no-screen --fps {fps} --device {device} --gaze_array {gaze_array} --no_gaze_array {no_gaze_array}'
os.system(cmd)