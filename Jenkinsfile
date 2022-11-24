pipeline {
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
