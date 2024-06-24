pipeline {
  agent {
        docker {
            image 'python:3.12-alpine'
            args '--network host'
        }
    }
  stages {
    stage('checkout') {
      steps {
        checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/serkuksov/Jenkins-test.git']])
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