pipeline {
  agent {
        docker {
            image 'python:3.12-alpine'
            args '-v /tmp:/tmp --network host'
        }
    }
  stages {
    stage('clone') {
      steps {
        sh 'git pull'
      }
    }

    stage('installing dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Tests') {
      steps {
        sh 'pytest -sv --alluredir=allure-results'
      }
    }
  }
}