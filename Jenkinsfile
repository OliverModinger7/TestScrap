pipeline {
  agent any
  stages {
    stage('buzz build') {
      steps {
        sh './jenkins/build.sh'
      }
    }

    stage('buzz test') {
      steps {
        sh './jenkins/test-all.sh'
      }
    }

  }
}