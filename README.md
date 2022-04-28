# Self_Driving Car Lane Detection System
# Introduction to Problem
With the rapid development of society, automobiles have become one of the transportation tools for people to travel. In the narrow road, there are more and more vehicles of all kinds. As more and more vehicles are driving on the road, the number of victims of car accidents is increasing every year. How to drive safely under the condition of numerous vehicles and narrow roads has become the focus of attention. Advanced driver assistance systems which include lane departure warning (LDW), Lane Keeping Assist, and Adaptive Cruise Control (ACC) can help people analyse the current driving environment and provide appropriate feedback for safe driving or alert the driver in dangerous circumstances. This kind of auxiliary driving system is expected to become more and more perfect. However, the bottleneck of the development of this system is that the road traffic environment is difficult to predict. After investigation, in the complex traffic environment where vehicles are numerous and speed is too fast, the probability of accidents is much greater than usual. In such a complex traffic situation, road colour extraction and texture detection as well as road boundary and lane marking are the main perceptual clues of human driving.
Lane detection is a hot topic in the field of machine learning and computer vision and has been applied in intelligent vehicle systems. The lane detection system comes from lane markers in a complex environment and is used to estimate the vehicle’s position and trajectory relative to the lane reliably. At the same time, lane detection plays an important role in the lane departure warning system. 
# Proposed Solution
To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using frame masking. The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we simply update those pixel values to 0 in the NumPy array.
After making we need to detect lane lines. The technique used to detect mathematical shapes like this is called Hough Transform. Hough transformation can detect shapes like rectangles, circles, triangles, and lines.

# Requirements
## Technology Stack – 

#### Software Configuration 
These are the Software Configurations that are required.
•    Operating System: Windows 10/8/7 (incl. 64-bit), Mac OS, Linux 
•	Language: Python 3
•	Libraries: OpenCv, Numpy, Matplotlib, Pandas, OS
•    IDE: Jupyter Notebook/ Spyder 3
•    Framework: Tkinter / Streamlit

 #### Hardware Configuration 
These are minimum Hardware configurations that are required. 
•    Processor: Intel core 2 duo or higher. 
•    RAM: 2 GB or higher 
•    HDD: 256 GB or higher
•    Monitor: 1024 x 768 minimum screen resolution. 
•    Keyboard: US en Standard Keyboard.
## User Requirements
Since this an autonomous self-driving car, the user does not directly interact with the car. Rather, the car may have some in-dash computer system, like those found in modern day cars.
The in-dash systems, apart from providing entertainment features and vital information like speed and engine RPM, provide navigation aids like GPS as well. They, thus, act as an interface between the user and the car. Such in-dash systems and modifications required for them to work with our system, however, are beyond the scope of this project.

# Project Scope
This model can be updated and tuned with more efficient mathematical modelling, whereas the classical OpenCV approach is limited and no upgrade is possible as the approach is not efficient It is unable to give accurate results on the roads which do not have clear markings present on the roads. Also it cannot work for all climatic conditions This technology is increasing the number of applications such as traffic control, traffic monitoring, traffic flow, security etc. 

# Conclusion 
In this project, we proposed a new lane detection pre-processing and ROI selection methods to design a lane detection system. The main idea is to add white extraction before the conventional basic pre-processing. Edge extraction has also been added during the pre-processing stage to improve lane detection accuracy. We also placed the ROI selection after the proposed pre-processing. Compared with selecting the ROI in the original image, it reduced the nonlane parameters and improved the accuracy of lane detection. Currently, we only use the Hough transform to detect straight lane and EKF to track lane and do not develop advanced lane detection methods. In the future, we will exploit a more advanced lane detection approach to improve the performance.



