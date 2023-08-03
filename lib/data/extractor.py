import os
import cv2
# A class to extract data from video clips
class DataExtractor(object):
    def __init__(self, directory):
        self.location = directory

    def extract(self):
        self.get_video_clips_files()
        self.get_video_clips_duration()
        self.get_video_clips_name()
        self.get_video_clips_extension()
    
    def get_video_clips_files(self):
        self.video_clips_files = os.listdir(self.location)
        self.data_size = len(self.video_clips_files)
    
    def get_video_clips_duration(self):
        self.video_clips_duration = []
        for video_clip in self.video_clips_files:
            video_clip_path = os.path.join(self.location, video_clip)
            video = cv2.VideoCapture(video_clip_path)
            fps = video.get(cv2.CAP_PROP_FPS)
            frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
            duration = frame_count / fps
            self.video_clips_duration.append(duration)

    def get_video_clips_name(self):
        self.video_clips_name = []
        for video_clip in self.video_clips_files:
            video_clip_name = video_clip.split(".")[0]
            self.video_clips_name.append(video_clip_name)
    
    def get_video_clips_extension(self):
        self.video_clips_extension = []
        for video_clip in self.video_clips_files:
            video_clip_extension = video_clip.split(".")[1]
            self.video_clips_extension.append(video_clip_extension)