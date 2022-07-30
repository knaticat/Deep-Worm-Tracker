# Strong SORT with PyTorch

This folder contains Strong SORT model trained on the worm reid dataset.

## Dependencies
- python 3 (python2 not sure)
- numpy
- scipy
- opencv-python
- sklearn
- torch >= 0.4
- torchvision >= 0.1
- pillow
- vizer
- edict
   

## Training the RE-ID model for StrongSORT

1. Download and extract the [worm-reid-dataset](https://drive.google.com/drive/folders/13ZfVVmoCg2Z58oicaYwotK1johqDDZTM?usp=sharing)&nbsp;.
2. The directory structure is similar to the MARS dataset containing a bbox_train, bbox_test and info folder. Out of 32 worm identities we use a 80:20 training to testing split. the info folder contains description of the train_name and test_name .txt file that contain the image information for each worm identity. The naming convention used is same as the [MARS dataset](http://zheng-lab.cecs.anu.edu.au/Project/project_mars.html)&nbsp; which is:
In bbox "0001C1T0002F0016.jpg", "0065" is the ID of the worm. "C1" denotes the single camera used. "T0002" means the 2th tracklet. "F016" is the 16th frame within this tracklet. For the tracklets which were each of 20-30s duration videos, their names are accumulated for each ID. The frames start from "F001" in each tracklet.
3. The track_train_info.mat and track_test_info.mat matrices contains in order for each tracklet: start frame (column 1), end frame (column 2), worm-id (column 3) and camera index (column 4). Note that the CMC evaluation metric expects that gallery images have different camera indices in the test and train data. Thus, we set camera indices as 0 and 1 for the indvidual identities in the track_test_info matrix.
4. The query_IDX.mat contains the query indices for checking against the gallery images.

After this, to train torchreid models available we have defined a [wormreid.py](deep/reid/wormreid.py) file that is used to register our dataset in the format expected by the torchreid engine.

**To start training:**
* Find the [reid.py](deep/reid/reid.py) file.
* Choose the model to be used for training on the reid dataset.
* Run the reid.py file after adjusting hyperparameters. The training can be monitored by tensorboard.

## Training the RE-ID model for DeepSORT
The original model used in paper is in original_model.py, and its parameter here [original_ckpt.t7](https://drive.google.com/drive/folders/1xhG0kRH1EX5B9_Iz8gQJb7UNnn_riXi6).  

To train the model, first you need download [Market1501](http://www.liangzheng.com.cn/Project/project_reid.html) dataset or [Mars](http://www.liangzheng.com.cn/Project/project_mars.html) dataset.  

Then you can try [train.py](deep_sort/deep/train.py) to train your own parameter and evaluate it using [test.py](deep_sort/deep/test.py) and [evaluate.py](deep_sort/deep/evalute.py).



