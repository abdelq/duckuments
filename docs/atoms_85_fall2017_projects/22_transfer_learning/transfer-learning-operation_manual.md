# Transferred Lane following {#demo-transfer-lane-following status=beta}

TODO: JT: move to operation manual section of teh book

This is the description of transferred lane following demo.

<div class='requirements' markdown="1">

Requires: Wheels calibration completed.[wheel calibration](#wheel-calibration)

Requires: Camera installed in the right position.

Requires: Joystick demo has been successfully launched.[Joystick demo](#rc-control)

Requires: PyTorch installed on duckiebot and laptop. (On duckiebot, you can either build from source([link](http://book.duckietown.org/fall2017/duckiebook/pytorch_install.html#sec:pytorch-install)), or download the [pytorch-0.2 wheel file](https://drive.google.com/open?id=1LhQNIoHLU1cpSEpf_Vpd3jjLDDWUZEOr) we built)

</div>

## Video of expected results 

[link 1 of lane following](https://drive.google.com/open?id=1Ejk0Qw-NuIKNsQFs99nhd0tbmFDdtRvs)
[link 2 of lane following](https://drive.google.com/file/d/1WLr2g_A2MrHwgDoTQ51GwCw9u2iNH-Zo/view?usp=sharing)

## Duckietown setup notes 

A duckietown with white and yellow lanes. No obstacles on the lane.

## Duckiebot setup notes

Make sure the camera is heading ahead. Tighten the screws if necessary. 

## Pre-flight checklist 

Check: turn on joystick. 

Check: Enough battery of the duckiebot. 

## Demo instructions 

Here, give step by step instructions to reproduce the demo.

Step 1: On duckiebot, in /DUCKIERTOWN_ROOT/ directory, run command:

    duckiebot `roslaunch deep_lane_following lane_following.launch`
    
Wait a while so that everything has been launched. Press R1 to start autonomous lane following. Press L1 to switch to joystick control.

The following is the same as demo-lane-following:
Empirically speaking, no duckiebot will successfully run the demo for its first time. Parameter tuning is a must. The only two parameters that you can modify is the gain and trim. The parameter pair which makes your bot go straight will unlikely work for the lane following due to the current controller design. Facts show that a gain ranging from 0.5 to 0.9, as long as paired with a suitable trim, will all work on this demo. Start with your parameter pair obtained from wheel calibration. Increase gain for higher speed. Increase trim to horizontally move the bot to the center of the lane. Decrease will do the inverse. 

Step 2: On laptop, make sure ros environment has been activated, run command:

    laptop `rqt`
    
In rqt, the images can be visualized are /(vehicle_name)/camera_node/image/compressed

## Train the network from scratch

Step 1: Download the simulator docker from  [link](https://hub.docker.com/r/cbschaff/duckietown/), and launch it by following the similar instructions in [link](https://hub.docker.com/r/yanjundream/duckietown_simulator/)

Step 2: Clone [link](https://github.com/ruotianluo/gym-duckietown.git) and run

    laptop `python collect_data.py`

This will generate ~10100 images under `images` folder.

**Note**: you can skip the first two step If you want to download the images we collected. Here is the [link](https://drive.google.com/open?id=1l0WgstSRR_97Gp5wFVJmnjvItRLi00CU))

Step 3: Clone [link](https://github.com/ruotianluo/duckietown_project_pose_estimation.git),
Assume duckietown_project_pose and gym-duckietown are under the same folder.

Step 4: Pretrain on simulation images:

    laptop `cd duckietown_project_pose_estimation; python main.py --augment --use_model2`

You can add `--cuda` if you have gpu available.

Step 5: Download real images from [link](https://drive.google.com/file/d/1P_X1CYiUOwGZtr476Qk22O-Mlu4O7KTI/view?usp=sharing), and decompress under gym-duckietown folder.

Step 6: Finetune on real images, by run:

    laptop `python finetune.py --use_model2 --epochs 200`

Step 7: Checkout branch cbschaff-devel and copy model.

    duckiebot `git checkout cbschaff-devel`
    duckiebot `catkin_make`
    duckiebot `roscd deep_lane_following`
    duckiebot `cp model_file include/deep_lane_following/model.pth.tar`
    

Step 8: Run the ros package.

    duckiebot `roslaunch deep_lane_following lane_following.launch`

## Troubleshooting 

Contact Chip Schaff or Ruotian Luo(TTIC) via Slack if any trouble occurs. 
