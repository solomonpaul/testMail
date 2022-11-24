pipeline {
    agent {
      docker {
        image 'python:3'
        label 'my-build-agent'
      }
    }
    stages {
        stage('Test') {
            steps {
              sh """
              python --version
              python ./text_Mail.py
              """
            }
        }
    }
}
