# Self_Driving-Car-Lane-Detection-System
# Introduction to Problem
With the rapid development of society, automobiles have become one of the transportation tools for people to travel. In the narrow road, there are more and more vehicles of all kinds. As more and more vehicles are driving on the road, the number of victims of car accidents is increasing every year. How to drive safely under the condition of numerous vehicles and narrow roads has become the focus of attention. Advanced driver assistance systems which include lane departure warning (LDW), Lane Keeping Assist, and Adaptive Cruise Control (ACC) can help people analyse the current driving environment and provide appropriate feedback for safe driving or alert the driver in dangerous circumstances. This kind of auxiliary driving system is expected to become more and more perfect. However, the bottleneck of the development of this system is that the road traffic environment is difficult to predict. After investigation, in the complex traffic environment where vehicles are numerous and speed is too fast, the probability of accidents is much greater than usual. In such a complex traffic situation, road colour extraction and texture detection as well as road boundary and lane marking are the main perceptual clues of human driving.
Lane detection is a hot topic in the field of machine learning and computer vision and has been applied in intelligent vehicle systems. The lane detection system comes from lane markers in a complex environment and is used to estimate the vehicle’s position and trajectory relative to the lane reliably. At the same time, lane detection plays an important role in the lane departure warning system. 
# Proposed Solution
To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using frame masking. The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we simply update those pixel values to 0 in the NumPy array.
After making we need to detect lane lines. The technique used to detect mathematical shapes like this is called Hough Transform. Hough transformation can detect shapes like rectangles, circles, triangles, and lines.

# Requirements
## Technology Stack – 

Software Configuration 
These are the Software Configurations that are required.
•    Operating System: Windows 10/8/7 (incl. 64-bit), Mac OS, Linux 
•	Language: Python 3
•	Libraries: OpenCv, Numpy, Matplotlib, Pandas, OS
•    IDE: Jupyter Notebook/ Spyder 3
•    Framework: Tkinter / Streamlit


