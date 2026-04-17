pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // If using Git, you'd use 'git url' here. 
                // For a local test, we'll just print a message.
                echo 'Pulling code from repository...'
            }
        }
        
        stage('Run Script') {
            steps {
                echo 'Executing Python App...'
                sh 'python3 math_utils.py'
            }
        }
        
        stage('Unit Test') {
            steps {
                echo 'Running Tests...'
                sh 'python3 test_math.py'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
