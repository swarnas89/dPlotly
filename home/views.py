from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from home.getdata import getConfTitles,getConfData
from home.ke_examlple import getKeywordsFromConcatenatedAbstractAndTitle
from home.wiki_example import getWikiFilteredWords
from plotly.offline import plot
from home.similarity_example import getSimilarityScores
from home.chart import getBcharts,barChart
import plotly.graph_objects as go

def home(requests):
    return render(requests,'home/welcome.html',{"ConfNames":getConfTitles()})
def charts(requests):
    return render(requests,'home/plot.html')
def graphView(requests):
    return render(requests,'home/graphs.html')
def bubbleView(requests):
    return render(requests,'home/bubbleplot.html')
def getListValues(request,num):
    #dropdown_value = "Teaching the unteachable: on the compatibility of learning analytics and humane education"
    year_dropdown=request.POST.get('exampleFormControlSelect1')
    t1=request.POST.get('exampleFormControlSelect2')
    print("The selected year is:",year_dropdown)
    t2=t1.replace("'","")
    #print("The value is" ,t2)
    val=getConfData(t2)
    #print("data is:",val)
    return render(request,'home/welcome.html',{"ConfNames":getConfTitles(),"ConfDetails":val})
def getCharts(request):
    return render(request,'home/bubbles_tpc.html',{'plot_div':getBcharts(),'plot_div1':barChart(),'concats':getKeywordsFromConcatenatedAbstractAndTitle(),'wiki':getWikiFilteredWords(),'simscore':getSimilarityScores()})



