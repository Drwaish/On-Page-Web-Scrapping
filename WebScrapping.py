#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the BeautifulSoup Library  
  
from bs4 import BeautifulSoup
import requests  
  
#Creating the requests  
  


# In[3]:


"""Request to get content from website"""

URL="http://lhr.nu.edu.pk/faculty/"
res = requests.get(URL)  
print(res.text)  
# Convert the request object to the Beautiful Soup Object  

print(res.status_code)


# In[4]:


#print title
soup=BeautifulSoup(res.content,'html.parser')
print(soup.title.text)


# In[6]:


#Load data of fast school of computing into card
card=soup.find(id="fsc")


# In[7]:


#print card here
card.prettify()


# In[8]:



#Collect data of images from facultyImage
facu=card.find_all("div",class_="facultyImage")


# In[9]:


#load data from image tags into img 
img=card.select("img")


# In[10]:


#list to store image links
image_link=[]


# In[11]:


for sr in img:
    image_link.append(sr['src'])
    


# In[12]:


image_link[0:3]


# In[13]:


#for name of faculty
name_h5 = soup.select('h5')


# In[14]:


name=[] #faculty names


# In[15]:



for i in range(len(name_h5)):
    name.append(name_h5[i].text)
    


# Names of Faculty

# In[16]:


name[0:3]


# Designation and Emails of faculty

# In[17]:


designation=[]
hec_approved_phd_supervisor=[] #1 means true 0 means false
emails=[]


# In[18]:


#select all p tags for getting Designition and Emails or is he/she HEC approved supervisior
small=card.select("p")


# In[19]:


#vb=small[1].text
#vb[0]
#val1=vb.split("\n")
#vb
#val1[2].strip()
#len(val1)


# In[20]:


for i in range(len(small)):
    vb=small[i].text.strip()
    # At even iterations return designition 
    if i%2==0:
        val=vb.split("\n")
        designation.append(val[0].strip())
        if len(val)==3:
            hec_approved_phd_supervisor.append(1)
        else:
            hec_approved_phd_supervisor.append(0)
    #At odd iterations return emails
    else:
        emails.append(vb)
        
        
            
            
    
    


# In[21]:


designation[0:3]


# In[22]:


emails[0:3]


# In[23]:


faculty_profile_link=[]


# In[24]:


#links to check profile
links=card.find_all('a')


# In[25]:


for link in links:
    
     faculty_profile_link.append(link["href"])


# In[26]:


faculty_profile_link[0:3]


# In[120]:


faculty_profile=[]
education=[]
phone_no=[]


# In[121]:


url1="http://lhr.nu.edu.pk/"
for url in faculty_profile_link:

    url=url[1:]

    new_url=url1+url
    print(new_url)
    profile=requests.get(str(new_url))
    print(profile.status_code)
    soup1=BeautifulSoup(profile.content,"html.parser")
    card1=soup1.find("div",class_="container")
    edu=card1.select("li")
    for i in range(len(edu)):
        edu[i]=edu[i].get_text(strip="True")
                   
    education.append(edu)

    kl=card1.find("span",class_="small").get_text(strip="True")   #for phone
    phone_no.append(kl)
    lk=card1.find("p" ,class_="text-justify")
    if lk is not None:
        lk=lk.get_text(strip="True") #for profile
        faculty_profile.append(lk)
    else: 
        faculty_profile.append("Profile_Not_Available")

    

    
    


# In[ ]:


designation
hec_approved_phd_supervisor #1 means true 0 means false
emails
name
faculty_profile
education
phone_no
image_link
faculty_profile_link


# In[129]:


for i in range(len(name)):
    intro1="My name is {name} .I am a {desig} at FAST NU Lahore. Here is the list of my degrees:\n {edu} and \n A little intro:\n {prof}. \n If any one contact me, he/she can contact me on phone {phone_no} and also on email {email}".format(name=name[i],desig=designation[i],edu=education[i],prof=faculty_profile[i],phone_no=phone_no[i],email=emails[i])
    print(intro1)
    if hec_approved_phd_supervisor[i]==1:
        print("One more thing I am also HEC Approved PHD Supervisor")
    link="This is my image link{img_lnk}\n and profile link{prof_lnk}".format(img_lnk=image_link[i],prof_lnk=faculty_profile_link[i])
    print(link)
    


# In[ ]:




