# Binary-Classification-of-Images-Using-CNN

# * Collection Of Data
---> Collected the dataset  which consist of images dogs vs cat where it consist of different transformation of Data in both training set and test set where the data was not uploaded in the directory fetched through the API from kaggle
     using following Command

                       !mkdir -p ~/.kaggle
                       !cp kaggle.json ~/kaggle.json

---> After fetching the data and downloading the data in the editor, the data will be downloaded in the format of zip Using the following API token from the kaggle

                      !kaggle datasets download -d salader/dogs-vs-cats


# * Conversion of Zip file to folder

---> The Conversion of Zip to the file is converted using the zipfile Module by using the following code

                               import zipfile
                               zip_ref=zipfile.ZipFile('/content/dogs-vs-cats.zip','r')
                               zip_ref.extractall('/content')
                               zip_ref.close()

# * Overview 

---> Build AN CNN Architecture/Model and explored how CNN Extract the features from the image data and provides efficient results on the images data

---> Devloped an Binary Classification CNN Model and trained the Model on 20k+ images on training data and prediction of testing data with 10k images where model classifies and produce the output based on the imput of the image data.

---> To extract the features of the input data, implemented different type of Convolution Operation

                1) Convolution Operation
                2) MaxPooling
                3) Activation




  ![image](https://github.com/mudith-nahata/Binary-Classification-of-Images-Using-CNN/assets/96544398/c39285fe-c8a9-488f-9e74-d62ab76aca12)




# * Results

---> After Evaluating the Perfomace of CNN Model where Model Performs Well on the training data and doesnt perfom well in the test data

# * Implemented Features

---> As the Existing Model Consist with  the Problem of Overfitting 

---> Implemented the techniques such as Batch Normalization, Dropouts ,Data Augmentation and improved the perfomance of CNN Model on testing and data  and acheived the accuracy of 95%

# * Libraries Used

            1) NumPy
            2) Pandas
            3) Matplotlib
            4) Tensorflow
            5) Keras
            6) OpenCV

# * Technologies Used

        --> Deep Learning Neural Networks
