pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        git branch: 'main', url: 'https://github.com/solomonpaul/testMail.git'
        sh 'python3 text_Mail.py'
      }
    }
  }
}
