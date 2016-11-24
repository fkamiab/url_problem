# URL Problem

This is a script that takes a plaintext file containg URLs of images as an argument and downloads all images, storing them on the local hard disk.

## Input File
The file, containing the URLs should be a plaintext file, with the URL of an image on each of its lines. The [URLS.txt](https://github.com/fkamiab/url_problem/blob/master/URLs/URLs.txt), is an example of such a text file. Some of the URLs may contain files that are not valid images, and some of the URLs may be faulty and not accessible. The code [image_download.py](https://github.com/fkamiab/url_problem/blob/master/image_download.py) is written in a way that can handle these two types of errors. So you can either run the code with your own input file with an arbitrary path name, or by specifying the path of this given input file in the local [URLs](https://github.com/fkamiab/url_problem/tree/master/URLs) directory.

## Running the Code
In order to run the code, use python 2.7, and in the command line, type:

~~~~
python image_download.py path_to_URL_textfile
~~~~

For example, if you are using the local [URLS.txt](https://github.com/fkamiab/url_problem/blob/master/URLs/URLs.txt) file, type:

~~~~
python image_download.py ./URLs/URLs.txt
~~~~

If the pathname or filename are wrong, the code will prompt you with an error message.

## Output

The code creates two local directories (if they do not already exist):

~~~~
./IMAGES
~~~~

and

~~~~
./ERROR_LOG
~~~~


The downloaded images, will be in the `./IMAGES` folder. If an image is faulty, the code does not include it. The errors (either the urls of faulty images or inaccsessible urls) are saved in an `error_log.txt` file in the `ERROR_LOG` directory.



