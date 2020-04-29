
# coding: utf-8

# In[77]:


#We start importing the modules that we will need.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[78]:


#Import the dataset
df = pd.read_csv("/home/aruiz/RRSC/test_answers_2.csv", header=0)


# In[79]:


df.set_index('Number_participant', inplace=True)


# In[80]:


#G:GRAPHENE


# In[81]:


bins = np.arange(8) - 0.5
plt.hist(df["Show_def_knowledge_before"], bins, edgecolor='black', linewidth=1.2)
plt.title("Participants' general knowledge about graphene before the activity")
plt.ylabel("Number of participants")
plt.xlabel("Number of graphene-related features that participants are able to define")
plt.xticks(range(7),('0', '1', '2', '3', '4', '5', 'NS/NC'))
plt.xlim([-0.5, 6.5])
plt.show()
plt.savefig('Figure1.png')


# In[82]:


bins = np.arange(8) - 0.5
plt.hist(df["Show_def_increase_knowledge"], bins, edgecolor='black', linewidth=1.2)
plt.title("Participants' general learning about graphene through the activity")
plt.ylabel("Number of participants")
plt.xlabel("Number of graphene-related features that participants learn as new")
plt.xticks(range(7),('0', '1', '2', '3', '4', '5', 'NS/NC'))
plt.xlim([-0.5, 6.5])
plt.show()
plt.savefig('Figure2.png')


# In[83]:


#R:RESEARCH


# In[84]:


bins = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
plt.hist(df["Show_research_society_before"], bins, edgecolor='black', linewidth=1.2)
plt.title("General perception on societal importance of research activities (before)")
plt.ylabel("Number of participants")
plt.xlabel("Level of agreement with the importance of research in society")
plt.xticks((-2,-1,0,1,2,3),('Completely disagree', 'Partially disagree', 'Neutral', 'Agree', 'Completely agree', 'NS/NC'), rotation=20)
plt.xlim([-2.5, 3.5])
plt.show()
plt.savefig('Figure3.png')


# In[85]:


fig, ax = plt.subplots()
data = df["Show_impact_research_society"]
bins = np.arange(-4.5, 6.5, 1).tolist()
N, bins, patches = ax.hist(data, bins, edgecolor='black', linewidth=1.2)

plt.title("Impact of the activity on the perception of societal importance of research")
plt.ylabel("Number of participants")
plt.xlabel("Impact level")
plt.xticks((-4,-3,-2,-1,0,1,2,3,4,5),('Huge', 'Considerable', 'Moderated', 'Slight','No impact', 'Slight','Moderated', 'Considerable', 'Huge','NS/NC'), rotation=30)
plt.xlim([-4.5, 5.5])

patches[0].set_facecolor('darkred')
patches[1].set_facecolor('brown')
patches[2].set_facecolor('indianred')
patches[3].set_facecolor('lightcoral')
patches[4].set_facecolor('w')
patches[5].set_facecolor('aquamarine')
patches[6].set_facecolor('turquoise')
patches[7].set_facecolor('lightseagreen')
patches[8].set_facecolor('darkcyan')

plt.show()
plt.savefig('Figure4.png')


# In[86]:


#A:APPLICATION


# In[87]:


bins = np.arange(-0.5, 5.5, 1).tolist()
plt.hist(df["Show_apps_before"], bins, edgecolor='black', linewidth=1.2)
plt.title("Number of applications of graphene that participants mention before the activity")
plt.ylabel("Number of participants")
plt.xlabel("Number of correct applications")
plt.xticks((0,1,2,3,4),('None', '1', '2 or 3', 'More than 3','NS/NC'), rotation=20)
plt.xlim([-0.5, 4.5])
plt.show()
plt.savefig('Figure5.png')


# In[88]:


bins = np.arange(-0.5, 5.5, 1).tolist()
plt.hist(df["Show_learnt_apps"], bins, edgecolor='black', linewidth=1.2)
plt.title("Number of applications of graphene that participants learn through the activity")
plt.ylabel("Number of participants")
plt.xlabel("Number of correct applications")
plt.xticks((0,1,2,3,4),('None', '1', '2 or 3', 'More than 3','NS/NC'), rotation=20)
plt.xlim([-0.5, 4.5])
plt.show()
plt.savefig('Figure6.png')


# In[89]:


#P:POLITICS


# In[90]:


x1=[]
y1=[]
x2=[]
y2=[]
for i in df.index:
    if df.loc[i, "World_before"] ==1:
        x1.append(i)
        y1.append(6)
for i in df.index:
    if df.loc[i, "Continental_before"] ==1:
        x1.append(i)
        y1.append(5)
for i in df.index:
    if df.loc[i, "Country_before"] ==1:
        x1.append(i)
        y1.append(4)
for i in df.index:
    if df.loc[i, "Regional_before"] ==1:
        x1.append(i)
        y1.append(3)
for i in df.index:
    if df.loc[i, "Local_before"] ==1:
        x1.append(i)
        y1.append(2)
for i in df.index:
    if df.loc[i, "Scientists_before"] ==1:
        x1.append(i)
        y1.append(1)
for i in df.index:
    if df.loc[i, "Others_before"] ==1:
        x1.append(i)
        y1.append(7)
for i in df.index:
    if df.loc[i, "P_NR/DK_before"] ==1:
        x1.append(i)
        y1.append(8)
for i in df.index:
    if df.loc[i, "World_after"] ==1:
        x2.append(i)
        y2.append(6)
for i in df.index:
    if df.loc[i, "Continental_after"] ==1:
        x2.append(i)
        y2.append(5)
for i in df.index:
    if df.loc[i, "Country_after"] ==1:
        x2.append(i)
        y2.append(4)
for i in df.index:
    if df.loc[i, "Regional_after"] ==1:
        x2.append(i)
        y2.append(3)
for i in df.index:
    if df.loc[i, "Local_after"] ==1:
        x2.append(i)
        y2.append(2)
for i in df.index:
    if df.loc[i, "Scientists_after"] ==1:
        x2.append(i)
        y2.append(1)
for i in df.index:
    if df.loc[i, "Others_after"] ==1:
        x2.append(i)
        y2.append(7)
for i in df.index:
    if df.loc[i, "P_NR/DK_after"] ==1:
        x2.append(i)
        y2.append(8)

ax = plt.gca()
ax.scatter(x1, y1, color="b", alpha=0.75, s=50)
ax.scatter(x2, y2, color="r", alpha=0.35, s=300)
plt.title("Participants' opinion on suitable level of scientific politics decisions")
plt.yticks((1,2,3,4,5,6,7,8),('Scientists', 'Local', 'Regional', 'Country','Continental', 'World', 'Others', 'NS/NC'), rotation=0)
plt.ylabel("Decision's level")
plt.xlabel("Participant")
plt.ylim([0.5, 8.5])
plt.show()
plt.savefig('Figure7.png')


# In[91]:


#H:HORIZON


# In[92]:


bins = np.arange(-0.5, 4.5, 1).tolist()
plt.hist(df["Show_horizon_before"], bins, edgecolor='black', linewidth=1.2)
plt.title("Accuracy of the definition of H2020 framework before the activity")
plt.ylabel("Number of participants")
plt.xlabel("Level of accuracy")
plt.xticks((0,1,2,3),('Incorrect/Unkwown', 'Partially correct', 'Correct', 'NS/NC'), rotation=20)
plt.xlim([-0.5, 3.5])
plt.show()
plt.savefig('Figure8.png')


# In[93]:


bins = np.arange(-0.5, 4.5, 1).tolist()
plt.hist(df["Show_increase_horizon"], bins, edgecolor='black', linewidth=1.2)
plt.title("Improvement in the accuracy of the definition of H2020 framework through the activity")
plt.ylabel("Number of participants")
plt.xlabel("Level of accuracy")
plt.xticks((0,1,2,3),('No improvement', 'Partial improvement', 'Huge improvement', 'NS/NC'), rotation=20)
plt.xlim([-0.5, 3.5])
plt.show()
plt.savefig('Figure9.png')


# In[94]:


X11=[]
Y11=[]
X22=[]
Y22=[]
for i in df.index:
    if df.loc[i, "Health_before"] ==1:
        X11.append(i)
        Y11.append(1)
    if df.loc[i, "Fundamental_before"] ==1:
        X11.append(i)
        Y11.append(2)
    if df.loc[i, "Materials_before"] ==1:
        X11.append(i)
        Y11.append(3)
    if df.loc[i, "Environmental_before"] ==1:
        X11.append(i)
        Y11.append(4)
    if df.loc[i, "H_others_before"] ==1:
        X11.append(i)
        Y11.append(5)
    if df.loc[i, "H2_NR/DK_before"] ==1:
        X11.append(i)
        Y11.append(6)
    if df.loc[i, "Health_after"] ==1:
        X22.append(i)
        Y22.append(1)
    if df.loc[i, "Fundamental_after"] ==1:
        X22.append(i)
        Y22.append(2)
    if df.loc[i, "Materials_after"] ==1:
        X22.append(i)
        Y22.append(3)
    if df.loc[i, "Environmental_after"] ==1:
        X22.append(i)
        Y22.append(4)
    if df.loc[i, "H_others_before"] ==1:
        X22.append(i)
        Y22.append(5)
    if df.loc[i, "H2_NR/DK_after"] ==1:
        X22.append(i)
        Y22.append(6)
ax = plt.gca()
ax.scatter(X11, Y11, color="b", alpha=0.75, s=50)
ax.scatter(X22, Y22, color="r", alpha=0.35, s=300)
plt.title("Desired scientific areas related to major H2020 investment")
plt.yticks((1,2,3,4,5,6),('Health', 'Fundamental', 'Materials', 'Environmental','Others', 'NS/NC'), rotation=0)
plt.ylabel("Scientific field")
plt.xlabel("Participant")
plt.ylim([0.5, 6.5])
plt.show()
plt.savefig('Figure10.png')


# In[95]:


#E:ECONOMICS


# In[96]:


x11=[]
y11=[]
x22=[]
y22=[]
for i in df.index:
    if df.loc[i, "Comparative_before"] ==1:
        x11.append(i)
        y11.append(1)
    if df.loc[i, "Comparative_before"] ==0:
        x11.append(i)
        y11.append(0)
    if df.loc[i, "Comparative_before"] ==-1:
        x11.append(i)
        y11.append(-1)
    if df.loc[i, "E_NR/DK_before"] ==1:
        x11.append(i)
        y11.append(2)
    if df.loc[i, "Comparative_after"] ==1:
        x22.append(i)
        y22.append(1)
    if df.loc[i, "Comparative_after"] ==0:
        x22.append(i)
        y22.append(0)
    if df.loc[i, "Comparative_after"] ==-1:
        x22.append(i)
        y22.append(-1)
    if df.loc[i, "E_NR/DK_after"] ==1:
        x22.append(i)
        y22.append(2)
ax = plt.gca()
ax.scatter(x11, y11, color="b", alpha=0.75, s=50)
ax.scatter(x22, y22, color="r", alpha=0.35, s=300)
plt.title("Desired relative value of %GDP invested in science respect the actual one")
plt.yticks((-1,0,1,2),('Lower', 'Equal', 'Higher', 'NS/NC'), rotation=0)
plt.ylabel("Desired relative value")
plt.xlabel("Participant")
plt.ylim([-1.5, 2.5])
plt.show()
plt.savefig('Figure11.png')


# In[97]:


#N:NEGATIVE


# In[98]:


x111=[]
y111=[]
x222=[]
y222=[]
for i in df.index:
    if df.loc[i, "Investment_before"] ==1:
        x111.append(i)
        y111.append(1)
for i in df.index:
    if df.loc[i, "Environment_before"] ==1:
        x111.append(i)
        y111.append(2)
for i in df.index:
    if df.loc[i, "Ethics_before"] ==1:
        x111.append(i)
        y111.append(3)
for i in df.index:
    if df.loc[i, "Risks_before"] ==1:
        x111.append(i)
        y111.append(4)
for i in df.index:
    if df.loc[i, "Others_before"] ==1:
        x111.append(i)
        y111.append(5)
for i in df.index:
    if df.loc[i, "N_NR/DK_before"] ==1:
        x111.append(i)
        y111.append(6)
for i in df.index:
    if df.loc[i, "Investment_after"] ==1:
        x222.append(i)
        y222.append(1)
for i in df.index:
    if df.loc[i, "Environment_after"] ==1:
        x222.append(i)
        y222.append(2)
for i in df.index:
    if df.loc[i, "Ethics_after"] ==1:
        x222.append(i)
        y222.append(3)
for i in df.index:
    if df.loc[i, "Risks_after"] ==1:
        x222.append(i)
        y222.append(4)
for i in df.index:
    if df.loc[i, "Others_after"] ==1:
        x222.append(i)
        y222.append(5)
for i in df.index:
    if df.loc[i, "N_NR/DK_after"] ==1:
        x222.append(i)
        y222.append(6)

ax = plt.gca()
ax.scatter(x111, y111, color="b", alpha=0.75, s=50)
ax.scatter(x222, y222, color="r", alpha=0.35, s=300)
plt.title("Participant's opinion about negative aspects of science")
plt.yticks((1,2,3,4,5,6),('Investment return', 'Enviromental risk', 'Ethics', 'Danger','Others', 'NS/NC'), rotation=0)
plt.ylabel("Negative aspect")
plt.xlabel("Participant")
plt.ylim([0.5, 6.5])
plt.show()
plt.savefig('Figure12.png')

