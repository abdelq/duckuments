# Transfer Learning in Robotics {#transfer-learning status=ready}

TODO: JT: move file to appropriate location / rename


<div class='requirements' markdown='1'>

Results: Understanding transfer learning and the domain randomization technique for transfer learning.

</div>

This unit introduces the concept of Transfer Learning and how it can be applied to Robotics.


## Transfer Learning Definition 

Transfer learning is a subfield of machine learning that focuses on using knowledge gained while solving one problem to solve a related problem.

## Why is transfer learning important in autonomous driving (or duckietown)

A known problem for autonomous driving (in real world or duckietown) is the lack of data. Today, the most successful methods use a form of machine learning called deep learning. Deep Learning is extremely powerful but is known to require a large amount of data to achieve good performance. However, it is time intensive and expensive to collect labeled data on a real system. Additionally, in reinforcement learning, the agent learns by trial and error, which can lead to large safety concerns for the vehicle and the people around it.

A solution to the data problem is to build a simulator, in which we can safely collect data and train deep learning systems. However there is a discrepancy between simulation and reality because the simulator does not perfectly model the world. So, we need transfer learning techniques to utilize models trained in simulation on real systems.

## Transfer Learning in duckietown

In our case, the simulator has clean background and rooftop, but real duckietown has cluttered background. And also, the texture of the road are not exactly the same as duckitown, and there’s no illumination changes in the simulator. However the lane width, camera setting are similar. Additionally, the dynamics in the simulation will not directly match the real Duckietown.

<div figure-id="fig:sim_vs_real" figure-class="flow-subfigures" figure-caption="Simulator images and real images">
    <div figure-id="subfig:sim" figure-caption="Simulator image">
        <img src="sim_img.png" style='width: 20em; height: auto'/>
    </div>
    <div figure-id="subfig:real-image" figure-caption="Real Image">
        <img src="real_img.png" style='width: 20em; height: auto'/>
    </div>
</div>

Need to have images with the correct filename in the folder

### Domain randomization

Domain randomization is a common technique to enable transfer from simulation to the real world. The idea is to continually randomize the dynamics and look of the simulator. The intuition behind this idea is simple: the real world is going to look and act unlike the simulator, so we should force our policy to be robust to these factors. For example, let’s imagine we wanted to train a policy to control the duckiebot directly from images. As long as you can determine the location of the lane lines, the exact look of the environment is unnecessary for the task. However, it is easy for the model trained in simulation to rely on the exact look of the simulation, making it useless in Duckietown. By forcing the policy to be robust to the lighting, coloring, and textures specific to the simulator, it will focus on details such as the position and shape of objects, which are equivalent to that in Duckietown. A policy which only relies on this information will then work when deployed in Duckietown.

<div figure-id="fig:domain_random" figure-class="flow-subfigures" figure-caption="Simulators after domain randomization">
    <div figure-id="subfig:dom_rdm" figure-caption="">
        <img src="domain_random.png" style='width: 30em; height: auto'/>
    </div>
</div>

### Specific task to transfer
Here we have a simple example of training neural network for pose estimation using transfer learning. We replace the pose estimation module in current lane following package with the trained network.

The network takes the camera image as input, and outputs pose d and theta. (d and theta are the angle with respect to the front and )

### Training pipelines:

Collect images by placing duckiebot in the simulator with different poses (The poses are recorded and later used to train the model).
Train the neural network on simulator images. Each image is augmented differently by domain randomization technique during training. We use a CNN which contains 5 convolution layers and 2 fully connected layer. We use mean square error and use Adam to do optimization.
Finetune on real images. (We collected by driving the bot around the duckiebot, and manually label the d and theta by bare eyes)
Deploy on real bots.

### Reference.
https://arxiv.org/pdf/1703.06907.pdf
