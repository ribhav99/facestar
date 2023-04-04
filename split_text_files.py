import json
import os
import cv2
from tqdm import tqdm


folder_name = 'youtube_data_gaze_direction'
original_folder = 'youtube_data'
parsed_folder_name = 'parsed_data'
metadata_file_path = 'parsed_data/metadata.json'
video_format = '.mp4' # also change fourcc later in code

if not os.path.isdir(os.path.join(parsed_folder_name, 'split_text_files')):
    os.mkdir(os.path.join(parsed_folder_name, 'split_text_files'))

metadata = json.load(open(metadata_file_path, 'r'))

# Split Text Files
for clip in tqdm(metadata['data']):
    original_name = clip['name'][:clip['name'].rindex('_')]
    original_name = original_name.replace(" ", "_")
    clip_name = clip['name'].replace(" ", "_")
    if os.path.isfile(os.path.join(parsed_folder_name, 'split_videos', clip_name + video_format)):
        continue
    try: 
        gaze_data = open(os.path.join(folder_name, original_name + '.txt'), 'r')
        lines = gaze_data.readlines()
        gaze_data.close()
        interval = clip['video_range']
        lines = lines[interval[0]: interval[1]]
        parsed_gaze_data = open(os.path.join(parsed_folder_name, 'split_text_files', clip_name + '.txt'), 'w')
        for i in lines:
            parsed_gaze_data.write(i)
        parsed_gaze_data.close()
    
    # Split Video Files (original not gaze estimation ones)
        cap = cv2.VideoCapture(os.path.join(original_folder, original_name + video_format))
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(os.path.join(parsed_folder_name, 'split_videos', clip_name + video_format), fourcc, int(float(clip['fps'])), (width, height), True)
        cap.set(cv2.CAP_PROP_POS_FRAMES, interval[0])
        for _ in range(interval[1] - interval[0] + 1):
            ret, frame = cap.read()
            if not ret:
                print(f"couldn't read frame from video {original_name} or {clip['name']}")
            
            out.write(frame)
        cap.release()
        out.release()
    
    except FileNotFoundError:
        print(f'{clip} not found')
    
    