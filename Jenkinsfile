pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        sh 'git clone https://github.com/serkuksov/Jenkins-test.git'
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