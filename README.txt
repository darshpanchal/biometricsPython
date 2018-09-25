** Voice and Facial Biometrics system in Python 2.7 **

Prerequisites: (Install using pip)
1 - opencv2-python
2 - numpy
3 - scipy
4 - sklearn

Details: 

This biometrics currently have trained facial data of Tom Cruise and PM Modi. Their voice data wasn't available
so I downloaded sample voice data set from internet and renamed one as modi and another as tom. Currently test image is taken from test_data folder. And test audio wav files are in development_set_test.txt (for test data of modi) and you can rename development_set_test.txt.tom to development_set_test.txt (for test data of tom). Currently live recording of voice and picture is not supported due to my computer limitations.

For Voice recognition, GMM (Gaussian Mixture Model) is used to train extracted MFCC's of a wav audio file and then saving voice model with extention .gmm in speaker_models folder.

For Face recognition, Haarcascade is used to detect face and to predict face, LBPH face recognizer is used.

Usage:

Step 1 - Run __init__.py script and then Enter "Yes" or "Y" (without quotes) to continue.
Step 2 - Then enter name ("tom" or "modi")
Step 3 - Then Let script test the data and give results. If all data matches then "Door Unlocked" will be printed in CLI 	 but if any of the authentication fails then "Authentication failed" will be printed on CLI.


Training:

If you want to train model with new users, simply add 3-4 images of the person in training_data folder with subfolder name "s3", "s4" and so on.. And for voice, add 5 new mono wav files to development_set folder.


PS - Do not forget to change the development_set_test.txt file contents as per required persons authorization.
If any issues, feel free to ping me on darshpanchal.97@gmail.com