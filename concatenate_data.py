import cv2
import os
from pqdm.processes import pqdm
import multiprocessing

def get_session_and_cut_number(name):
    return int(name[7:9]), int(name[-6:-4])

def concatenate_videos_and_audio(session, folder_path='male_speaker/trainset', dataset='train', target_fps=20):
    initialised = False
    gender = folder_path[:folder_path.index('_')]

    for f in sorted(os.listdir(folder_path)):
        sesh, _ = get_session_and_cut_number(f)
        path = os.path.join(folder_path, f)

        if f.endswith('.mp4') and sesh == session:
            cap = cv2.VideoCapture(path)
            if initialised == False:
                fps = cap.get(cv2.CAP_PROP_FPS)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(f'{dataset}/{gender}_session{sesh}_fps{target_fps}.avi', fourcc, target_fps, (int(cap.get(3)),int(cap.get(4))))
                initialised = True

            count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                if count % (fps // target_fps) == 0:
                    out.write(frame)
                count += 1
            
            cap.release()
    
    if initialised:
        out.release()
        
        cv2.destroyAllWindows()

if __name__ == '__main__':
    if not os.path.isdir('train'):
        os.mkdir('train')
    if not os.path.isdir('test'):
        os.mkdir('test')
    args = []
    # target_fps must be a divisor of 60
    for i in range(1, 100):
        d1 = {'session': i, 'folder_path': 'male_speaker/trainset', 'dataset': 'train', 'target_fps': 20}
        d2 = {'session': i, 'folder_path': 'male_speaker/testset', 'dataset': 'test', 'target_fps': 20}
        d3 = {'session': i, 'folder_path': 'female_speaker/trainset', 'dataset': 'train', 'target_fps': 20}
        d4 = {'session': i, 'folder_path': 'female_speaker/trainset', 'dataset': 'test', 'target_fps': 20}
        args.append(d1)
        args.append(d2)
        args.append(d3)
        args.append(d4)
    
    result = pqdm(args, concatenate_videos_and_audio, n_jobs=multiprocessing.cpu_count(), argument_type='kwargs')