import json
import os
import cv2


folder_name = 'youtube_gaze_direction'
parsed_folder_name = 'parsed_data'
metadata_file_path = 'parsed_data/metadata.json'
video_format = '.mp4' # also change fourcc later in code

if not os.path.isdir(os.path.join(parsed_folder_name, 'split_text_files')):
    os.mkdir(os.path.join(parsed_folder_name, 'split_text_files'))

metadata = json.load(open(metadata_file_path, 'r'))

# Split Text Files
for clip in metadata['data']:
    original_name = clip['name'][:clip['name'].rindex('_')]
    # Need to convert spaces to '_'
    try: 
        gaze_data = open(os.path.join(folder_name, original_name + '.txt'), 'r')
        lines = gaze_data.readlines()
        gaze_data.close()
        interval = clip['video_range']
        lines = lines[interval[0]: interval[1]]
        parsed_gaze_data = open(os.path.join(parsed_folder_name, 'split_text_files', clip['name'] + '.txt'))
        for i in lines:
            parsed_gaze_data.write(i)
        parsed_gaze_data.close()
    
    # Split Video Files (original not gaze estimation ones)
        cap = cv2.VideoCapture(os.path.join(folder_name, original_name + video_format))
        cap.set(cv2.CAP_PROP_POS_FRAMES, interval[0])
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(os.path.join('split_videos', clip['name'] + video_format), fourcc, int(clip['fps']))

        for _ in range(interval[1] - interval[0] + 1):
            ret, frame = cap.read()
            if not ret:
                print(f"couldn't read frame from video {original_name} or {clip['name']}")
            out.write(frame)
        cap.release()
        out.release()
    
    except FileNotFoundError:
        print(f'{clip} not found')