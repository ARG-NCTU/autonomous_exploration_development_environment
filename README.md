# How to run this repo with our robot (Husky_UR5) in gazebo

## Clone repo

Clone this repo to run tare algorithm.

```
git clone git@github.com:ARG-NCTU/autonomous_exploration_development_environment.git
```

## Set up the Docker 

The all required environment was organized, only need laptop or computer with GPU, and make sure install docker already.

1. Docker Run

    Run this script to pull docker image to your workstation.

    ```
    source docker_run.sh
    ```
2. Docker Join

    If want to enter same docker image, type below command.

    ```
    source docker_join.sh
    ```
3. Catkin_make

    Execute compile script in the first time, then the other can ignore this step.
    ```
    catkin_make
    ``` 

4. setup environment

    Make sure run this command when the terminal enter docker. 
    ```
    source environment.sh
    ```

## Download map

Run the script to download experiment map.

```
python3 download_map.py
```
