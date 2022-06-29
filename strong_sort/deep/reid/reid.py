import torchreid
from torchreid import models
from wormreid import Worm

if __name__ == '__main__':
    torchreid.data.register_video_dataset('worm-reid-data', Worm)

    datamanager = torchreid.data.VideoDataManager(
        root= '/home/user/Deep-Worm-Tracker/strong_sort/',
        sources= 'worm-reid-data',
        height= 150,
        width=100,
        transforms=["random_flip", "random_crop"] 
    )
    
    model = torchreid.models.build_model(
        name= 'mobilenetv2_x1_4',
        num_classes=datamanager.num_train_pids,
        loss="softmax",
        pretrained= True   
    )
    model = model.cuda()

    optimizer = torchreid.optim.build_optimizer(
        model,
        optim='adam',
        lr=0.0003
    )

    scheduler = torchreid.optim.build_lr_scheduler(
        optimizer,
        lr_scheduler="single_step",
        stepsize=20
    )

    engine = torchreid.engine.VideoSoftmaxEngine(
        datamanager,
        model,
        optimizer=optimizer,
        scheduler=scheduler,
        label_smooth=True
    )

    engine.run(
        save_dir="/home/user/Deep-Worm-Tracker/strong_sort/deep/checkpoint/mobilenetv2/",
        max_epoch=100,
        eval_freq=10,
        print_freq=31,
        test_only=False,
    )
    