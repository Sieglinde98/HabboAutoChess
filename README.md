# Subtitle modifier
#### Video Demo:  
#### Description:
The purpose of **Subtitle adjuster** is to modify a subtitle file, adding or substracting an ammount of seconds to each time interval sequence. This can help to match the text of the subtitles with the dialogue of a film, series or any video that a user is watching.

The program is composed of a Python Flask app with a single HTML and a CSS file. 


First I will explain the ```index.html``` file:
The header only shows the title, a simple description of the site and a Jinja block that reads from the ```app.py``` the ```error``` variable, which is a boolean that prints a green flash message if the submit was successful (error = False), and a red one if it wasn't (error = True).

The main block shows two different input and submit blocks:
- a input named "file", allowing to upload of a file
- another one named "time", allowing to set a float number
- and two buttones named "action", which will select if the user wants tho delay or advance the subtitles

When submitted, the app.py program will calculate everything, and if no errors occur with the input, will redirect to this same index file. Then the page will show a block displaying the filename, it's size, a display of the modified file and a button that allows to download it.


Now I will explain the ```app.py``` file:
First i'm defining two constant variables, one is ```UPLOAD_FOLDER``` that defines the folder where the uploaded, and later modified file, will be stored, and a second one called ```ALLOWED_EXTENSIONS``` which is a list containing all valid the subtitle file extensions.
Since there are lots of different writeable subtitle file extensions, each one for different media software and each one having a unique structure that organizes the subtitles, I decided to work with the most popular one, '.srt' (SubRip). But further updates of the program could have different functions that converts a file from one extension to another and vice versa and the results will be the same.

Second, I'm defining a route that serves as path to download the modified file.

Next is the index route. It will first check all the possible errors from the ```time```, ```action``` and ```file``` submitted from the page, each one flashing a different message. If there isn't, the program will store the uploaded file in the ```files``` folder, create a 'modified' copy of the filename, and then will start iterating over each character inside the uploaded file looking for time intervals like the next one (including the new lines): 

>*"*
>*00:00:12,180 --> 00:00:14,940*
>*"*

This sequence tells from when to when a subtitle text will appear at screen. Before these characters there is always an incremented number that numbers each individual subtitle, and after them there is always a text that shows the dialogue, and after this dialogue, two new lines followed by the next subtitle number. With this repeating pattern, I managed to read each character and determine where does it fit in the pattern, reading the time intervals into the ```intervals``` variable, and outputting the remaining characters into the modified file.

When the time intervals have been found, they'll be stored as a string and then execute rather the ```substract``` or ```add``` function if the user has submitted an ```Advance``` or ```Delay``` action respectively. Both functions have the same structure:
- it will split the ```intervals``` string into a list of characters, selecting the next lines, both time counters and the arrow in the middle (which is defined at ```intervals_to_clock``` function)
- then the timers inside ```intervals``` along with the ```time``` variable (which stores the submitted seconds) will be formatted as a date string (without the day, month and year part)
- then both variables will be summed or substracted, depending on the function
- and return the resulting sequence of characters to the main function

After this, the modified ```intervals``` variable will be writed in the output file, will reset the variables to search the next time sequence, modify it and repeat until the end of the file. 

When the file is finished, the program will prepare the value of the file size, the filename, the contents of the file to be displayed, will set the 'error' variable to "False" and flash a "The file is ready!" message before rendering everything in the index file.

Then you can download the resulting file and enjoy the film (/'u')/
