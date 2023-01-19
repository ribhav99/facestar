import cv2
from tqdm import tqdm
import random
import os
random.seed(6)

def export_images(video, n=100):
    cap = cv2.VideoCapture(video)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'Total Frames = {total_frames}; # Samples = {n}')
    count = 0
    pbar = tqdm(total=total_frames)
    # i = set(random.sample(range(0, total_frames-1), n))
    # explicitly because random.seed was not consistent
    i = {1536, 8194, 9730, 7, 1543, 4103, 9231, 3092, 7704, 2078, 1572, 6183, 9786, 6716, 8252, 1598, 7229, 3649, 6222, 3161, 603, 3173, 5232, 8819, 7294, 6783, 4737, 8835, 9859, 10378, 7309, 3214, 9882, 3230, 7326, 10402, 4770, 3245, 9401, 4286, 3262, 205, 2771, 2262, 3291, 9435, 5855, 6376, 748, 9964, 8432, 7925, 4350, 7946, 9995, 5904, 6928, 279, 5920, 4389, 7974, 1320, 5933, 6958, 8007, 8009, 5454, 2385, 358, 8554, 9070, 3438, 881, 4467, 6516, 1914, 5498, 4986, 7040, 9608, 10135, 5015, 8605, 1443, 1959, 9643, 4012, 9138, 10162, 9652, 4019, 1459, 1469, 8640, 465, 3036, 6113, 1525, 6137, 5116}
    if not os.path.isdir(f'{video[:-4]}'):
        os.mkdir(f'{video[:-4]}')

    index = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            print(f'breaking after {count} frames')
            break
        
        if count in i:
            cv2.imwrite(f'{video[:-4]}/{index}.png', frame)
            index += 1

        count += 1
        pbar.update(1)

    cap.release()
    pbar.close()
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    export_images('temp/female_session1_fps20_smoothed.avi')
