# Exercise 2 - Writing scripts and using GitHub
The exercise for this week is meant to help you better understand data types and lists in Python, and practice saving files to GitHub.
Below you have a series of "problems" in which you will be asked to solve by either downloading and modifying a starter script, or creating a new script file.
After making you changes, you will need to upload them to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/2017/lessons/L2/exercise-2-hints.html) if you're having trouble.

Scores on this exercise are out of **20 points**.

## Problem 1 - Making changes to a file in GitHub (*7 points*)
Your first task for this week is to make some modifications to the broken script [`station_ages.py`](station_ages.py) that is included in this week's exercise.
The script should allow users to find the age of an [FMI observation station](http://en.ilmatieteenlaitos.fi/observation-stations) by setting the `selectedStation` variable.
Don't worry about the case of a user entering a station name that is not on the list.

**Your score on this problem will be based on**

- Fixing **3 major code problems** to get this script working as expected
- Committing each change separately to GitHub without changing the script filename
- Listing the changes you needed to make to get the code working in plain English at the end of this file (see [Problem 3](#problem-3) below).

## Problem 2 - Creating and uploading a script to GitHub (*9 points*)
The table below presents [monthly average temperatures recorded at the Helsinki Malmi airport](https://www.timeanddate.com/weather/finland/helsinki/climate).

| Month     | Temperature [°C] |
| --------- | :--------------: |
| January   | -3.5             |
| February  | -4.5             |
| March     | -1.0             |
| April     | 4.0              |
| May       | 10.0             |
| June      | 15.0             |
| July      | 18.0             |
| August    | 16.0             |
| September | 11.5             |
| October   | 6.0              |
| November  | 2.0              |
| December  | -1.5             |

Create a script called `average_temps.py` that allows users to select a month and have the monthly average temperature printed to the screen.
For example, if the user sets month to "March", the script will display

```
The average temperature in Helsinki in March is -1.0
```
**Your score on this problem will be based on**

- Having your script display the monthly average temperature in a selected month, set by defining the variable `selectedMonth` near the top of the script.
- Having it work for all 12 months in the year.
- Using the basic script format described in [this week's lesson](https://geo-python.github.io/2017/lessons/L2/writing-scripts.html).
- Including comments that explain what most lines in the code do
- Uploading your script to your GitHub repository for this week's lesson with the name `average_temps.py`.
- Your answers to the three questions about the challenges you faced in writing your own script (see [Problem 3](#problem-3) below).

## Problem 3 - Answering questions using Markdown (*4 points*)
The last task in this week's exercise is to make some changes to this `README.md` file to provide answers to the following questions.

1. Under the heading for Problem 1 (`## Problem 1`), list the changes you needed to make to the code (in regular English, not Python code) to get it working.
You are welcome to use a numbered list if you like.
You can read about how to format numbered lists on the GitHub page about [GitHub-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
2. Add a heading for Problem 2 and beneath it list some of the challenges you faced in creating your own Python script from scratch.
What parts of the code were most difficult to create? What things were you able to take from other resources in this week's lesson? Any other comments about the difficulties in creating your own script?

3. Add a heading for Problem 3 and beneath it give your comments about this week's lesson.

    - What did you like?
    - What did you dislike?
    - What would you change?
    
4. Lastly, just for fun, add an image of an animal that you like along with a short caption giving its name and anything special you might like to add.
You can add an image by linking to a website, or by uploading an image to your GitHub repository and linking to that.
Since we've spoken briefly about software licencing, we suggest that you search for images in a repository that includes licencing information such as [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) or [Pixabay](https://pixabay.com/).
You are, of course, also welcome to upload your own animal images.
You can add it under the Problem 3 heading in the answers.

**Your score on this problem will be based on**

- Your answers to the three questions in part 3 of this problem
- Posting an image of a favorite animal using Markdown

# Answers
## Problem 1

#### Excercise 1 - Finding errors in the script

The following are the corrections needed to make the provided code to run proberly:

1. *SyntaxError* - in the print statement. "years. was changed to "years." 
2. *ValueError* - `selectedStation` = 1 is invalid staement, and was changed to `selectedStation` = `stationName[index]`
3. *TypeError* - the `stationYears` was given a wrong type of input, which is why I added a new variable ´`selectedYear` to fetch an index with and assigned that as an input to perform the calculation with.  

## Problem 2 - Creating one's own script

**1. The hardest parts of the code dealt with index and how to use it:**

   * I haven't been playing with Python in awhile so getting up and going was a bit slow. I noticed I still have problems understanding the 'fetching' of items in a list with an index and then assigning them to a new variable in order to use it in an print statement. Somehow it seems abit abstract...? Maybe it is becouse the whole idea of methods (the dot notation in lists or other objects), feels complex especially when you have many variables and/ or combine many methods together.

   * In general the idea that index starts with a zero is not that hard to comprehend, even though at times when you get to more complex pieces of code it can cause a minor error/ miscalculation, but usually that is becouse I am so lost with the code to beging with :smile:
   
**2. What influences or ideas you were able to take from other of this weeks resources?**

   * I added an extra print statement printing out the month and its index, as it clarified/ simplified the code for me abit. First I got the error of not being able to print the line as I was lumbing string and integer variables together. So instead of creating a whole new variable such as MonthIndexStr, I just used the str() method to convert the variable within the print statement.

   * Also, I like to keep my code 'tidy' (i.e. readable) so adding comments (or just comment something like #---------------------) or adding empty line to identify 'blocks' is normal to me. The docstrings was a newer concept to me that I have to integrate to my style, as I do feel it makes the script look more professional and in a way more 'thought out'.
   
**3. Other comments with respect to creating one's own script:**
 
   * The excercise felt in general okay and did not cause any major difficulties, but usually when starting from square one on your own, it can feel quite intimidating. What I often do is to write down what variables I need, in what order I should introduce them and what 'methods' (not as in append., .reverse(), etc. but what kind of structure the code should take - lists, creating functions, if-loops...) I need to implement in order to get the final, correct output. Writing stuff down seems to arrange the question at hand in my head and then I can move on to my computer and start playing with the actual code.

   * I also try not to think that certain 'methods' should always be used on their own, but I think form a learning/ understaning perspective, it is important to make your brain understand that different methods can and should be used mixed together. When I started, it was difficult to mix i.e. if -loops with for- statements as I learned them separately (if that makes any sense). So I find it to be important to make that super clear from the very beginning, but at the same time I find I start loosing motivation when the taks and excercises get way too complicated way too fast - so finding the middle ground is important... 

   * These comment may not relate to the original question, but just wanted to point these issues out if there are any students in the course who have as complicated way of thinking as I have :smiley: 
    
 ## Problem 3 - Comments and thoughts on this weeks lecture and excersice
 
:+1: **What I liked about this weeks topics:**

- As I have been studying Python independently with Zed Shaw's *Learn Python the Hard Way* (really good book for learning the basics btw) I have some knowledge on different data types and how they behave, that they have their own in-built methods, etc. so sitting in the lecture room without having to take notes felt **__good__** :sunglasses: 

- The excercises requred some *programmatical* thinking when it comes to creating new variables and assigning indeces which allows your brain to learn and think in a certain way. This is becouse there is a logic behind programming, but at the beginning it does not always feel like so...

:-1: **What I disliked this week:** 

- Can't really say much here as I already noted above, the topics discussed this week were fairly easy. And I hope in the future I can keep saying the same (knocks on wood :facepunch:). 

:open_mouth: **What I would change/ alter:**

- What I noticed by overhearing others discussing as the class ended, was that the speed was pretty fast and some weren't able to keep up. I can identify to this becaouse the main reason why I have skipped few programming courses before has been becouse the speed in the class has been way too fast and moving on to way too difficult tasks too soon. I understand in the class the speed has to be pretty considerable in order to go through all the topics but playing with the basic concepts is essential in order to learn the *logic* of coding in general...

  * I think linking some exercises from Shaw's Learn Python the Hard Way might allow some students who are new/ have problems understandig how the code works to grasp a better understanding of the topics discussed in the class.
  
    * Becouse in the excersices you have study drills where you pretty much have to break, modify and 'trash' the code, you learn better how the code behaves if you tweak it there and how it reacts when you comment out another line here or there. At least for me taking time to actually play with the code has helped alot! In general internalizing that you cannot break the code but you can always access the original script might also take the 'fear' of the code away... 

![Text shown if image does not load](https://github.com/Kajomi/Python-for-GeoPeople---course/blob/master/orcas.jpg)<br/>
*Figure 1:Having lived both in Seattle and B.C. and still not seeing any orcas pisses me off. Regardless, beautiful animals!*



This is some text.
You can use *italics* or **bold** text easily.
You may want to read a bit more about [formatting text in Github-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
You can see an example of how to display an image with a caption below.
