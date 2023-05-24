pipeline {
  agent any
  stages {
    stage('buzz build') {
      steps {
        archiveArtifacts(artifacts: 'target/*.jar', fingerprint: true)
      }
    }

    stage('buzz test') {
      agent any
      environment {
        BUZZ_NAME = 'Wroker Bee'
      }
      steps {
        sh '''echo I am a $BUZZ_NAME
./jenkins/build.sh'''
      }
    }

  }
}