pipeline {
  agent any
  stages {
    stage('Cloning repository') {
      steps {
        checkout scm
      }
    }
    stage('Install Dependencies and Run Tests') {
            steps {
                withPythonEnv('my-virtual-env') {
                    sh 'pip install -r requirements.txt'
                    sh 'chmod +x test_runner.sh'
                    sh './test_runner.sh'
                }
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