pipeline {
    agent any

    stages {
        stage('Check Files') {
            steps {
                echo 'Checking what Jenkins downloaded...'
                // This lists the files so we can see if math_utils.py exists
                sh 'ls -la'
            }
        }
        
        stage('Execute Python') {
            steps {
                echo 'Running the math script...'
                // Make sure the filename here matches exactly what is in your GitHub repo
                sh 'python3 math_utils.py'
            }
        }
    }
}
