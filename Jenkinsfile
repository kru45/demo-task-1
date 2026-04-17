pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Testing the code...'
                // If this fails, Jenkins stops immediately
                sh 'python3 test_math.py'
            }
        }
        stage('Execute Main') {
            steps {
                echo 'Test passed! Now running the main script...'
                sh 'python3 math_utils.py'
            }
        }
    }
}
