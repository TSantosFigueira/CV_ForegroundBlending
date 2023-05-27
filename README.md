# Foreground Blending
It takes two videos (of the same size) as parameters and removes the green screen of the foreground video to include the background video.

The code is avaliable on 'background_blending.py'. The video files in the root of the project are videos that illustrate the foreground video without the green screen and the final video, respectively. Since the script uses the cv2.addWeighted method, both videos must have the same size (width * height).

You can use the CLI passing as parameters -r to indicate the foreground video (this video must have a green screen background) and -b to provide the path of the background video.


![Captura de tela 2023-05-27 131529](https://github.com/TSantosFigueira/CV_ForegroundBlending/assets/8387776/ac8012ae-734d-47e3-a8c5-d1b07e394729)
Plus
![Captura de tela 2023-05-27 132306](https://github.com/TSantosFigueira/CV_ForegroundBlending/assets/8387776/6d20dee2-d312-43f5-8c14-f8f40e3f352c)
Results in 
![Captura de tela 2023-05-27 132342](https://github.com/TSantosFigueira/CV_ForegroundBlending/assets/8387776/97d6f40f-9a26-47ce-8933-e5ab440b523a)
