<p align="center">
    <img style="margin: 0 0 0 60px" src="/wireframe/banner_2.png" alt="formica banner"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>  
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://camo.githubusercontent.com/caf9d3251680e742d78d1caf78b151140a3498a8cbd6b0877246c1f5217743fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4669676d612532302d2532334632344531452e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d4669676d61266c6f676f436f6c6f723d7768697465"/>
</p>



<h2 align="center" style="font-weight:bold">Project Description</h2>
<p align="center">
Several communities have joined Discord, with over 6.7 million servers existing on discord, the need for proper form analytics has increased, while most communities use Google forms or other third-party forms to analyze and visualize data, I believe that we can leverage Discord API to allow users to fill forms without leaving discord while also providing useful analytics to the Admin who created the form. This helps admins and mods to view the data via the discord bot or web interface, whichever is convenient
</p>
<p align="center">
Collection of form data is often not taken seriously, you are providing information to be collected by one organisation but you have no idea where all the data is going to be circulated, There needs to be transparency in regards to sharing of form data to the user. Formica allows sharing of collected form data among communities also notifying users and letting them know that the data submitted on a form is being shared to another community, So the user can chose to delete his data from the shared form data.
</p>


<h2 align="center" style="font-weight:bold">Web Interface</h2>
<p align="center">
<img src="https://i.imgur.com/aHZr15T.gif">
</p>



<h2 align="center" style="font-weight:bold">Discord Bot</h2>
<p align="center">
<img src="https://i.imgur.com/PmphjEm.gif">
</p>


<h2 align="center" style="font-weight:bold">Backend and Frontend Setup</h2>


```bash

# Add Client ID and Secret Key 
cd formica/backend/API
touch .env
nano .env
CLIENT_ID= <ClientID> 
CLIENT_SECRET= <ClientSecret> 

#Run using Docker
cd formica
docker-compose build 
docker-compose up

```


<h2 align="center" style="font-weight:bold">Discord Bot Setup</h2>


```bash

#Add Bot Secret key
cd formica/bot
touch .env 
nano .env 
TOKENT = <BotToken>

#Run the bot 
python formica_bot.py

```


<h2 align="center" style="font-weight:bold" id="contributing">Project Demo</h2>

<p align="center" style="margin: 20px 0 30px 0">
Formica is a project for Sprint 2 of  the MLH Fellowship. Here's a demo video that was made for the submission. This might help you understand the project better.
  <a href="https://youtu.be/yiLA9oJ-O-s" target="#">
    Demo Video
  </a>
</p>  


<h2 align="center" style="font-weight:bold">Contribution</h2>
<p align="center">
    Check out our <a href="/CONTRIBUTING.md">Contributions Guidelines</a>
</p>
