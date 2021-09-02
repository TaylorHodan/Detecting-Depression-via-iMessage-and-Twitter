# Detecting-Depression-via-iMessage-and-Twitter
This was part of my AP Research study that focused on designing an algorithm to detect signs of depression in users by analyzing their data from iMessage and Twitter. The score that was returned by the program reflected whether the user had depression and, if so, the severity.

The first phase of this program involved collecting data from the Reddit API to test whether the program could correctly identify users with depression. To be considered depressed, the user had to be found on a depression-related subreddit and had to mention specific phrases, such as "I was diagnosed with depression." During each phase, the number of correctly identified cases was examined as well as the number of each times a symptom, such as fatigue or a depressed mood, were flagged. Adjustments were then made accordingly to try to increase the accuracy of the program.

The next phase involved testing the program on users' Twitter and iMessage data. These participants voluntarily signed up to participate in this research study. Users would run the corresponding Twitter and iMessage files, and then enter the released score into the Swift file. This interpreted their score and told them whether they had depression and, if so, the severity.

This tool is still in beta testing, and is not a clinical assessment. Rather it acts as a means of potentially alerting users that they are showing signs of depression and should receive professional medicial assistance. 

The Swift files for the mobile application are still in the process of being published.
