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
    image=[]
    ref_link=[]

    url="https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=5"

    driver=webdriver.Chrome()
    driver.get(url)
    ps=driver.find_elements(By.CLASS_NAME, 'flex-container')
    
    for i in ps:
        a=i.find_element(By.TAG_NAME, 'rt-img')
        title.append(a.get_attribute('alt'))
        image.append(a.get_attribute('src'))
        b=i.find_element(By.TAG_NAME, 'a') 
        ref_link.append(b.get_attribute('href'))
    print("Done")
    data={"Title": title, "Image_Link": image, "Refrence_Link":ref_link}
    df_1=pd.DataFrame(data)
    df_1.to_csv("Rotten_Tomatoes_Movie_List.csv")
    return title,image,ref_link
            

title,image,ref_link=movie_list()
title_1,year,rating,genre,rating_score,running_duration=movie_info(ref_link)
#title_1,rating,year,genre,rating_score,running_duration=movie_info(ref_link)
data2={"Title":title_1, "Rating":rating[0].split(' ')[0],"Year":year,"Genre":genre,"Rating_Score":rating_score,"Duration":running_duration,"Image_Link":image}
df=pd.DataFrame(data2)
print("done with table")
df.to_csv("Rotten_Tomatoes_Movie_Info.csv")





