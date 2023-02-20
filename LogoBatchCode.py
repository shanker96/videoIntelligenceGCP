import io
import os
from google.cloud import videointelligence

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'neuro-insight-376720-362489f4a64a.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'feisty-rigging.json'

input_folder = "/Users/shan/Desktop/SMU/Spring/Capstone/VisionAPIDemo/demoVids"
features = [videointelligence.Feature.LOGO_RECOGNITION]

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        video_path = os.path.join(input_folder, filename)
        with io.open(video_path, "rb") as movie:
            input_content = movie.read()

        video_client = videointelligence.VideoIntelligenceServiceClient()
        operation = video_client.annotate_video(
            request={"features": features, "input_content": input_content}
        )
        print("\nProcessing video {} for logo recognition:".format(filename))

        result = operation.result(timeout=180)
        print("\nFinished processing video {}.".format(filename))
        print(result)

        # Process shot level logo annotations
        shot_labels = result.annotation_results[0].shot_label_annotations
        for i, shot_label in enumerate(shot_labels):
            print("Shot label description for video {}: {}".format(filename, shot_label.entity.description))
            for entity in shot_label.entities:
                print("\tEntity description: {}".format(entity.description))
                print("\tConfidence: {}".format(entity.confidence))
            for i, shot in enumerate(shot_label.segments):
                start_time = (
                    shot.segment.start_time_offset.seconds
                    + shot.segment.start_time_offset.microseconds / 1e6
                )
                end_time = (
                    shot.segment.end_time_offset.seconds
                    + shot.segment.end_time_offset.microseconds / 1e6
                )
                positions = "{}s to {}s".format(start_time, end_time)
                confidence = shot.confidence
                print("\tSegment {}: {}".format(i, positions))
                print("\tConfidence: {}".format(confidence))
            print("\n")
