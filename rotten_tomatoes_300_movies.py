import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def movie_info(link):
      
    title_1=[]
    info=[]
    rating=[]
    rating_score=[]
    year=[]
    genre=[]
    running_duration=[]
    for j in link:
        print("Start")
        url=j
        driver=webdriver.Chrome()
        driver.get(url)
 
        #getting rating score through xpath
        rating_link = driver.find_element(By.XPATH, '//*[@id="topSection"]/div[1]')
        rating_score.append(rating_link.text.split('\n')[12].split(' ')[0])
       
        #Getting title and movie info
        ps=driver.find_elements(By.CLASS_NAME, 'thumbnail-scoreboard-wrap')
        rate=driver.find_elements(By.CLASS_NAME,'panel-body.content_body')
 
        for i in ps:
            a=i.find_element(By.TAG_NAME, 'h1')
            title_1.append(a.text)
            b=i.find_element(By.TAG_NAME, 'p')
            info.append(b.text)
            h= [q for w in [b.text] for q in w.split(",")]
            year.append(h[0])
            genre.append(h[1])
            running_duration.append(h[2])

        #Getting the rating for the movie
        for k in rate:
            a=k.find_element(By.TAG_NAME,'span')
            rating.append(a.text)
        
    print("end")
    return title_1,year,rating[0],genre,rating_score,running_duration


def movie_list():
    title=[]
    ref_link=[]
    img_link=[]

    for i in range(1,3):

        url="https://editorial.rottentomatoes.com/guide/essential-movies-to-watch-now/"+str(i)+"/"
        driver=webdriver.Chrome()
        driver.get(url)

        ps=driver.find_elements(By.CLASS_NAME, 'row.countdown-item')
        tl=driver.find_elements(By.CLASS_NAME, 'article_movie_title')
        
        #extracting image and refrence link
        for i in ps:
            
            b=i.find_element(By.TAG_NAME, 'img')
            img_link.append(b.get_attribute('src'))
            c=i.find_element(By.TAG_NAME, 'a') 
            ref_link.append(c.get_attribute('href'))

        #extracting the title of movie
        for i in tl:
            a=i.find_element(By.TAG_NAME, 'a')
            title.append(a.text)

    # mov_lst={"Title":title,"Image_Link": img_link,"Refrence_Link":ref_link}
    # df=pd.DataFrame(mov_lst)
    # df.to_csv("Rotten_Tomatoes_300_Movie_list.csv")
    return img_link,ref_link

image,ref_link=movie_list()
title_1,year,rating,genre,rating_score,running_duration=movie_info(ref_link)
data2={"Title":title_1, "Rating":rating[0].split(' ')[0],"Year":year,"Genre":genre,"Rating_Score":rating_score,"Duration":running_duration,"Image_Link":image}
df=pd.DataFrame(data2)
df.to_csv("Rotten_Tomatoes_300_Movie_Info.csv")