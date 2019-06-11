# Car-Classification---Stanford-Dataset
<!--This is the model for the classification problem posed by the Stanford  car dataset. This is also the official submission for the Grab AI for S.E.A challenge 2019.-->

<b>Problem Statement:</b> As mentioned on the description page of the <a href='https://ai.stanford.edu/~jkrause/cars/car_dataset.html'>dataset</a>, the task is to classify the image of a car into different classes. These classes are typically based on the model, make and year of the launch of the car.

<b>Dataset Description:</b><br>
The dataset contains train and test image set, in about equal proportion. Each of the image in the dataset belongs to one of the 196 classes. <br>
It also contains a separate annotations file for both the training and the test set. These files define the bounding boxes for the cars in each of the image and the class to which the car belongs. These annotation files are added here under devkit folder and 

<b>Approach</b><br>
The idea was to use a pretrained model and test it on the test data. The idea seems to work and was able to achive high accuracy on the test set. And the reason I chose Densenet121 architecture is that I feel they could propagate the features more efficiently even though they use more memory.<br>
<b>How to run</b><br>
Run the very first cell of the notebook, to import all the libraries used.(requirements.txt has been attached for more help in case of any issues)
To retrain the model run all the cells under the header 'Training'
To test the model, jump to the header 'Test'. It will load the pretrained saved parameters in the model architecture and use it to make the predictions.
For any custom dataset, change the test images folder path in the notebook (i.e. path_test_img variable) and change the path of the test annotation file as well.
