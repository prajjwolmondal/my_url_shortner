[![my_url_shortner](https://circleci.com/gh/prajjwolmondal/my_url_shortner.svg?style=shield)](https://app.circleci.com/pipelines/github/prajjwolmondal/my_url_shortner)  [![Known Vulnerabilities](https://snyk.io/test/github/prajjwolmondal/my_url_shortner/badge.svg)](https://snyk.io/test/github/prajjwolmondal/my_url_shortner)

# My URL Shortner

A simple app that shortens URLs, like bit.ly (Project is still WIP)

My focus on this project was to try out technologies that I didn't try out in the past. Mainly, I wanted to try out having a project with a CI pipeline that would run tests against the incoming code changes. 

## Technologies used

- [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask) - provided a great flask template with all the bells and whistles attached
- [flask](flask.palletsprojects.com/) - the framework of choice for the backend
- [MySQL](https://www.mysql.com/) - the database
- [pytest](https://docs.pytest.org/en/latest/) - used for the unit tests
- [circleci](circleci.com/) - the CI for this project. I saw CircleCI mentioned on a lot of job postings so I decided to check it out. I love the [debug with ssh](https://circleci.com/docs/2.0/ssh-access-jobs/) feature.
- [docker](https://www.docker.com/)
- [bootstrap](https://getbootstrap.com/) - for the site styling