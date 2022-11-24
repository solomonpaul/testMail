pipeline {
    agent {
      docker {
        image 'python:3'
        label 'agent1'
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
