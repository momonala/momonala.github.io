# Mohit Nalavadi 

project portfolio 

-------------------------------------------------------------------------------------

### Skillset: 

| Advanced   | Proficent  |  Actively Learning 
|------------|------------|--------------------
| Python 3.5 | Tensorflow | C++
| Data Science | Teaching myself new Python libs         | SLAM
| OpenCV     | Arduino      | ROS
| Sklearn    | NLP
| Keras      | MATLAB 
| Biosensors | RNNs/LSTMs
| ML/CNNs

-------------------------------------------------------------------------------------

- Click the project links to view code, documentation & in-depth write ups 

### [Laneline & Vehicle Detection for Autonomous Cars](https://github.com/momonala/udacity_carND_term1/tree/master/project5_vehicle_detection)

<img src="https://raw.githubusercontent.com/momonala/udacity_carND/master/project5_vehicle_detection/images/final_out.png" width="600" alt="raw" />

- This project was the capstone for Term 1 of Udacity's Self Driving Car Nanodegree  
     - https://www.youtube.com/watch?v=k5xHKRoW5VY
- Laneline Detection Pipeline:
   - Camera Calibration 
   - Perspecitve Warp
   - Sliding Window to detect lanes using trigonometry 
   - Calculates instantenous turning radius and centerlane deviation 
   - False Detection filters 
- Vehicle Detection with Machine Learning Pipeline:  
   - curated & augmented my own dataset 
   - used sklearn and Keras to build an ensemble classifier 
   - extracted color channel and HOG features 
   - PCA dimensionality reduction 
   - False detection filters
   
#### Additional projects from Udacity SDC Nanodegree Term 1 include: 

- [Traffic Sign Detection ](https://github.com/momonala/udacity_carND/tree/master/project2_traffic_sign_classifier)
    - Convolutional Neural Net built in Tensorflow   
    
<img src="https://raw.githubusercontent.com/momonala/udacity_carND/master/project2_traffic_sign_classifier/images/chart.png" width="500" alt="raw" />

- [Behavioral Cloning Neural Net](https://github.com/momonala/udacity_carND/tree/master/project3_behavioral_cloning)

    - Built a Convolutional Net in Keras to predict steering angles for lane images 
    - Curated & augmented my own dataset
    - Tested on a driving simulator 
    - Implemented code from NVIDIA's research paper on End-To-End Learning 
    
<img src="https://raw.githubusercontent.com/momonala/udacity_carND/master/project3_behavioral_cloning/images/bc_cap.png" width="400" alt="raw" />

--------------------------------------------------------------------------------------------------------

### [Cell Colony Counting](https://github.com/momonala/imaging_and_vision/tree/master/cell_counting) 

- I was tasked to update the vision algorithms for a synthetic biology company, Amyris 
- I built a Python application to count colonies on 96 Agar wellplate
- Vast improvment over original shipped software 
    - 95% of cells were counted, compared to 70% on the original software
    - I built methods for automated cell selection based on size and separation criteria 
    - Integrated seamlessly with the existing hardware 
- Used Hough Lines Circle method in OpenCV 

<img src="https://raw.githubusercontent.com/momonala/imaging_and_vision/master/cell_counting/img/disp.png" width="900" alt="raw" />

----------------------------------------------------------------------------------------------------------
### [Insula (V.1)](https://github.com/momonala/Insula-V2)

- Insula creates music in realtime from physiological biosignals 
- My Senior Thesis Project, built in a team of four 
    - I was responsible for developing the sensors and firmware for biosignal processing 
    - We won 1st prize for the Interdisciplinary Section of the SCU Thesis Conference 
- Used 4 Biosensors: EEG (brainwaves), EMG (muscle contractions), ECG (heart rate), and breath rate
    - each of these inputs translated into a muscal output ex. musical tension, chords, tempo 

[<img src="https://raw.githubusercontent.com/momonala/Insula-V2/master/documentation/youtubev1.png" width="400" alt="raw" />](https://www.youtube.com/watch?v=mQc6FYXu02Q&feature=youtu.be "test")
    
### [Insula (V.2)](https://github.com/momonala/Insula-V2)

- As a solo project I created a haptic glove to create music from hand gestures 
- Custom built hardware, firmware, software 

[<img src="https://raw.githubusercontent.com/momonala/Insula-V2/master/documentation/youtube.png" width="500" alt="raw" />](https://www.youtube.com/watch?v=Azrm98Bf4nk "test")

-----------------------------------------------------------------------------------------------------------

### [Quantitative Finance](https://github.com/momonala/quantitative_finance)

- Built a novel algorithm using Bollinger Bars to predict stock prices 
- Used regression and probablistic thresholds to identify ideal entry/exit positions of any given stock 
- Extensive use of pandas, numpy, gridsearch, time series, and other data science tools 
- Project landed me a 3rd round interview at quant company, Quantopian, despite having no finance background 

<img src="https://raw.githubusercontent.com/momonala/quantitative_finance/master/files/z_example.png" width="800" alt="raw" />

----------------------------------------------------------------------------------------------------------

### [Optical Heart-Rate Detection Via Webcam](https://github.com/momonala/optical_heart_rate)

- real-time computer vision to measure heart-rate from changes in optical intensity via a webcam. 
- Implementation of MIT paper 
- Tools used: 
    - openCV 
    - scipy fourier transform, detrend, 
    - sklearn Independent Component Analysis (FastICA)
    - heavy use of mixed-signal engineering concepts 

----------------------------------------------------------------------------------------------------------

### [Biobots Website and Data Science](https://github.com/momonala/biobots)

- This was my technical interview for a software engineering role at bioprinting company, Biobots 
- I built a web dashboard in a weekend
    - Flask backend 
    - no previous experience in Javascript, CSS
        - shows my resilience to get a job done and ability to learn quickly & efficiently 
    - Display manager for user's data 
- Also included a data science approach to analyze the given dataset 

------------------------------------------------------------------------------------------------------------

### [Data Science Tutorials](https://github.com/momonala/DS_tutorials)

- I was a Data Science Associate Instructor at General Assembly SF 
- I created tutorials on problem subjects which students requested 
    - QQ Plots 
    - Regularization 
    - Time Series (taught this lecture) 
    - P-Value vs. T-Value 
    - Regression 