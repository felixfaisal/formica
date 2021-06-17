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


<h2 align="center" style="font-weight:bold">Contribution Guidelines 🏗</h2>

Are we missing any of your favorite features, which you think you can add to it❓ We invite you to contribute to this project and improve it further

To start contributing, follow the below guidelines: 

🌟. Star🌟 the project to bookmark and appreciate the work.

<em> Take a look at the existing [issues](https://github.com/felixfaisal/formica/issues) or create your own issues. Wait for the Issue to be assigned to you after which you can start working on it. </em>


**1.**  Fork [this](https://github.com/felixfaisal/formica.git) repository.

**2.**  Clone your forked copy of the project.

```
git clone --depth 1 https://github.com/<your_user_name>/formica.git
```

**3.** Navigate to the project directory :file_folder: .

```
cd formica
```

**4.** Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/felixfaisal/formica.git
```

**5.** Check the remotes for this repository.

```
git remote -v
```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository) and install the requirements to run the code.

```
git pull upstream main
npm install
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Perform your desired changes to the code base.


**9.** Track your changes:heavy_check_mark: .

```
git add . 
```

**10.** Commit your changes .

```
git commit -m "Relevant message"
```

**11.** Check for your changes .

```
git status
```

**12.** Push the committed changes in your feature branch to your remote repo.

```
git push -u origin <your_branch_name>
```

**13.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.

**14.** Add appropriate title and description to your pull request explaining your changes and efforts done.

**15.** Click on `Create Pull Request`.

**16.** Voila :exclamation: You have made a PR to the website :boom: . Sit back patiently and relax while the project maintainers review your PR. Please understand, at timesthe time taken to review a PR can vary from a few hours to a few days.



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

<center>

## 📌 Opensource Programs

### This project is a part of following Open Source Program
<br>
</center>

<table style="width:80%;background-color:white;border-radius:30px;">
    <tr>
  <td>
<center>
  <a href="https://letsgrowmore.in/soc/"><img src="https://letsgrowmore.in/wp-content/uploads/2021/05/cropped-growmore-removebg-preview.png"></img></a>
  </center>
  </td>
  </tr>
</table>
    <hr>
</p>
<br>
<h2 align="center" style="font-weight:bold">Code of Conduct</h2><br>
<p align="center">
<a href="https://github.com/felixfaisal/formica/blob/main/CODE_OF_CONDUCT.md "> 
<h5 align="center"><b>Click to read</b></a>  

<br>
<h2 align="center" style="font-weight:bold">Project Admin👨‍</h2>
<br>
<p align="center">
<img width=20% src="https://avatars.githubusercontent.com/u/42486737?v=4">
</p>
<a href="https://www.linkedin.com/in/faisal-ahmed-farooq-6395a0174/">
<h5 align="center"><b>Felix Faisal</b></a>

<br>    
<h2 align="center" style="font-weight:bold">License </h2>
<br>
<p align="center">
<a href="https://github.com/felixfaisal/formica/blob/main/LICENSE"></p>
<h5 align="center"><b>MIT License</b></a>
