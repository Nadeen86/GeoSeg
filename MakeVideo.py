import cv2
import os

def createVideo(image_sequence_path,outputVidoPath):

    # Path to the directory containing the image sequence
    image_sequence_dir = image_sequence_path #/media/nadin/c5b0209b-0601-4e7b-b0bf-492a1ebb89e2/Videos/unetformer_r180/seq/Result/'

    # Get the list of image files in the directory
    image_files = sorted([os.path.join(image_sequence_dir, file) for file in os.listdir(image_sequence_dir) if file.endswith('.png')])

    # Define the output video file
    output_video_path = outputVidoPath #'/media/nadin/c5b0209b-0601-4e7b-b0bf-492a1ebb89e2/Videos/unetformer_r180/seq/output_video.mp4'

    # Get the first image to extract its dimensions
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 videos
    fps = 20  # Frames per second
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    Image_Count=0
    # Iterate through each image in the sequence and write it to the video
    for image_file in image_files:
        image = cv2.imread(image_file)
        video_writer.write(image)
        Image_Count+=1
        print(Image_Count)

    # Release the VideoWriter object
    video_writer.release()

    print("Video composed successfully.")

if __name__ == "__main__":
    createVideo()