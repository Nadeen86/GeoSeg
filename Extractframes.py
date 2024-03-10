import sys
import cv2
import os

import MakeVideo as mv
import inference_uavid

def main(video_path,outPath,combinedImagePath,outVideoPath):

    # Path to the video file
    video_path = video_path #'/media/nadin/c5b0209b-0601-4e7b-b0bf-492a1ebb89e2/Videos/images.mp4'

    # Output directory for extracted frames
    output_directory = outPath + "/seq/Images" #'/media/nadin/c5b0209b-0601-4e7b-b0bf-492a1ebb89e2/Videos/outFrames/'

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Initialize variables
    frame_count = 0

    # Read frames from the video
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # Break the loop if no more frames are available
        if not ret:
            break
        
        # Save the frame as a PNG image
        output_path = os.path.join(output_directory, f'frame_{frame_count:04d}.png')
        cv2.imwrite(output_path, frame)
        
        # Increment frame count
        frame_count += 1
        print(f"{frame_count} frames were extracted")

    # Release the video capture object
    cap.release()

    print(f"{frame_count} frames extracted and saved as PNG images in {output_directory}")
    
    sys.argv=["inference_uavid.py","-i", outPath, "-c", "GeoSeg/config/uavid/unetformer.py","-o", combinedImagePath ,"-t", 'lr', "-ph", "1152", "-pw", "1024", "-b", "2","-d", "uavid"]
    inference_uavid.main()

    mv.createVideo(combinedImagePath+"/seq/Result/",outVideoPath)
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py param1 param2")
        sys.exit(1)
    
    # Extract command-line arguments
    video_path = sys.argv[1]
    outPath = sys.argv[2]
    combinedImagePath = sys.argv[3]
    outVideoPath = sys.argv[4]


    main(video_path,outPath,combinedImagePath,outVideoPath)