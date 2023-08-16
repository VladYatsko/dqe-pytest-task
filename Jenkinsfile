pipeline {
  agent any
  stages {
    stage('Install Dependencies and Run Tests') {
      steps {
        script {
          sh "pip install -r requirements.txt"
        }
      }
    }
    stage('Create, copy in new branch') {
      steps {
        sh 'git branch -D pre-prod'
        sh 'git checkout -b pre-prod'
        sh 'touch somefile'
        sh 'git add .'
        sh 'git status'
        sh 'git config --global user.name "Uladzislau Yatsko"'
        sh 'git config --global user.email "uladzislau_yatsko@epam.com"'
        sh 'git commit -m "Pushing to pre-prod"'
      }
    }
    stage('Push to pre-prod') {
      steps {
        script {
            sshagent (credentials: ['VladYatskoSSH']){
                sh 'git branch'
                sh 'git remote set-url origin git@github.com:VladYatsko/dqe-pytest-task.git'
                sh 'git push origin pre-prod'
            }
        }
      }
    }
  }
}