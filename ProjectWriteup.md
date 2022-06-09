# WriteUp Object -- Detection in an Urban Environment

## Project overview

In the project I managed to use many skills/Python API functions studied from the previous lessons. The aim of this project is to detect traffic relevant objects in an urban environment.

## Set up

At the very beginning, each data anlyst has to explore the dataset carefully. This is the most important part of evert machine learning project. Hence, the first task is to add the code in the `Exploratory Data Analysis` jupyter notebook and run them with our dataset. Thus, we are able to explore the dataset used for training, validation (to see if the split is reasonable, naja, the split in the current project seems to be not necessary). After that we have to modify the config files to specify the parameters for the trainning. The most imporant things are 1. the batch size. 2 step size. I noticed that some template files from workspace is not the same as those from gitlab [this repository](https://github.com/udacity/nd013-c1-vision-starter). There are two at least two critical differences. (a). the step size in the repo of github, is 10 times as those in the workspace. (b) the `Explore Augmentations` jupyter notebook in workspace is not accessible, but the one from github is correct. 

## Data Set

In the `Exploratory Data Analysis` jupyter notebook I performed some statistical analysis for the dataset. However, since the seaborn seems to be not available in this workspace (a little weird), I was not able plot them in the online-notebook. But it is easy to see that the most part of the to be detected object is vehicles, followed by pedestrians and cyclists. (e.g. cars: 345886, pedestrians: 97378, cyclists: 2489)

## Training

Within the online-workspace, the most important thing is in the shortest time to get a converged result, I reset the batch size to 8, so that the loss function decreases much more quickly than the default value (batch_size = 2). It is worth to mention that we (who use the online workspace) must use the original template for pipepline.config, where the total_step_size is 2500. With this parameter, the training can stagnate within 2-3 hours. It is acceptable. Otherwise it lasts too long, and we can even not leave our online-workspace alone and we must keep it as an active session. Honestly, it is a kind of wasting time. Hence, I suggest that we can introduce some modules like tmux or screen: to be able to train a complex model in a detached mode, if necessaray (e.g. for projects that needs hours-long time). Other improvement I did is to use augmentation skills, the paramters for those are contained pipeline.config and for visualization the effect, it can be found in the `Explore Augmentations` jupyter notebook. The best values for the specification are different from project to prject, we must try it iteratively.

