import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def movie_info(link):
    #Extracting movie information based on link passed as an argument
    year=[]
    title=[]
    rated=[]
    duration=[]
    rating_score=[]
    genre=[]
    info=[]
    for l in link:
        url=l
        driver=webdriver.Chrome()
        driver.get(url)

        ps=driver.find_elements(By.CLASS_NAME,"c-heroMetadata_item.u-inline")
        tl=driver.find_elements(By.CLASS_NAME,"c-productHero_score-container.u-flexbox.u-flexbox-column.g-bg-white")
        score=driver.find_elements(By.CLASS_NAME,"c-siteReviewScore.u-flexbox-column.u-flexbox-alignCenter.u-flexbox-justifyCenter.g-text-bold.c-siteReviewScore_green.c-siteReviewScore_user.g-color-gray90.c-siteReviewScore_medium")
        gen=driver.find_elements(By.CLASS_NAME, "c-globalButton_container.g-text-normal.g-height-100.u-flexbox.u-flexbox-alignCenter.u-pointer.u-flexbox-justifyCenter.g-width-fit-content")

        count = 0
        for i in ps:
            count+=1
            if count <= 4:
                a=i.find_element(By.TAG_NAME, "span")
                info.append(a.text.split('\n')[0])
                if count==1:
                    year.append(a.text.split('\n')[0])
                if count==2:
                    rated.append(a.text.split('\n')[0])
                if count==4:
                    duration.append(a.text.split('\n')[0])

        for j in tl:
            a=j.find_element(By.TAG_NAME,"div")
            title.append(a.text)

        count1 = 0
        for i in score:
            count1 += 1
            if count1 == 1:
                a=i.find_element(By.TAG_NAME, "span")
                rating_score.append(a.text)

        count2 = 0
        for g in gen:
            count2 += 1
            if count2 == 1:
                a=g.find_element(By.TAG_NAME,"span")
                # h=[q for w in [a.text] for q in w.split(",")]
                genre.append(a.text)
    
    
    return year,rated,duration,title,rating_score,genre

def movie_list():
    title=[]
    img_link=[]
    ref_link=[]
    for i in range(1,9):
        url="https://www.metacritic.com/browse/movie/?releaseYearMin=1910&releaseYearMax=2024&page="+str(i)
        driver=webdriver.Chrome()
        driver.get(url)

        ps=driver.find_elements(By.CLASS_NAME,"c-finderProductCard")
        tl=driver.find_elements(By.CLASS_NAME,"c-finderProductCard_info.u-flexbox-column")

        for i in ps:
            a=i.find_element(By.TAG_NAME,"a")
            ref_link.append(a.get_attribute("href"))
            b=i.find_element(By.TAG_NAME, "img")
            img_link.append(b.get_attribute("src"))
        
        for j in tl:
            c=j.find_element(By.TAG_NAME, "div")
            title.append(c.get_attribute("data-title"))
    return title,img_link,ref_link
    # data={"Title":title,"Image_Link":img_link,"Refrence_Link":ref_link}
    # df=pd.DataFrame(data)
    # df.to_csv("Metacritics_Movie_List.csv")
    

title_1,image,ref_link=movie_list()
year,rated,duration,title,rating_score,genre=movie_info(ref_link)

data1={"Title":title,"Genre":genre,"Image_Link":image}
data2={"Year":year,"Rating":rated,"Duration":duration}
data3={"Rating_Score":rating_score}
df_1=pd.DataFrame(data1)
df_2=pd.DataFrame(data2)
df_3=pd.DataFrame(data3)
df_1.to_csv("Metacritics_Title_Genre_image.csv")
df_2.to_csv("Metacritics_Year_Rating_duartion.csv")
df_3.to_csv("Metacritics_Rated.csv")


