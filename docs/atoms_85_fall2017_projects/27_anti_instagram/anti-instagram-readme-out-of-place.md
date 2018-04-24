# Anti Instagram ReadMe {#anti-instagram-readME status=beta}

TODO: JT: move to appropriate code section.

This is the short description of anti-instagram software.

<div class='requirements' markdown="1">

Requires: Camera calibration completed. [Camera calibration](#camera-calib)

</div>

## Video of expected results

<div figure-id="fig:readme-out-of-place">
    <figcaption>Anti instagram video</figcaption>
    <dtvideo src="vimeo:257258742"/>
</div>


## Duckietown setup notes

A duckietown with white and red solid lines, yellow dashed lines and black lane surface. No obstacles on the lane.

## Duckiebot setup note

Any duckiebot satisfying the basic DB17 configuration will work.

## Instructions to use the Anti-Instagram node

### Description of the Anti Instagram Node

Input parameters for the Anti instagram node:
1. _~ai_interval_: This sets the time in seconds between each computation of the color transformation. Default: 10

2. _~fancyGeom_: States what mask should be used to remove the background. If it is set to _false_, just one third from above is cut away to do the color transformation. If it is set to _true_, the flood fill approach is used. [Attention: Very time consuming and not stable results.] Default: false.
3. _~n_centers_: Indicates how many centers for k-Means should be used. Default: 6
4. _~blur_: Indicates what type of blur should be used. Options are _'median'_ or _'gaussian'_. Default: _'median'_
5. _~resize_: Defines by what factor the picture should be resized before computing the transformation. Default: 0.2
6. _~blur_kernel_: Defines the kernel size of the blur. Default: 5
7. _~cb_percentage_: Defines the percentage of data points that should be cut away by the histogram equalization. Default: 2
8. _trafo_mode_: Defines the transformation mode of the color transformation. Options are _'both'_ for histogram equalization first and kMeans after, _'lin'_ for kMeans only and _'cb'_ for histogram equalization only. Default: _'both'_


### How to start the lane following
Step 0: On duckiebot, change to /&#36;DUCKIETOWN_ROOT/ directory and checkout the lastest version of devel-anti-instagram branch.

Step 1: Run command:

    duckiebot &#36; source environment.sh &amp;&amp; source set_ros_master.sh &amp;&amp; source set_vehicle_name.sh

    duckiebot &#36; roslaunch duckietown_demos lane_following.launch

Wait a while so that everything has been launched.

If you accidentally press R1 which starts autonomous lane following, press L1 to switch back to joystick control.

Step 2: On laptop, change to /&#36;DUCKIETOWN_ROOT/ directory and perform the following steps:

    laptop &#36; source environment.sh

    laptop &#36; export ROS_MASTER_URI=http://robot_name.local:11311/

    laptop &#36; rqt_image_view

which opens a window to preview image messages. Select the /robot name/camera_node/image/compressed to view camera image stream. Place the duckiebot somewhere in duckietown.

Step 3:

Run command:

    rosparam set /robot name/line_detector_node/verbose true

so that line_detector_node will publish the result.

Step 4:

To view the result, select in rqt_image_view the topic /robot name/line_detector_node/image_with_lines.
The anti-instagram node is continually running and will determine a proper transformation.

This can be seen as well with the following topics:
*   combination of ~corrected_image and ~uncorrected_image (shows the raw correction)
*   ~geomImage (shows the preprocessed image with the mask)

## Troubleshooting

Contact czuidema@ethz.ch
