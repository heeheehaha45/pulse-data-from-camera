# pulse-data-from-camera
 Detecting one’s health status with analysis of blood flow captured from a normal video camera
---------------------------
Special thanks for the work of Tristan Hearn, as I got a lot inspired from his work:
https://github.com/thearn/webcam-pulse-detector

The lib folder and get_pulse.py in this repo is mainly from his work, I fixed some bug and add some function based on his work.

--------------------------

As blood flow under skin reflects one’s health status, my research is about detecting one’s health status with analysis of blood flow captured from a normal video camera. 
Rather than just estimating the heart beat, the data captured is a 2-D image video which is amplified to visualize the blood flow of the whole body. The video is then feed to a CNN for analysing the health status of the user.

![alt text](https://github.com/kekileong/pulse-data-from-camera/blob/master/New%20Project%20(5).png)

This repo will focus showing the result of processing the raw video frames in order to visualize the impact of blood flow.

--Look at the change of every pixel in the whole image--

I intended to investigate the change of every pixel value of the green channel in the whole image over time, and amplify the result so the change of blood flow in different parts of the arm can be seen from human eye. In order to do this, I take a series of frames from the webcam, chop the interested part(remove the background and other objects in the desk, only the arm is left), extract the green channel (researches has shown that green channel is the most sensitive to blood change on skin), and apply the formula to each pixel to “normalize” each pixel in order to amplify the change.

img[x][y][1] =int( 255*(img[x][y][1]-mini)/(maxi-mini) )

where maxi is the maximum pixel value(lightest) of the frames over time, and mini is the darkest pixel.	

![alt text](https://github.com/kekileong/pulse-data-from-camera/blob/master/2.png)



Result:
We can see the result images from output_after_process zip file. If you play the images, you can see there is a ‘wave’ of change along the arm.

Newest Result:
After applying median blur to the resulting image, it has a better visual effect:

![alt text](https://media.giphy.com/media/MeDoEBeZUgEqJUKt79/giphy.gif)

If you find it hard to observe, it would be clearer for enlarging the image:
https://giphy.com/gifs/MeDoEBeZUgEqJUKt79/fullscreen

Result of using different transfomrations is uploaded in result_of_various_methods.zip. Some of them may have better visual effect.

