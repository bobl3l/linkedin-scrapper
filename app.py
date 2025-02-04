from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import plotly.utils
import json
from datetime import datetime
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)



divisions=["cyber security","cloud","data analyst","full stack","frontend","backend","QA/Test","DevOps","Web","Mobile","System Administrator","Quant","AI"]
languages=["JavaScript","TypeScript","HTML/CSS","SQL","Python","Java","C++","C#","Ruby","Kotlin","Go","Objective-C","Flutter","Swift","Scala","PHP","R"]
techs=["React","Next","LLM","AI","CMS","Wordpress","Node","AWS","Node","Angular","Redux","Django","Flask",".NET","Spring","Vue","Express"]

def numbers_scrapper(context):
    context = context.replace(" ", "%20")
    jobs_url = f"https://www.linkedin.com/jobs/search?keywords={context}&location=United%20Kingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    response = requests.get(jobs_url)
    job_soup = BeautifulSoup(response.text, 'html.parser')
    job_number = job_soup.find('span',{'class':"results-context-header__job-count"}).text.strip()
    job_number = job_number.replace('+',"")
    return job_number
def job_scrapper():
    info_url="https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=United%20Kingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    job_fetched = 0
    response = requests.get(info_url)
    job_soup = BeautifulSoup(response.text, 'html.parser')
    job_number = job_soup.find('span',{'class':"results-context-header__job-count"}).text.strip()
    job_number = job_number.replace('+',"")
    job_number_int=int(job_number)

    id_list=[]
    while job_fetched < job_number_int:
        scrapping_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=software%2Bengineer&location=United%2BKingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&start={job_fetched}"
        response = requests.get(scrapping_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listing = soup.find_all('li')
        for job in job_listing:
            base_card_div = job.find('div',{"class": "base-card"})
            job_id = base_card_div.get("data-entity-urn").split(":")[3]
            id_list.append(job_id)
        if len(id_list)%10==0 and len(id_list)!=0:
            job_fetched+=10
        else:
            break

    job_list=[]

    for job_id in id_list:
        job_url=f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
        job_response = requests.get(job_url)
        job_soup=BeautifulSoup(job_response.text,"html.parser")
        job_post={}
        job_post["company_name"]=job_soup.find("a",{"class":"topcard__org-name-link topcard__flavor--black-link"}).text.strip()
        job_post["location"]=job_soup.find("span",{"class":"topcard__flavor topcard__flavor--bullet"}).text.strip()
        job_post["post_date"]=job_soup.find("span",{"class":"posted-time-ago__text topcard__flavor--metadata"}).text.strip()
        job_post["job_description"]=job_soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative overflow-hidden"}).get_text(separator=' ').strip()
        job_list.append(job_post)


@app.route('/')
def index():
    return render_template("index.html")

role_graph = dash.Dash(__name__, server=app, url_base_pathname="/roles/")
@app.route("/roles/")
def roles():
    role_number = {}
    for div in divisions:
        role_number[div]=numbers_scrapper(div).replace(",","")
        role_number[div]=int(role_number[div])

    sorted_items = sorted(role_number.items(), key=lambda item: item[1])  
    labels, values = zip(*sorted_items)  

    # Step 4: Create the Dash Figure (Horizontal Bar Chart)
    fig = go.Figure(go.Bar(
        y=labels,
        x=values,
        orientation='h',
        marker=dict(color="steelblue")
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, range=[0, max(values) * 1.1]),
        yaxis=dict(showgrid=False),
        title="Horizontal Bar Chart (Sorted Lowest to Highest)"
    )

    # Step 5: Layout for Dash App
    role_graph.layout = html.Div(children=[
        html.H1("Dash Graph in Flask"),
        dcc.Graph(figure=fig,config={"displayModeBar": False})
    ])
    
    return role_graph.index()  # Serve Dash within Flask

lang_graph = dash.Dash(__name__, server=app, url_base_pathname="/languages/")
@app.route("/languages/")
def languages():
    language_count = {}
    for lang in languages:
        language_count[lang]=numbers_scrapper(lang).replace(",","")
        language_count[lang]=int(language_count[lang])

    sorted_items = sorted(language_count.items(), key=lambda item: item[1])  
    labels, values = zip(*sorted_items)  

    # Step 4: Create the Dash Figure (Horizontal Bar Chart)
    fig = go.Figure(go.Bar(
        y=labels,
        x=values,
        orientation='h',
        marker=dict(color="steelblue")
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, range=[0, max(values) * 1.1]),
        yaxis=dict(showgrid=False),
        title="Horizontal Bar Chart (Sorted Lowest to Highest)"
    )

    # Step 5: Layout for Dash App
    lang_graph.layout = html.Div(children=[
        html.H1("Dash Graph in Flask"),
        dcc.Graph(figure=fig,config={"displayModeBar": False})
    ])
    
    return lang_graph.index()  # Serve Dash within Flask

tech_graph = dash.Dash(__name__, server=app, url_base_pathname="/tech/")
@app.route("/tech/")
def tech():
    tech_count = {}
    for tech in techs:
        tech_count[tech]=numbers_scrapper(tech).replace(",","")
        tech_count[tech]=int(tech_count[tech])

    sorted_items = sorted(tech_count.items(), key=lambda item: item[1])  
    labels, values = zip(*sorted_items)  

    # Step 4: Create the Dash Figure (Horizontal Bar Chart)
    fig = go.Figure(go.Bar(
        y=labels,
        x=values,
        orientation='h',
        marker=dict(color="steelblue")
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, range=[0, max(values) * 1.1]),
        yaxis=dict(showgrid=False),
        title="Horizontal Bar Chart (Sorted Lowest to Highest)"
    )

    # Step 5: Layout for Dash App
    tech_graph.layout = html.Div(children=[
        html.H1("Dash Graph in Flask"),
        dcc.Graph(figure=fig,config={"displayModeBar": False})
    ])
    
    return tech_graph.index()  # Serve Dash within Flas

if __name__ == '__main__':
    app.run(debug=True)