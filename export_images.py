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
    i = set(random.sample(range(0, total_frames-1), n))

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
