import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import videointelligence

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'feisty-rigging.json'

# CLOUD VISION APIs
#client = vision.ImageAnnotatorClient()
#print(client)
#print(dir(client))

video_client = videointelligence.VideoIntelligenceServiceClient()

print(video_client)

features = [videointelligence.Feature.LABEL_DETECTION]