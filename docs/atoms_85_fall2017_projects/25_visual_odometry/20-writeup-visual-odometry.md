# Visual Odometry Project {#visual-odometry-int-rep status=beta}

Here we briefly describe the theory behind the model in the visual odometry project.  The discussion begins with a review of epipolar geometry and a description of the depth image-based rendering problem, then moves to the description of the deep learning model used.

## Epipolar geometry and DIBR

<div figure-id="fig:epipolar-geometry" figure-caption="Epipolar geometry.">
     <img src="epipolar.png" width='400' style='width: 5em'/>
</div>

We follow the discussion in Sun et al. (2010).  First, consider the stereo setup and recall the relationship between a world point

\begin{align}
m1 = \frac{1}{Z} K1 \cdot R1 [I| -C1]M \\
m2 = \frac{1}{Z} K2 \cdot R2 [I| -C2]M
\end{align}

If we choose the left camera as the reference, we can set $R1=I, C2=0$ in order to get:
\begin{align}
m1 = \frac{1}{Z}K1 \cdot [I|0] M \\
m2 = \frac{1}{Z}K2 \cdot R[I|-C]M
\end{align}

and then we can get the relationship with depth $Z$:

\begin{align}
Zm2 = ZK2 R K1^{-1}m1 + K2 C
\end{align}

Using this relationship, we can learn a prediction for $Z$ and use image $m1$ to predict image $m2$--we describe the experiments below.

## Learning Depth Prediction

We consider an end-to-end CNN-based unsupervised learning system for depth estimation, using the paper Unsupervised Learning of Depth and Ego-Motion from Video by Zhou et al., CVPR 2017.  This model was initially trained on the KITTI dataset, and we take the pre-trained weights and evaluate them in Duckietown, showing that the results can be significantly improved by fine-tuning with Duckietown images.  Our goal is real-time inference, and at test time we only use the depth prediction network:

<div figure-id="fig:dispnet" figure-caption="The general architecture.">
     <img src="dispnet.png" width='400' style='width: 15'/>
</div>

The model consists of two networks--a pose estimation network giving us $R,t$ between the source and target frames, and a depth prediction network that gives us $Z$ and allows us to warp the source view to the target view using the pose and the RGB values in the source image.  Over time, the depth prediction network begins to predict reasonable depth values.
The result of fine-tuning on Duckietown data plus KITTI pretraining versus applying trained model on the KITTI dataset directly:

<div figure-id="fig:finetune" figure-caption="Fine tuning on our dataset.">
     <img src="pretrain.png" width='500' style='width: 15'/>
</div>

When the bot turns, motion blur heavily affects the model predictions. One way to alleviate this problem would be to preprocess input images. First deblur them and then feed them to the depth prediction network. Having blurred images in the training set would also slightly improve the results:

<div figure-id="fig:blur" figure-caption="Results on motion-blurred images.">
     <img src="blur.png" style='width: 15'/>
</div>

## True Depth

We benchmark our results against the true distance from the camera we get from April tag detection.  In the figure below, we show the predicted depth values versus the estimated depth:

<div figure-id="fig:realdepth" figure-caption="Comparison to true depth.">
     <img src="real_depth.png" style='width: 15'/>
</div>

Outliers at low depths are due to lack of texture around April tags. As we can see with proper scaling our estimated depth is well aligned with the  estimated depth from April tags--using a sparse set of true depth maps, we can rescale our pixelwise prediction into metric units.

## Conclusions

We demonstrated a monocular depth estimation pipeline, trained with no annotated data.  The approach gives reasonable depth predictions in Duckietown, but we found several notable limitations.  The results on motion-blurred frames are poor, even after fine-tuning with a small number of blurred images--for good results in fast-moving environments, we would likely need to train with more blur.  In addition, our approach does not incorporate any traditional depth post-processing, which should significantly improve results.

Our depth prediction node could be used for a variety of tasks, including point-cloud-based SLAM as well as obstacle detection.

## References

[Unsupervised Learning of Depth and Ego-motion from Video](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/)

[Depth Image-Based Rendering](http://www.apsipa.org/proceedings_2010/pdf/APSIPA197.pdf)

Author: Igor

Maintainer: Igor

Point of Contact: Igor
