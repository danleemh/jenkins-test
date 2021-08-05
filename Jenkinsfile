pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "Building..."
        sleep 2
        echo "Building... Done"'''
      }
    }
    stage('Test') {
      steps {
        sh '''
        echo "Testing..."
        sleep 2
        echo "Testing... Done"
        '''
      }
    }
    stage('Collect Test Result') {
      steps {
        sh '''echo "Collecting..."
        sleep 2
        echo "Collecting... Done"'''
      }
    }

  }
}
