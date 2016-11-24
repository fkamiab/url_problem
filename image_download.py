# Author: Farbod Kamiab
# Code that takes a plaintext file as an argument and downloads all images, storing them on the local hard disk

import sys
import os
import urllib
import imghdr


def main():

    ################################
    
    ''' Makes sure that the path to the URL text file is provided. If not, an error message is displayed. '''
    
    if len(sys.argv)<2:
        print 'Please run the code with a valid path to the URL text file as its argument.'
        sys.exit(2)
        
    ################################
    
    ''' Storing the path to the file. '''
    
    filename = sys.argv[1]
    
    ################################
    
    ''' Tries to open the file specified, and store its content in a list, and if the procedure fails, an error message is displayed. '''
    
    try:
        with open(filename) as f:
            list_of_urls = f.readlines()
    except IOError:
        print 'Path or filename provided is not valid.'
        sys.exit(2)
        
    ################################
    
    ''' Strips the list of urls of blank lines '''
    
    list_of_urls = map(lambda s: s.strip(), list_of_urls)
    list_of_urls = filter(None, list_of_urls)
    
    ################################
    
    ''' If it does not yet exist, creates a local directory for saving the images. '''
    
    path_images = './IMAGES'
    if not os.path.exists(path_images):
        os.makedirs(path_images)
    print 'Saving images in {}'.format(path_images)
    
    ################################
    
    ''' If it does not yet exist, creates a directory for storing the error log. Also opens the error log file.'''
    
    path_error_log = './ERROR_LOG'
    if not os.path.exists(path_error_log):
        os.makedirs(path_error_log)
    error_log_file = open("{}/error_log.txt".format(path_error_log), "w")
    print 'Saving error log in {}'.format(path_error_log)
    
    ################################
    
    ''' Creates two counter indices to count the number of failures, either in the validity of the image files or the urls. '''
    
    index_image_fail=0
    index_url_fail =0
    
    ################################
    
    '''  For-loop going through each of the urls and downloading the images. '''
    
    for i in range(0, len(list_of_urls)):
        # Tries connecting to the URL and retrieving the image file. 
        try:
            # Path for saving the image specified. 
            image = "{}/image_{}.jpg".format(path_images, i)
            # Retrieves the image from the URL. 
            urllib.urlretrieve(list_of_urls[i], image)
            # If the image retrieved is a corrupted/not valid file type, it deletes it.
            if imghdr.what(image)==None:
                os.remove(image)
                # If it is the first image file failure, creates a list and stores the URL of the file in it. 
                # Then keeps adding subsequent failures to the list
                if index_image_fail==0:
                    list_image_fail =[list_of_urls[i]]
                else:
                    list_image_fail.append(list_of_urls[i])
                # Counts the number of image file failures
                index_image_fail += 1
        # If retrieving the file from the URL fails, stores the url failures in a separate failure list and counts the instances.     
        except IOError:
            if index_url_fail ==0:
                list_url_fail =[list_of_urls[i]]
            else:
                list_url_fail.append(list_of_urls[i])
            index_url_fail += 1

    ################################
    
    ''' ERROR LOG FILE '''
    # If the list of image file failures is not empty, stores the URLs matching the error in the error log file. 
    try:
        length=len(list_image_fail)
        error_log_file.write('The image in the following URLs is not a valid image:\n')
        for i in range(0, length):
            error_log_file.write('{}\n'.format(list_image_fail[i]))
    # If the list is empty, says all files are valid in the error log file. 
    except NameError:
        error_log_file.write('All files downloaded were valid images.\n')

    # If the list of url failures is not empty, stores the URLs matching the error in the error log file    
    try:
        length=len(list_url_fail)
        error_log_file.write('The following URLs could not be reached:\n')
        for i in range(0, length):
            error_log_file.write('{}\n'.format(list_url_fail[i]))
    # If the list is empty, says all files are valid in the error log file.           
    except NameError:
        error_log_file.write('All URLs were valid.\n')
    # Closes error log file.    
    error_log_file.close()

    ################################    

    
    return None




if __name__ == "__main__":
    
    main()



