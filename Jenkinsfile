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
        PATH=$PATH:/usr/local/bin/
        echo $PATH
        python3 searchAndTest.py
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
