#  The Duckietown project {#part:duckietown-project}

# What is Duckietown? {#what-is-duckietown status=beta}

## Goals and objectives

Duckietown is a robotics education and outreach effort.

The most tangible goal of the project is to provide a low-cost educational platform for learning about autonomous systems, consisting of lectures and other learning material, the Duckiebot autonomous robots, and the Duckietowns, which constitute the infrastructure in which the Duckiebots navigate.

We focus on the *learning experience* as a whole, by providing a set of modules, teaching plans, and other guides, as well as a curated role-play experience.

We have two targets:

1. For **instructors**, we want to create a "class-in-a-box" that allows people to offer a modern and engaging learning experience. Currently, this is feasible at the advanced undergraduate and graduate level, though in the future we would like to provide a platform that can be adapted to a range of different grade and experience levels.

2. For **self-guided learners**, we want to create a "self-learning experience" that allows students to go from having zero knowledge of robotics to a graduate-level understanding.

In addition, the Duckietown platform is also suitable for research.

<!-- TODO: add references to papers submitted/published with it. -->

<!-- Duckietown has been recently incorporated as a non-profit foundation. -->

## Learn about the Duckietown educational experience

The video in [](#fig:duckumentary) is the "Duckumentary", a documentary about the first version
of the class, during Spring 2016.


<div figure-id="fig:duckumentary">
    <figcaption>The Duckumentary, created by <a href="https://www.facebook.com/ChrisWelchPhotography/">Chris Welch.</a>
    </figcaption>
    <dtvideo src='vimeo:231688769'/>
</div>

The video in [](#fig:road-to-autonomy) is a documentary created by Red Hat
on the current developments in self-driving cars.

<div figure-id="fig:road-to-autonomy">
    <figcaption>The road to autonomy</figcaption>
    <dtvideo src="vimeo:219731087"/>
</div>


If you'd like to know more about the educational experience, [](#bib:tani16duckietown) present
a more formal description of the course design for Duckietown: learning objectives, teaching
methods, etc.


## Learn about the platform

<!-- The best way to get a sense of how the platform looks is to watch
these videos. They show off the capabilities of the platform. -->

The video in [](#fig:v3) shows some of the functionality of the platform.

If you would like to know more, the paper [](#bib:paull17duckietown) describes the Duckiebot
and its software. (With 30 authors, we made the record for a robotics conference!)

<div figure-id="fig:v3">
    <figcaption>Duckietown functionality</figcaption>
    <dtvideo src="vimeo:231843373"/>
</div>



<cite class='pub-ref-desc' id='bib:tani16duckietown'>
    <span class="author"><a href='https://eapsweb.mit.edu/people/jtani'>Jacopo Tani</a>, <a href='http://people.csail.mit.edu/lpaull/'>Liam Paull</a>, <a href='https://eapsweb.mit.edu/people/zuber/'>Maria Zuber</a>, <a href='http://danielarus.csail.mit.edu/'>Daniela Rus</a>, <a href='http://www.mit.edu/~jhow/'>Jonathan How</a>, <a href='https://marinerobotics.mit.edu/'>John Leonard</a>, and <span class="author-ac">Andrea Censi</span>.</span>
    <span class="title">Duckietown: an innovative way to teach autonomy.</span>
    <span class="booktitle">In <em>EduRobotics 2016</em>. Athens, Greece, December 2016.</span>
    <span class="links"><span class="pdf"><a href="http://people.csail.mit.edu/lpaull/publications/Tani_EDU_2016.pdf"><img style='border:0; margin-bottom:-6px; height: 17px'  src='pdf.png'/> pdf</a></span><span class="url"><a href="http://duckietown.mit.edu/"><img style='border:0; margin-bottom:-6px; height: 17px'  src='web.png'/> supp. material</a></span></span><a class='pub-ref-bibtex-link' onclick='javascript:document.getElementById("tani16duckietown").style.display="block";' href='javascript:void(0)'>bibtex</a><pre class='pub-ref-bibtex' id='tani16duckietown' style='display: none;'>@inproceedings{tani16duckietown,
        author = "Tani, Jacopo and Paull, Liam and Zuber, Maria and Rus, Daniela and How, Jonathan and Leonard, John and Censi, Andrea",
        title = "Duckietown: an Innovative Way to Teach Autonomy",
        url = "http://duckietown.mit.edu/",
        booktitle = "EduRobotics 2016",
        year = "2016",
        month = "December",
        address = "Athens, Greece",
        pdf = "http://people.csail.mit.edu/lpaull/publications/Tani_EDU_2016.pdf"
    }</pre>
</cite>







<style>
img.icon {
    float: left;
    width: 5em;
    margin: 0.5em;
}
.pub-ref-desc {  }
.pub-ref-short { width: 100%;
    /*font-size: smaller;*/
}
.pub-ref-desc .title {
    font-weight: bold;
}
.pdf, .url { margin-left: 3px;}
.url { display: none;}

.pub-ref-bibtex-link  { margin-left: 3px; }
@media print {
    .pub-ref-bibtex-link { display: none; }
}
</style>

<cite class='pub-ref-desc' id='bib:paull17duckietown'>
    <span class="author"><a href='http://people.csail.mit.edu/lpaull/'>Liam Paull</a>, <a href='https://eapsweb.mit.edu/people/jtani'>Jacopo Tani</a>, Heejin Ahn, Javier Alonso-Mora, Luca Carlone, Michal Cap, Yu Fan Chen, Changhyun Choi, Jeff Dusek, Daniel Hoehener, Shih-Yuan Liu, Michael Novitzky, Igor Franzoni Okuyama, Jason Pazis, Guy Rosman, Valerio Varricchio, Hsueh-Cheng Wang, Dmitry Yershov, Hang Zhao, Michael Benjamin, <a href='http://web.mit.edu/chrisc/www/Home.html'>Christopher Carr</a>, <a href='https://eapsweb.mit.edu/people/zuber/'>Maria Zuber</a>, <a href='http://karaman.mit.edu/'>Sertac Karaman</a>, <a href='http://ares.lids.mit.edu/'>Emilio Frazzoli</a>, <a href='http://www.mit.edu/~ddv/'>Domitilla Del Vecchio</a>, <a href='http://danielarus.csail.mit.edu/'>Daniela Rus</a>, <a href='http://www.mit.edu/~jhow/'>Jonathan How</a>, <a href='https://marinerobotics.mit.edu/'>John Leonard</a>, and <span class="author-ac">Andrea Censi</span>.</span>
    <span class="title">Duckietown: an open, inexpensive and flexible platform for autonomy education and research.</span>
    <span class="booktitle">In <em>IEEE International Conference on Robotics and Automation (ICRA)</em>. Singapore, May 2017.</span>
    <span class="links"><span class="pdf"><a href="http://people.csail.mit.edu/lpaull/publications/Paull_ICRA_2017.pdf"><img style='border:0; margin-bottom:-6px; height: 17px'  src='pdf.png'/> pdf</a></span><span class="url"><a href="http://duckietown.mit.edu/"><img style='border:0; margin-bottom:-6px; height: 17px'  src='web.png'/> supp. material</a></span></span><a class='pub-ref-bibtex-link' onclick='javascript:document.getElementById("paull17duckietown").style.display="block";' href='javascript:void(0)'>bibtex</a><pre class='pub-ref-bibtex' id='paull17duckietown' style='display: none;'>@inproceedings{paull17duckietown,
        author = "Paull, Liam and Tani, Jacopo and Ahn, Heejin and Alonso-Mora, Javier and Carlone, Luca and Cap, Michal and Chen, Yu Fan and Choi, Changhyun and Dusek, Jeff and Hoehener, Daniel and Liu, Shih-Yuan and Novitzky, Michael and Okuyama, Igor Franzoni and Pazis, Jason and Rosman, Guy and Varricchio, Valerio and Wang, Hsueh-Cheng and Yershov, Dmitry and Zhao, Hang and Benjamin, Michael and Carr, Christopher and Zuber, Maria and Karaman, Sertac and Frazzoli, Emilio and Vecchio, Domitilla Del and Rus, Daniela and How, Jonathan and Leonard, John and Censi, Andrea",
        title = "Duckietown: an Open, Inexpensive and Flexible Platform for Autonomy Education and Research",
        url = "http://duckietown.mit.edu/",
        booktitle = "IEEE International Conference on Robotics and Automation (ICRA)",
        year = "2017",
        month = "May",
        address = "Singapore",
        pdf = "http://people.csail.mit.edu/lpaull/publications/Paull_ICRA_2017.pdf"
    }</pre>
</cite>
