pipeline {
  agent {
    docker {
      image 'python:3.8'
      args '-u'
    }
  }
  stages {
    stage('Install Dependencies and Run Tests') {
      steps {
        sh "pip install -r requirements.txt"
        sh "pytest --alluredir=results --reruns 5 ./tests/"
      }
    }
    stage('Create, copy and push in new branch') {
      steps {
        sh 'git checkout -b pre-prod'
        sh 'git add .'
        sh 'git config --global user.name "Uladzislau Yatsko"'
        sh 'git config --global user.email "uladzislau_yatsko@epam.com"'
        sh 'git commit -m "Pushing to pre-prod"'
        sh 'git push origin pre-prod'
      }
    }
  }
}