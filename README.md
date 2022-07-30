# Deep-Worm-Tracker

This repository contains the code to Deep-Worm-Tracker a realtime Deep Learning based *C. elegans* worm tracker. It is a combination of Deep object detection (YOLO) and tracking (Strong SORT) models.

## Features
* A large scale annotated dataset containing 3000 worm images is made available for training the object detection model.
* A first of its kind *C. elegans* re-id dataset containing 32 worm identities is used for training the tracking model.
* Annotated images account for background variability like worm trails, eggs, change in magnification, dust particles and marker prints used for demacrating quadrants in actual chemotaxis assays.
* Training time reduced to just 9 to 26 min based on network dimensions.
* Fast inference speed of 8 to 15 ms based on the YOLO object detection model.
* Added functionality to segment and skeletonize tracked worms.
* Individual worm trajectories are also highlighted. 

## Steps to Installation

It is reccomended to create separate conda environments for installing individual packages for the object detection (training YOLO model), tracking (training the torchreid model) and combined final model (for getting final track results). The steps would look something like:

1. Clone the repository:

   `git clone https://github.com/knaticat/Deep-Worm-Tracker.git`

2. Setup environments:
    ```bash
       #for running the Deep-Worm-Tracker using pretrained model weights (Quick start)
       cd Deep-Worm-Tracker
       conda create -n yolostrong
       pip install -r requirements.txt
       
       #for training yolo model
       cd yolov5
       conda create -n yolo
       pip install -r requirements.txt
       
       #for training torchreid model
       cd strong_sort
       conda create -n torchreid
       pip install -r requirements.txt
    ```
3. Running the tracker after cloning the Deep-Worm-Tracker repository:

    ```bash
       $ python3 track.py --source <can be video, webcam, image file> --yolo-weights <path to weights file stored in worm_object_weights> 
       --strong-sort-weights <one of mobilenetv2_x1_0_worm.pt, mobilenetv2_x1_4_worm.pt, osnet_ain_x0_5_worm.pt, osnet_x0_5_worm.pt, osnet_x0_25_worm.pt>
       --img <network dimension> --do-segment --do-skeleton --show-track --show-id-black --show-vid --save-vid
    ```
## Training YOLO model

The step by step instructions for training a YOLO model with a new dataset can be found in [YOLO training (link to external repository)](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)&nbsp;.
The worm detection dataset is available at [worm-data](https://drive.google.com/drive/folders/1PM4Rvrz-V6p-xqAEWsz66tAKu4W5x8Mc?usp=sharing) which can be extracted and training resumed.
A combination of [DarkMark](https://github.com/stephanecharette/DarkMark)&nbsp; and [Roboflow](https://roboflow.com/annotate) were used for annotating the dataset images. It's reccomended to use Roboflow for future annotations on newer image data for the user friendly interface. 
## Training Strong SORT reid model

## Acknowledgements

## Cite the work
