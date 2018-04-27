# Histogram Equalization {#preliminaries-histogram-equalization status=draft}
This text will talk about histograms used for image analysis.
## Motivation
Histogram Equalization can be used for contrast adjustment. For example when a gray scale picture has all values around one value the contrast mathematical difference between different pixels is in general really low. But with histogram equalization the colors are kind of normalized such that the difference and the therefore the contrast of a gray scale picture is increased.
## Histogram
 We'll assume in the following 8-bit values for every data point in a picture.
One can create histogram by counting the number of values for each appearance of intensity in a channel. Such a histogram has bin size 1.
So for a one channel picture (gray scale) we have different gray types between 0 and 255 (8-bit image).
A RGB picture would have for every channel such a histogram.
## Description of the Equalization
### Problem description
So let's assume we'll take a picture of a scene lightened with a perfect red light source.
If we have a look at the red channel of the picture we would see a peak somewhere (potentially towards the higher values) in the histogram.
Since through the red light every pixel is distorted by a certain added red light and the camera most probably overexposes for the red channel we'll end up with a peak in the red channel.

<center>
<figure>
<img src="histogram1.png" alt="kMeans working" style="width: 350px;"/>
<figcaption> Distorted histogram </figcaption>
</figure>
</center>

[ [source] ](https://en.wikipedia.org/wiki/Histogram_equalization)

So if we want to fix that problem we could equalize this histogram.

### Algorithm

The optimal idea is illustrated in the following picture:
<center>
<figure>
<img src="histogramequalization.png" alt="kMeans working" style="width: 250px;"/>
<figcaption> Basic idea </figcaption>
</figure>
</center>

[ [source] ](https://en.wikipedia.org/wiki/Histogram_equalization)

To get to this flat shaped histogram one can follow the algorithm described here:
1. Create a normalized histogram consisting probabilities $p_i$ where $i = 1,..., 255$ for a 8-bit image. The histogram describes how probable a certain value in the channel is: $p_i = \frac{\text{number of pixels with intensity n}}{\text{total number of pixels}}$.
2. Using that histogram one can equalize a picture by converting each pixel value $g_{i,j}$ of the picture with the following formula $g_{i,j} = \text{floor}((L-1) \cdot \sum_{n=0}^{f_{i,j}} p_n )$. With this procedure the histogram will be flattened as seen in the following picture.

[ [source] ](https://www.math.uci.edu/icamp/courses/math77c/demos/hist_eq.pdf)

<center>
<figure>
<img src="histogram2.png" alt="kMeans working" style="width: 350px;"/>
<figcaption> Equalized histogram </figcaption>
</figure>
</center>

[ [source] ](https://en.wikipedia.org/wiki/Histogram_equalization)
## Limits of the algorithm

Histogram equalization is rather unproblematic in single channel images like gray scale. But if one has three color channels the problem is that histogram equalization changes the relative distributions of the channels.  
This can lead to unexpected and unwanted behavior.  
A good idea to solve this problem is to use for example HSL instead of RGB space since you could equalize only luminance there. This would not change any hue or saturation value and provide a good white balance. HSV or LAB could be considered as well.

[ [source] ](http://ieeexplore.ieee.org/document/1257395/?reload=true&amp;arnumber=1257395)
