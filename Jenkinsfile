pipeline {
  agent any
  stages {
    stage('fluffy build') {
      parallel {
        stage('fluffy build') {
          steps {
            sh './jenkins/build.sh'
          }
        }

        stage('fluffy test') {
          steps {
            sh './jenkins/test-all.sh'
          }
        }

        stage('fluffy deploy') {
          steps {
            sh './jenkins/deploy.sh staging'
          }
        }

      }
    }

  }
}