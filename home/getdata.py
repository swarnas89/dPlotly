import pandas as pd 
import numpy as np

data_conf = pd.read_csv(r"E:\Master Thesis\LA\Repos\dPlotly\dPlotly\static\assets\dataset.csv")
data_conf['ProcessedTitle'] = data_conf['title'].map(lambda x: x.replace(",",""))
#data_conf['ProcessedTitle'] = data_conf['ProcessedTitle'].map(lambda x: x.replace("'",""))

def getConfTitles():
    
    list_years=list(data_conf['year'].values)
    list_titles=list(data_conf['ProcessedTitle'].values)
    dictionary = {}
    for i, j in zip(list_years, list_titles):
        dictionary.setdefault(i, []).append(j)
    return dictionary
def getConfData(title):
    #print("The value inside function is :",title)
    title=title.lstrip()
    #data_conf.set_index('ProcessedTitle')
    #print("the  df is",data_conf.loc[title,:])
    #values_title=data_conf.query('ProcessedTitle=="'+title+'"')
    values_title1=data_conf.loc[data_conf['ProcessedTitle'] == title]
    #print(values_title1)
    #print("The values title is:",values_title1)
    values_dic=values_title1.set_index('ProcessedTitle').T.to_dict('list')
    #print(values_dic)
    return values_dic
def getKeywords(title):
    return list(getConfData(title).values())[0][8]
def getDataFrame():
    return data_conf
def concatTitleAndAbstract():
    data_concat=data_conf
    data_concat["titleandabstract"] = data_concat["ProcessedTitle"] +" "+data_concat["abstract"]
    return data_concat['titleandabstract'].values
#print(concatTitleAndAbstract()[0])


#values=getKeywords(" Supporting teachers intervention in students virtual collaboration using a network based model".lstrip())
#print(values)
#d=getConfTitles()
#print(d)