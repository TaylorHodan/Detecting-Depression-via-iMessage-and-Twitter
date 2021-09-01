import praw

reddit = praw.Reddit(
    client_id="kmvbGAQEpAbOsg",
    client_secret="0KS_nSCyhrq3lF3Gj8yiRX4RDiETxA",
    password="Appleby_2021",
    user_agent="Collecting Text Data",
    username="Explore_User_2021",
)    

#Variable:
postCount = 0 

posts = []
depressionSubreddit = reddit.subreddit('depression')
depressionHelpSubreddit = reddit.subreddit('depression_help')
depressionAloneSubreddit = reddit.subreddit('ForeverAlone')
depressionRSubreddit = reddit.subreddit('depressionregimens')
with open ("depressedUsers.txt", "w", encoding="utf-8") as mFile:
    with open("normalUsers.txt", "w", encoding="utf-8") as myFile:
        for post in depressionSubreddit.hot(limit=1000):
            pTitle = str(post.title)
            pText = str(post.selftext)
            pLength = len(pText)
            find = False
            if (pLength>30):
                for i in range (len(pText)-31):
                    if (pText[i:(i+31)].lower()=="i was diagnosed with depression" or pText[i:(i+31)].lower()=="i got diagnosed with depression"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)
                        find = True
                        postCount+=1
            if (pLength>25) and find==False:
                for i in range (len(pText)-26):
                    if (pText[i:(i+26)].lower()=="my diagnosis of depression"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText) 
                        find = True
                        postCount+=1
            if (pLength>39) and find==False:
                for i in range (len(pText)-40):
                    if (pText[i:(i+40)].lower()=="i got formally diagnosed with depression"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>21) and find==False:
                for i in range (len(pText)-22):
                    if (pText[i:(i+22)].lower()=="suffer from depression"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>22) and find==False:
                for i in range (len(pText)-23):
                    if (pText[i:(i+23)].lower()=="my depression diagnosis"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>24) and find==False:
                for i in range (len(pText)-25):
                    if (pText[i:(i+25)].lower()=="diagnosed with depression"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>20) and find==False:
                for i in range (len(pText)-21):
                    if (pText[i:(i+21)].lower()=="i want to kill myself"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True   
                        postCount+=1
            if (pLength>23) and find==False:
                for i in range (len(pText)-24):
                    if (pText[i:(i+24)].lower()=="i want to commit suicide"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>13) and find==False:
                for i in range (len(pText)-14):
                    if (pText[i:(i+14)].lower()=="i am depressed"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>23) and find==False:
                for i in range (len(pText)-24):
                    if (pText[i:(i+24)].lower()=="life is not worth living"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True  
                        postCount+=1
            if (pLength>18) and find==False:
                for i in range (len(pText)-19):
                    if (pText[i:(i+19)].lower()=="i dont want to live"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True 
                        postCount+=1
            if (pLength>14) and find==False:
                for i in range (len(pText)-15):
                    if (pText[i:(i+15)].lower()=="killing myself"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True  
                        postCount+=1
            if (pLength>10) and find==False:
                for i in range (len(pText)-11):
                    if (pText[i:(i+11)].lower()=="kill myself"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True  
                        postCount+=1
            if (pLength>12) and find==False:
                for i in range (len(pText)-13):
                    if (pText[i:(i+13)].lower()=="i want to die"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True 
                        postCount+=1
            if (pLength>6) and find==False:
                for i in range (len(pText)-7):
                    if (pText[i:(i+7)].lower()=="kill me"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True  
                        postCount+=1
            if find==False:
                myFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
            posts.append([pTitle, pText])
        
        for post2 in depressionHelpSubreddit.hot(limit=1000):
            p2Title = str(post2.title)
            p2Text = str(post2.selftext)
            p2Length = len(p2Text)
            find2 = False
            if (p2Length>30):
                for i in range (len(p2Text)-31):
                    if (p2Text[i:(i+31)].lower()=="i was diagnosed with depression" or p2Text[i:(i+31)].lower()=="i got diagnosed with depression"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)
                        find2 = True
                        postCount+=1
            if (p2Length>25) and find2==False:
                for i in range (len(p2Text)-26):
                    if (p2Text[i:(i+26)].lower()=="my diagnosis of depression"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text) 
                        find2 = True
                        postCount+=1
            if (p2Length>21) and find2==False:
                for i in range (len(p2Text)-22):
                    if (p2Text[i:(i+22)].lower()=="suffer from depression"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True
                        postCount+=1
            if (p2Length>39) and find2==False:
                for i in range (len(p2Text)-40):
                    if (p2Text[i:(i+40)].lower()=="i got formally diagnosed with depression"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True
                        postCount+=1
            if (p2Length>24) and find2==False:
                for i in range (len(p2Text)-23):
                    if (p2Text[i:(i+23)].lower()=="my depression diagnosis"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True 
                        postCount+=1
            if (p2Length>22) and find2==False:
                for i in range (len(p2Text)-25):
                    if (p2Text[i:(i+25)].lower()=="diagnosed with depression"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True
                        postCount+=1
            if (p2Length>20) and find2==False:
                for i in range (len(p2Text)-21):
                    if (p2Text[i:(i+21)].lower()=="i want to kill myself"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True 
                        postCount+=1
            if (p2Length>23) and find2==False:
                for i in range (len(p2Text)-24):
                    if (p2Text[i:(i+24)].lower()=="i want to commit suicide"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True     
            if (p2Length>13) and find2==False:
                for i in range (len(pText)-14):
                    if (pText[i:(i+14)].lower()=="i am depressed"):
                        mFile.write(str(pTitle)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(pText)    
                        find = True
                        postCount+=1
            if (pLength>23) and find==False:
                for i in range (len(p2Text)-24):
                    if (p2Text[i:(i+24)].lower()=="life is not worth living"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True   
                        postCount+=1
            if (p2Length>18) and find2==False:
                for i in range (len(p2Text)-19):
                    if (p2Text[i:(i+19)].lower()=="i dont want to live"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True  
                        postCount+=1
            if (p2Length>14) and find2==False:
                for i in range (len(p2Text)-15):
                    if (p2Text[i:(i+15)].lower()=="killing myself"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True 
                        postCount+=1
            if (p2Length>10) and find2==False:
                for i in range (len(p2Text)-11):
                    if (p2Text[i:(i+11)].lower()=="kill myself"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True 
                        postCount+=1
            if (p2Length>12) and find2==False:
                for i in range (len(p2Text)-13):
                    if (p2Text[i:(i+13)].lower()=="i want to die"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True  
                        postCount+=1
            if (p2Length>6) and find2==False:
                for i in range (len(p2Text)-7):
                    if (p2Text[i:(i+7)].lower()=="kill me"):
                        mFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p2Text)    
                        find2 = True 
                        postCount+=1
            if find2==False:
                myFile.write(str(p2Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")        
            
            posts.append([p2Title, p2Text])
            
        for post3 in depressionAloneSubreddit.hot(limit=1000):
            p3Title = str(post3.title)
            p3Text = str(post3.selftext)
            p3Length = len(p3Text)
            find3 = False
            if (p3Length>30):
                for i in range (len(p3Text)-31):
                    if (p3Text[i:(i+31)].lower()=="i was diagnosed with depression" or p3Text[i:(i+31)].lower()=="i got diagnosed with depression"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)
                        find3 = True
                        postCount+=1
            if (p3Length>25) and find3==False:
                for i in range (len(p2Text)-26):
                    if (p3Text[i:(i+26)].lower()=="my diagnosis of depression"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text) 
                        find3 = True
                        postCount+=1
            if (p3Length>21) and find3==False:
                for i in range (len(p3Text)-22):
                    if (p3Text[i:(i+22)].lower()=="suffer from depression"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True
                        postCount+=1
            if (p3Length>39) and find3==False:
                for i in range (len(p3Text)-40):
                    if (p3Text[i:(i+40)].lower()=="i got formally diagnosed with depression"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True
                        postCount+=1
            if (p3Length>24) and find3==False:
                for i in range (len(p3Text)-25):
                    if (p3Text[i:(i+25)].lower()=="diagnosed with depression"):
                        mFile.write(str(p3Title)+"\n"+str(p2Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True
                        postCount+=1
            if (p3Length>22) and find3==False:
                for i in range (len(p3Text)-23):
                    if (p3Text[i:(i+23)].lower()=="my depression diagnosis"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True 
                        postCount+=1
            if (p3Length>20) and find3==False:
                for i in range (len(p3Text)-21):
                    if (p3Text[i:(i+21)].lower()=="i want to kill myself"):
                        mFile.write(str(p3Title)+"\n"+str(pText)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True 
                        postCount+=1
            if (p3Length>23) and find3==False:
                for i in range (len(p3Text)-24):
                    if (p3Text[i:(i+24)].lower()=="i want to commit suicide"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True   
                        postCount+=1
            if (p3Length>13) and find3==False:
                for i in range (len(p3Text)-14):
                    if (p3Text[i:(i+14)].lower()=="i am depressed"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True
                        postCount+=1
            if (p3Length>23) and find3==False:
                for i in range (len(p3Text)-24):
                    if (p3Text[i:(i+24)].lower()=="life is not worth living"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True
                        postCount+=1
            if (p3Length>18) and find3==False:
                for i in range (len(p3Text)-19):
                    if (p3Text[i:(i+19)].lower()=="i dont want to live"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True   
                        postCount+=1
            if (p3Length>14) and find3==False:
                for i in range (len(p3Text)-15):
                    if (p3Text[i:(i+15)].lower()=="killing myself"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True  
                        postCount+=1
            if (p3Length>10) and find3==False:
                for i in range (len(p3Text)-11):
                    if (p3Text[i:(i+11)].lower()=="kill myself"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find = True   
                        postCount+=1
            if (p3Length>12) and find3==False:
                for i in range (len(p3Text)-13):
                    if (p3Text[i:(i+13)].lower()=="i want to die"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True  
                        postCount+=1
            if (p3Length>6) and find3==False:
                for i in range (len(p3Text)-7):
                    if (p3Text[i:(i+7)].lower()=="kill me"):
                        mFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p3Text)    
                        find3 = True 
                        postCount+=1
            if find3==False:
                myFile.write(str(p3Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")        
            
            posts.append([p3Title, p3Text])  
            
        for post4 in depressionRSubreddit.hot(limit=1000):
            p4Title = str(post4.title)
            p4Text = str(post4.selftext)
            p4Length = len(p4Text)
            find4 = False
            if (p4Length>30):
                for i in range (len(p4Text)-31):
                    if (p4Text[i:(i+31)].lower()=="i was diagnosed with depression" or p4Text[i:(i+31)].lower()=="i got diagnosed with depression"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)
                        find4 = True
                        postCount+=1
            if (p4Length>21) and find4==False:
                for i in range (len(p4Text)-22):
                    if (p4Text[i:(i+22)].lower()=="suffer from depression"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True
                        postCount+=1
            if (p4Length>25) and find4==False:
                for i in range (len(p4Text)-26):
                    if (p4Text[i:(i+26)].lower()=="my diagnosis of depression"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text) 
                        find4 = True
                        postCount+=1
            if (p4Length>39) and find4==False:
                for i in range (len(p4Text)-40):
                    if (p4Text[i:(i+40)].lower()=="i got formally diagnosed with depression"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True
                        postCount+=1
            if (p4Length>22) and find4==False:
                for i in range (len(p4Text)-23):
                    if (p4Text[i:(i+23)].lower()=="my depression diagnosis"):
                        mFile.write(str(p4Title)+"\n"+str(p3Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True  
                        postCount+=1
            if (p4Length>24) and find4==False:
                for i in range (len(p4Text)-25):
                    if (p4Text[i:(i+25)].lower()=="diagnosed with depression"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True
                        postCount+=1
            if (p4Length>20) and find4==False:
                for i in range (len(p4Text)-21):
                    if (p4Text[i:(i+21)].lower()=="i want to kill myself"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True  
                        postCount+=1
            if (p4Length>23) and find4==False:
                for i in range (len(p4Text)-24):
                    if (p4Text[i:(i+24)].lower()=="i want to commit suicide"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True     
                        postCount+=1
            if (p4Length>13) and find4==False:
                for i in range (len(p4Text)-14):
                    if (p4Text[i:(i+14)].lower()=="i am depressed"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True
                        postCount+=1
            if (p4Length>23) and find4==False:
                for i in range (len(p4Text)-24):
                    if (p4Text[i:(i+24)].lower()=="life is not worth living"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True   
                        postCount+=1
            if (p4Length>18) and find4==False:
                for i in range (len(p4Text)-19):
                    if (p4Text[i:(i+19)].lower()=="i dont want to live"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True  
                        postCount+=1
            if (p4Length>14) and find4==False:
                for i in range (len(p4Text)-15):
                    if (p4Text[i:(i+15)].lower()=="killing myself"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True 
                        postCount+=1
            if (p4Length>10) and find4==False:
                for i in range (len(p4Text)-11):
                    if (p4Text[i:(i+11)].lower()=="kill myself"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True  
                        postCount+=1
            if (p4Length>12) and find4==False:
                for i in range (len(p4Text)-13):
                    if (p4Text[i:(i+13)].lower()=="i want to die"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True 
                        postCount+=1
            if (p4Length>6) and find4==False:
                for i in range (len(p4Text)-7):
                    if (p4Text[i:(i+7)].lower()=="kill me"):
                        mFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")
                        i=len(p4Text)    
                        find4 = True 
                        postCount+=1
            if find4==False:
                myFile.write(str(p4Title)+"\n"+str(p4Text)+"\n\n\nTHISisAnewPOST\n")        
            
            posts.append([p4Title, p4Text])           

print(postCount)
myFile.close()
mFile.close()