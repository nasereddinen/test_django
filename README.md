# Introduction

Full stack Test Chez Volto


### installation

Pour installer le projet suivre les etapes suivants:

```sh
git clone <URL>
```
you have to install the project in a zip format and then initialize the .git inside the project



Le projet utilise mysql comme DB et comme port :3306  dans le ficher settings.py :

```sh
DATABASES = {
    'default': {
        .......
        'PORT': '3306'
    }
}

```

### virtualenv

> Requirements:
>     vous avez besion de `Python3.10` et `Python3.10-dev` installer dans votre  machine
>     Installer mkvirtualenv, personnellement J'ai préféré cette méthode.
1- Create virtualenv.

```sh
mkvirtualenv -a  projet_test 
```
```sh
workon projet_test
```
2- Installer tout les bibliothéques

```sh
pip install -r requirements.txt
```
### Start the project

apres le changement necessaires (collectstatic and migrations) excuter la command:

```bash
python manage.py runserver
```
### Documentation
>Presentation de projet (J'ai ajouté une application de Visualtion)
```sh
.
├── core
├── authentication
├── voltocms
├── visualisation
├── requirements.txt
├── templates

```



