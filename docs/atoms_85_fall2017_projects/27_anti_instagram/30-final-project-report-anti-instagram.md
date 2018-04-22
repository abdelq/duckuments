# Anti-Instagram: final report {#anti-instagram-final-report status=beta}

## The final result

<div figure-id="fig:example-embed">
    <figcaption>Anti instagram video</figcaption>
    <dtvideo src="vimeo:257258742"/>
</div>

TODO: add link to operation manually, add link to README / code sections (README.txt is in this folder - move to appropriate code section)

## Mission and Scope

### Motivation

During the process of autonomous driving the Duckiebot has to know where to drive and where not. For example the road marking or obstacles on the road give constraints where the allowable area to drive is.  
Let's take the road marking example. For Duckietown it is true that the road is rather black, the stopping lines are red, the side lines are white and the dashed middle lines are yellow.  
Knowing about this color information the Duckiebot is theoretically able to know whether it is on the correct lane position or not. By detecting the lines and estimating the position the Duckiebot can know whether it should drive more left or right or stay in the same position.  
This is only possible if we are assuming the line detection is done perfectly.  
Bus the line detection and especially the classification is done with the color information.  
The problem now is that the color can vary due to illumination variation. So the classification can fail and therefore the performance suffers.  
To sum up the lower the variance in the color of the lines the better the classification and the better the autonomous driving performance of the Duckiebot.

### Existing solution

Before we started our project a solution was already implemented. The existing approach was estimating a color transformation by using k-Means algorithm with 3 centers.  
First "true colors" were defined. These "true colors" should represent the best colors for the lines. So if the road marking lines would be in these predefined red, yellow and white the color classification would work the best.  
So this approach took all the pixels of the camera image and estimated three centers with the k-Means algorithm.  
Afterwards the three found centers were compared with the previously defined "true colors". The difference of the centers found by k-Means and the "true colors" lead to the color transformation.  
Maybe you can better imagine the procedure as follows:  
You take all the pixels and their RGB values. Then you plot each pixel in your imaginary R,G,B coordinate system.  
The k-Means algorithm now tries to detect clusters in this RGB space and estimates the center of these clusters. The centers of these clusters are now compared to the "true centers" which is the location of the optimal red for example in the RGB space. This leads to a transformation which is applied to every image from the camera of the Duckiebot.

### Opportunity

#### Advantages of existing solution

1. The idea of estimating a color transformation from a captured image based on estimated and true centers is very promising since it really focuses on transforming the colors.  
Often other image transformations focus on white balance. But we are concerned the most of the colors. So this clustering approach is a good idea here.

2. k-Means is a fairly simple approach and can be used for unsupervised learning. This is very interesting for a future online implementation.

#### Disadvantages of existing solution {#anti-instagram-disadvantages-existing}

1. The k-Means clustering was initialized only with 3 centers. This is a very rough guess. By analyzing several sample images one sees that there are distinct white, red and yellow clusters. They can indeed be represented by three distinct centers. But the problem is that all the other pixels have to assigned to a cluster as well. This distorts the color transformation.

2. The existing solution was not online. The color transformation had to estimated explicitly by pressing a button on the joystick. Firstly the system is not fully autonomous anymore since it needs user input (pressing the button). And secondly the user doesn't or cannot really know when the optimal moment is for a color transformation.

We sampled several pictures and tested the old implementation. Following a table with the sample pictures and the outputs.

Example 1:

<div>
      <img src="ad1_orig.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
      <img src="ad1_corr.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
      <p style="clear: both;"></p>
</div>

This was a good working example. The euclidean error of "true" centers compared to the centers which are estimated in the picture decreased from 175.541 to 43.724.  

Example 2:

<div>
      <img src="disad1_original.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
      <img src="disad1_corr.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
      <p style="clear: both;"></p>
</div>


This was a medium working example. The euclidean error of "true" centers compared to the centers which are estimated in the picture increased from 115.267 to 56.646

Example 3:

<div>
      <img src="disad2_orig.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
      <img src="disad2_corr.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
      <p style="clear: both;"></p>
</div>

A bad example. The error increased 78.114 to 146.192.

### Preliminaries

Preliminaries to the following topics would be good to have:
- [Clustering methods](#preliminaries-clustering-methods)
- [Convex optimization](#preliminaries-convex-optimization)
- [Histogram equalization](#preliminaries-histogram-equalization)

## Definition of the problem

The general idea is to find a transformation matrix $T$ which converts the original image such that we have the best colors for the color classification.

### Mathematical definition

#### General color transform {#anti-instagram-mathematical-general-transform}
A general color transformation is stated as follows:

\[
\vec{c}_{\text{transformed}}

=

T

\cdot

\vec{c}_{\text{in}}

=

\begin{pmatrix}
k_{1,1} & k_{1,2} & k_{1,3} \\
k_{2,1} & k_{2,2} & k_{2,3} \\
k_{3,1} & k_{3,2} & k_{3,3} \\
\end{pmatrix}

\cdot

\begin{pmatrix}
R_{\text{in}} \\
G_{\text{in}} \\
B_{\text{in}} \\
\end{pmatrix}

=

\begin{pmatrix}
R_{\text{transformed}} \\
G_{\text{transformed}} \\
B_{\text{transformed}} \\
\end{pmatrix}
\]

Where we have $\vec{c}_{\text{in}}$ as the input pixel values (a value per channel) and the vector $\vec{c}_{\text{transformed}}$ is the output of the color transform.
But first we used a slightly simpler color transform. Because we wanted to have a color transform which doesn't depend on other channels but only on one.
One wants to find for each of the channels (e.g. RGB) a scale factor and a shift value. This leads to the following mathematical formulation:
\[
\begin{pmatrix}
R_{\text{transformed}} \\
G_{\text{transformed}} \\
B_{\text{transformed}} \\
\end{pmatrix}

=

\begin{pmatrix}
k_{\text{red}} & 0 & 0 \\
0 & k_{\text{green}} & 0 \\
0 & 0 & k_{\text{blue}} \\
\end{pmatrix}

\cdot

\begin{pmatrix}
R_{\text{detected}} \\
G_{\text{detected}} \\
B_{\text{detected}} \\
\end{pmatrix}

+

\begin{pmatrix}
s_{\text{red}} \\
s_{\text{green}} \\
s_{\text{blue}} \\
\end{pmatrix}

\]

where $k_i$ stand for the different scale factors for each channel and $s_i$ are the shift factors for each channel.  
RGB color channel is just chosen as an example. The transform is valid for other channels as well. The best channel should be determined later.

Now with the found scales and shifts or with a full matrix as stated first we would have a color transform which can be applied to every image captured by the camera.  
This color transform would correct the image such that the colors are best to be detected by the line detector and hence the classifiction of the lines would work perfectly.

## Contribution / Added functionality

As a first idea we wanted to improve the current implementation. So we further investigated the k-Means approach.

### k-Means Approach
_Implemented in the kMeansClass found in the kmeans_rebuild.py file._
_This is set with the parameter lin for the trafomode in the ContAntiInstagramNode._

#### Idea {#anti-instagram-k-means-idea}

The core idea of the clustering approach is to define some "true" colors for the colors to be transformed. In the Duckiebot case these are yellow, white, black and red. These "true" colors can be defined differently if wished. It is just important that the definition is coherent with the color classification of the line detection. To determine the color transformation which would ideally map all the red line colors on the "true" red, the yellow line colors on the "true" yellow we have to find out what the error is. This is dependent obviously on the current environment illumination. So depending on the illumination the yellow of the dashed middle line is more or less "wrong" or away compared to the "true" center.  
The approach is now to determine the so called real centers of the colors of the lines by using a clustering method. In this case it is k-Means.  
We're going to cluster all the pixels of the input image and try to find the red, yellow, white and black cluster. By calculating the center of each of those clusters we are able to compute the color transform.

<center>
<figure>
<img src="distance.svg" alt="kMeans approach" style="width: 250px;"/>
<figcaption> Basic idea of the k-Means transform </figcaption>
</figure>
</center>
We were convinced that a clustering approach is a good solution because of the following points:
1. The clustering and the consequently determined centers lead to a color transformation focusing only on the problem relevant colors.
2. Clustering can be implemented unsupervised
We were convinced that k-Means is a good solution since it is fairly simple to implement.  

We decided to use the RGB space for the clustering approach and therefore as well as the reference space for the transformation described in [the chapter above](#mathematical-general-transform).

The following pictures show how sample images look in different color spaces.  
The far left is the original image where we got the data from. The second from left is the pixel values plotted in RGB space, the third in HSV space and the far right the pixel values in LAB space.

<div>
    <div>
        <img src="original.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
        <img src="rgb.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
        <img src="hsv.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
        <img src="lab.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
        <p style="clear: both;"></p>
    </div>
</div>

<div>
    <div>
        <img src="original2.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
        <img src="rgb2.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
        <img src="hsv2.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>
        <img src="lab2.png" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
        <p style="clear: both;"></p>
    </div>
</div>

One sees that the color clusters of red, yellow, white and black are nicely distinct in the RGB space. So RGB is a good space to do clustering.
As stated in [disadvantages](#disadvantages-existing) we used more than 3 cluster centers. So we tried it with 10 clusters. But now one has the problem that we don't know anymore which cluster is which. That's why we implemented a function which can determine which color is which.

#### Color determination

_Implemented in the determineColor function found in the kmeans_rebuild.py file._  

If we do k-Means in an unsupervised way we don't know in the end which cluster and therefore which center belongs to which color. We made the assumption that the nearest cluster center is of the same color as the nearest true center.  
We thought this assumption is reasonable because looking at some data in the RGB space one sees that if we would want to interchange clusters we need a massive distortion. Such a distortion is in our opinion almost impossible.  
So to determine which cluster belongs to which "true" center we do the following steps:  
1. The output of the k-Means consists of 10 centers. Or the number of centers you put as an input. Now for each "true" center the error to all found center of k-Means is computed.
2. We iterate through the "true" centers and look which determined center has the lowest value. This center would be assigned to the color of the "true" center. If a "true" center would've been assigned already we would take the determined center with the second lowest error.
3. Now we have a list of centers which we know what colors they are.

Using the least squares approach we can fit with these four centers an optimal color transformation.
The very alert fan of Duckietown will already have realized that in this whole color discussion there is one mistake: We don't have always the red stopping line in an image of the camera. There exist sections where you have a simple straight road without any intersections. Therefore you won't find any red color. So we need a solution for that.  
That's where color elimination comes into play.

#### Color elimination

_Implemented in the detectOutlier function found in the outlierEstimation file._  

The use of all four colors red, yellow, white and black can lead to wrong results. You just have to think of a situation where you don't find any red stopping line in the picture.
That's why we came up with the following "color elimination" procedure:
1. Pick three colors out of the four colors and do a least squares fit to find the color transformation.
2. Estimate the error of the least squares fit.
3. Repeat steps 1 and 2 for all color combinations and keep the three colors which give the lowest error. So this least squares fit would be the one without the outlier. So in the case you don't have any red in the image you would just use white, black and yellow since wrong red cluster would distort the color correction.
If there are all the four colors in the picture we observed that most of the time the black cluster is thrown away. This makes quite sense since in the [chapter](#k-means-idea) above we saw that the black center doesn't really fulfill the assumptions for k-Means since the black cluster is quite elliptical shaped.

Something we observed was that sometimes the procedure gave unreasonably high parameters as an output. So we came up with a convex optimization approach.

#### Convex optimization

_Implemented in the calcBoundedTrafo found in the calcLstsqTransform.py file._  


The idea here is to limit the parameter values of the color transform. We observed that for example a scale factor for a channel of 240 is unreasonably high. So we stated the following:
\[ 1/3 \leq k_i \leq 3\]
\[ -100 \leq s_i \leq 100\]
where $k_i$ and $s_i$ are the scale and the shift of each channel.

We used then convex optimization to limit the scale and shift values.

#### Online Approach

_Implemented in the ContAntiInstagramNode found in the cont_anti_instagram_node.py file._  
_This is set with the parameter ai_interval in the ContAntiInstagramNode._

We set the goal for our project to implement an online solution. So we decided to repeat the procedure described before every 30 seconds. This time interval is quite arbitrary and the lower would be the better.

#### Results

All in all the k-Means approach gives good results but it is too slow for an online approach. If we ran the algorithm on the Duckiebot it consumed almost all the processing power and other computational complex functions were limited.


### Histogram Equalization

_Implemented in the simpleColorBalanceClass found in the simpleColorBalanceClass file._
_This is trafomode cb for the ContAntiInstagramNode._

After implementing the k-Means approach we saw that there was need for something else. A very simple white balance would help us a lot to correct the picture to a certain extent and being very fast.

#### Idea

Doing research we found a promising approach for a very simple color balance.  
Actually the analysis in the [disadvatages chapter](#disadvantages-existing) led us to this idea. Experimenting with gimp we found out that the automatic white balace leads to quite good results:  

Example 1:

<div>
      <img src="disad1_original.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
      <img src="disad1_corr_gimp.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
      <p style="clear: both;"></p>
</div>


This was a medium working example. The euclidean error of "true" centers compared to the centers which are estimated in the picture increased from 115.267 to 31.2.

Example 2:

<div>
      <img src="disad2_orig.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;" />
      <img src="disad2_corr_gimp.jpg" style="float: left; width: 23%; margin-right: 1%; margin-bottom: 0.5em;"/>        
      <p style="clear: both;"></p>
</div>


This was a medium working example. The euclidean error of "true" centers compared to the centers which are estimated in the picture increased from 115.267 to 30.35.

This were very promising results comparing to the results of the [disadvatages chapter](#disadvantages-existing).

The idea works as following:  
1. Create a sorted list for every channel of the image.
2. Remove a certain predefined percentage of this list from the top and the bottom. The percentage serves as a parameter for the anti instagram node.
3. After removing the highest and the lowest value of this list serve as the thresholds($Th_{low}$, $Th_{high}$) for the frames afterwards.  
4. Do this for every channel.

So we don't compute any transform anymore. We simply set all the values lower than the low threshold to the lower threshold and the values higher than the high threshold to the high threshold.
This transform is applied as follows:
1. Set all values lower than $Th_{low}$ to $Th_{low}$ and higher than the $Th_{high}$ to $Th_{low}$. Do this for every channel.
2. Normalize the image to [0, 255].


#### Results

This procedure is way faster than k-Means. That's why it is our proposed solution in the end.

## General architecture

<center>
<figure>
<img src="flow2.svg" alt="kMeans approach" style="width: 400px;"/>
<figcaption> General architecture </figcaption>
</figure>
</center>

As seen in the picture the most important piece in our code is the Anti_Instagram node. It has the ability to get a raw image from the camera and calculate transform parameters out of it. So the core piece is the ContAntiInstagramNode.

### Anti Instagram node

Input parameters for the Anti instagram node:
1. _~ai_interval_: This sets the time in seconds between each computation of the color transformation. Default: 10

2. _~fancyGeom_: States what mask should be used to remove the background. If it is set to _false_, just one third from above is cut away to do the color transformation. If it is set to _true_, the flood fill approach is used. [Attention: Very time consuming and not stable results.] Default: false.
3. _~n_centers_: Indicates how many centers for k-Means should be used. Default: 6
4. _~blur_: Indicates what type of blur should be used. Options are _'median'_ or _'gaussian'_. Default: _'median'_
5. _~resize_: Defines by what factor the picture should be resized before computing the transformation. Default: 0.2
6. _~blur_kernel_: Defines the kernel size of the blur. Default: 5
7. _~cb_percentage_: Defines the percentage of data points that should be cut away by the histogram equalization. Default: 2
8. _trafo_mode_: Defines the transformation mode of the color transformation. Options are _'both'_ for histogram equalization first and kMeans after, _'lin'_ for kMeans only and _'cb'_ for histogram equalization only. Default: _'both'_

## Formal performance evaluation / Results

In the end we have to admit that k-Means is probably too time consuming for an online approach. Or at least for an online approach with a fixed interval.
Following you find computational time on the Duckiebot:

| Algorithm:                           | Running Time [s]     |
|----------------------------------    |------------------    |
| Color Balance                        |      0.0054          |
| Linear 2 iterations, 10 centers      |      1.9725          |
| Linear 2 iterations, 6 centers       |      0.6065          |
| Linear 10 iterations, 10 centers     |      4.1626          |
| Linear 10 iterations, 6 centers      |      1.3360          |
| Linear 20 iterations, 10 centers     |      5.1680          |
| Old Anti Instagram                  |      3.1517          |



## Future avenues of development

### Annotated Data

This failed horribly. We didn't manage to get any annotated data since something didn't work with the website.
For further improvement of the algorithm and a proper performance evaluation this would be crucial.

### Remove unwanted background

_Implemented in the geom.py file._

#### Idea

In order to make the k-Means approach faster one could try to remove unwanted background/irrelevant pixels. Since all the information except the road is of no use for the color transformation algorithm it can be remove. Up to now it just consumes more time and makes the algorithm incorrect. So if one could remove the unwanted background we could speed up k-Means because we don't have so many pixels anymore and because probably we don't need this many centers anymore. Since k-Means computational complexity is linear in both parameters this would definitively impact the computational time.

#### Lane Surface Identification

* Prior knowledge:
    * Assumption: Bottom ⅖ is lane, top ⅓ is not lane.
    * Pixels within a lane element have low gradient.
    * Pixels crossing boundaries, i.e. line edges, have high gradient.
* Detailed steps:
    1. Compute gradient

        Compute the image gradient with Sobel operator. The result turns out to be better when done in RGB rather than HSV space.

        <img src="grad.png" style="width: 400px"/>

    2. Threshold gradient

        This makes a binary image out of the gradient.

        <img src="grad_th.png" style="width: 400px"/>
    3. Dilate gradient

        This continues broken lines in the gradient, due to noise (e.g. from motion blur).

        <img src="grad_th_dilated.png" style="width: 400px"/>

    4. Zero fill bottom ⅖

        This part is assumed to be lane surface. See next step for explanation.

        <img src="grad_th_dilated_zeroed.png" style="width: 400px"/>

    5. Floodfill to get mask

        This yield the single connected component of low gradient part. The seed is chosen from the bottom ⅖.

        <img src="ff.png" style="width: 400px"/>

    6. Close narrow openings

        Regions inside narrow openings are probably high gradient part within the lane, and thus should be kept. We close it first, which is equivalent to dilation followed by errosion.

        <img src="ff_closed.png" style="width: 400px"/>

    7. Fill the holes

        Then fill the resulting holes by floodfilling from the top, and take the complement.

        <img src="ff_closed_ff.png" style="width: 400px"/>

    8. Clip off top $\frac{1}{3}$

        This part are assumed to be not lane surface, so it gets clipped off from the mask.

        <img src="ff_closed_ff_clipped.png" style="width: 400px"/>

#### Boundary Region Detection

* Intuitions:
    * We observed that regions of boundaries between lane lines already contain sufficient color information. This is because the line detector only cares about the edges of lane lines, which is the entire reason we are performing anti-instagram.
    * In addition, restricting to boundary areas will further remove irrelevant portions of the image while substantially accelerating k-means computation.
* Detailed steps:
    1. Compute, threshold and dilate gradient

        High gradient part corresponds to boundaries. Dilation is meant to cover more of the bordering pixels to get sufficient information.

        <img src="grad_cnt.png" style="width: 400px"/>

    2. Find contours as masks

        We want to capture the boundary areas, which can be found as contours in the gradient map above. This is done via the algorithm described in Suzuki, S. and Abe, K., Topological Structural Analysis of Digitized Binary Images by Border Following. CVGIP 30 1, pp 32-46 (1985) (implemented in OpenCV).

        <img src="grad_cnt_masked.png" style="width: 400px"/>

    3. Remove small contours and fill in

        Contours that have small size are probably noise. Fill in the holes turn out to provide more information than noise.

        <img src="grad_cnt_masked_th.png" style="width: 400px"/>

        The pixels under this mask then get fed into the k-means algorithm.

#### Existing code

There exists already some code for this idea. The basic concept is to use the flood fill concept. The output would be a mask which can be applied to every picture. But so far the generalization is difficult to make since the road geometry can easily change (e.g. in curves). And secondly this approach is quite time consuming as well.  
A simple workaround is the following:  
In general one can cut away the upper third of the picture to compute the color transform. One only need the road and its color for this procedure. So everything above the road is uninteresting for computing the color transform. The heuristic approach is cutting away the upper third. This is the default approach!

### Two step k-Means

Do the first transformation with n iterations and k centers. Then remember the k centers. For the next $2, \dots, z$ images only start from the previous centers from image $z_{i-1}$ to compute the next centers from image $z_{i}$.  

### Other clustering method

Another clustering method like expectation maximization based on Gaussian mixture models would have more accurate results since some of the color clusters are not really spherical and definitively not of the same size.

### White paper reference

To determine when exactly the moment for the color transformation is a white paper reference would help. So an idea would be to have a small white hardware piece in camera sight which is always exposed to the environment lighting conditions. There you could see when the best moment for a re-computation of a color transformation would be.

### Polarization filter

If you would put a polarization filter in front of the camera we would get rid of the reflections of the tape. This was a big problem we heard of several teams.


### Troubleshooting
Contact: [Christoph Zuidema](mailto:czuidema@ethz.ch)
