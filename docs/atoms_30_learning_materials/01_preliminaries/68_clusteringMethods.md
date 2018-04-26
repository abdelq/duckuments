# Clustering methods {#preliminaries-clustering-methods status=draft}
Clustering is the process of grouping some objects such that similar objects belong to the same group. In the sense of colors it could be that similar colors are grouped together e.g. bright red, ruby and pink belong to the group of red colors where as azure blue, copenhagen blue and dark blue would be grouped to the blue colors.  
Various algorithm can solve such a task. They differ in how they define what is a cluster (e.g. the members are within a certain distance) and how efficiently these algorithms can find these clusters.  
Following some algorithms for determining clusters are presented.

## k-Means clustering

### Description of the algorithm

Let's assume we have $d$ data points $x_{1,...,d}$ and $k$ cluster centers $m_{1,...,k}$. Now the algorithm tries to put the centers such that optimally all the clusters existing in the data are found. A data point $x_i$ belongs to the cluster $j$ if the cluster center $m_j$  is the nearest among all the clusters $m_{1,..,k}$.  

So the algorithm can be described as follows:  

1. Define a number k (number of cluster centers), initialize $m_{1,...,k}$, for example randomly.
2. Determine for every data point $x_i$ the nearest cluster center $m_j$. Assign this data point to the cluster $j$.
3. Recompute the cluster centers $m_{1,...,k}$ by finding the mean of all data points assigned to the cluster $j \in 1, ..., k$.
4. Repeat step 2 and 3 until convergence. Often a certain tolerance is used such that the algorithm stops until the difference between the iterations is smaller than the tolerance. Another way to stop the algorithm is to set a maximum number of iterations beforehand.  

<center>
<figure>
<img src="kmeans_working.png" alt="kMeans working" style="width: 500px;"/>
<figcaption> Example of a k-Means clustering [1] </figcaption>
</figure>
</center>

[ (source) ](http://blog.mpacula.com/2011/04/27/k-means-clustering-example-python/)

### Advantages and Limits

#### Advantages

- Simple clustering method compared to other clustering methods.
- Unsupervised learning is possible. One doesn't need any labeled data to perform a cluster analysis. Back to the color example from the introduction: The k-Means algorithm doesn't know about the colors. The algorithm only knows that the data points are near each other in RGB-space for example and therefore assigns them to the same cluster.

#### Limits

- There is no guarantee that k-Means converges to a global optimum. It depends on the initialization of the cluster centers in the beginning. Converging to local minima can lead to counter intuitive/"wrong" results.
- Computationally difficult: K-Means is in general NP-hard. The complexity scales with the number of data points $n$, centers $k$, iterations $i$, and attributes $a$ of each data point. (In the color example we have only one attribute. But it could be that there exist data points which have several attributes e.g. temperature, humidity, ...). So the complexity is in order of $n \cdot k \cdot i \cdot a$. But in the worst case the complexity can reach super polynomial behavior.
- Clusters are expected to have similar size and spherical shape since k-Means decides whether a data point lies within a cluster based on the Euclidean distance.

(*Hartigan, J. A.; Wong, M. A. (1979). "Algorithm AS 136: A K-Means Clustering Algorithm". Journal of the Royal Statistical Society. Series C (Applied Statistics). 28 (1): 100–108.*)

TODO: add bibtex for entry above

<center>
<figure>
<img src="kmeans_notworking.png" alt="kMeans working" style="width: 500px;"/>
<figcaption> Different examples of a k-Means clustering which are not working. </figcaption>
</figure>
</center>

[ [source] ](http://scikit-learn.org/stable/modules/clustering.html#k-means)

## Gaussian mixture models
We've seen above several drawbacks of k-Means clustering. That's why there is motivation to search for something better.
### Idea
Simply speaking Gaussian mixture models are a more general version of k-Means assuming we have k components. This means we fit to each cluster a Gaussian distribution. The underlying assumption is that every data point is generated through a mixture of Gaussian distributions. Their parameters are unknown and are determined through the algorithm.

### Algorithm
1. Initialize $n$ Gaussian mixture components with zero mean and identity covariance. (Often a diagonal covariance matrix is used.)
2. E-step: for each point, estimate the probability that each Gaussian generated it.
3.  M-step: modify the parameters according to the hidden variable to maximize the likelihood of the data.
4. Repeat step 2 and 3 (expectation-maximation [EM]) until average gain in log-likelihood is below this threshold.

### Advantages and Disadvantages

#### Positives
- Does not have any underlying assumption of structure in the data. Compared to k-Means this is a clear advantage. Gaussian mixture models can handle elliptical data for example. The same counts for the size of the cluster.

#### Negatives
- Difficult to interpret since a data point can belong to a certain degree to several clusters since affiliation is probabilistic.
- Complexity: The theoretical complexity of the GMM approach is similar as k-Means. So it results in $n \cdot k \cdot i$ for the number of data points $n$, centers $k$ and iterations $i$.
- Difficulties for high dimensional data.

<center>
<figure>
<img src="kmeans_vs_gmm.png" alt="kMeans working" style="width: 700px;"/>
<figcaption> K-Means in comparison with EM algorithm </figcaption>
</figure>
</center>

[ [source] ](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/ClusterAnalysis_Mouse.svg/450px-ClusterAnalysis_Mouse.svg.png)
