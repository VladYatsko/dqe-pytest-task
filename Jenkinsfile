pipeline {
  agent any
  stages {
    stage('Install Dependencies and Run Tests') {
      steps {
        script {
          sh "pip install -r requirements.txt"
          sh "pytest --alluredir=results --reruns 5 ./tests/"
        }
      }
    }
    stage('Create, copy in new branch') {
      steps {
        sh 'git checkout -b pre-prod'
        sh 'git add .'
        sh 'git config --global user.name "Uladzislau Yatsko"'
        sh 'git config --global user.email "uladzislau_yatsko@epam.com"'
        sh 'git commit -m "Pushing to pre-prod"'
    }
    stage('Push to pre-prod') {
            steps {
                script {
                    withEnv(['GIT_TOKEN=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']) {
                        sh 'git push origin pre-prod'
                    }
                }
            }
        }
      }
    }
}