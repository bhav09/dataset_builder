# dataset_builder
With this, one can create his own custom data set of image for the purpose of Image Classification.

Have segregated the application into 2 files so that is becomes easy to understand the processes behind building this boulder.


App.py is sum of frontend.py and backend.py with some slight changes.

    1. Frontend.py consists the code to launch the GUI
    2. Backend.py consists the code responsible for backend functioning of the application
    3. App.py consists the code which is formed by concatening the above files.
    
 
My chrome version is 81 so the driver that is being uploaded is according to the chrome version.

    To find the version of your chrome browser : chrome://settings/help
    Link to download the driver for chrome : https://chromedriver.chromium.org/downloads

You will have to run App.py only (make sure all the attachments(files) mentioned are present in the same directory) .

App.py is a prototype which can at max scrap and download 110 images from the web page , dynamically. So make sure that the number of images you want to download should not exceed 110. 
