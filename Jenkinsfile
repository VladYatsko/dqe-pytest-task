pipeline {
  agent any
  stages {
    stage('Cloning repository') {
      steps {
        checkout scm
      }
    }
    stage('Installing required libraries') {
      steps {
        echo 'Installing required libraries'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test phase') {
      steps {
        echo 'Testing phase'
        sh 'chmod +x test_runner.sh'
        sh './test_runner.sh'
      }
    }
    stage('Create, copy and push in new branch') {
      steps {
        sh 'git checkout -b pre-prod'
        sh 'git add .'
        sh 'git config --global user.name "Uladzislau Yatsko"'
        sh 'git config --global user.email "uladzislau_yatsko@epam.com"'
        sh 'git commit -m "Pushing to pre-prod"'
        sh 'git push origin '
      }
    }
  }
}