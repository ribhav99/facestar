import json
import os

folder_name = 'youtube_gaze_direction'
parsed_folder_name = 'parsed_data'
metadata_file_path = 'parsed_data/metadata.json'

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
    except FileNotFoundError:
        print(f'{clip} not found')

# TODO: Perform clustering and gaze prediction using text files
# TODO: Split Video Files 
# TODO: Annotate video files using the text files from clustering