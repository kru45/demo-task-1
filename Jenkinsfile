pipeline {
    /* This 'agent' block tells Jenkins to pull a specific 
       Python image and run all the following stages inside it.
    */
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Verify Environment') {
            steps {
                // This will now work because we are inside the Python container
                sh 'python --version'
            }
        }
        
        stage('Run Script') {
            steps {
                echo 'Executing Python App...'
                sh 'python math_utils.py'
            }
        }
        
        stage('Unit Test') {
            steps {
                echo 'Running Tests...'
                sh 'python test_math.py'
            }
        }
    }
}
