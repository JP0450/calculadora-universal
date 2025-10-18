pipeline {
  agent any

  options {
    timestamps()
    ansiColor('xterm')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          if (isUnix()) {
            sh 'docker build -t calculadora-universal:test .'
          } else {
            bat 'docker build -t calculadora-universal:test .'
          }
        }
      }
    }

    stage('Run Tests in Docker') {
      steps {
        script {
          if (isUnix()) {
            sh 'docker run --rm calculadora-universal:test'
          } else {
            bat 'docker run --rm calculadora-universal:test'
          }
        }
      }
    }
  }

  post {
    always {
      script {
        if (isUnix()) {
          sh 'docker images | head -n 20 || true'
        } else {
          bat 'docker images'
        }
      }
    }
  }
}
