pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                // This confirms Python is now visible to Jenkins
                sh 'python3 --version'
            }
        }

        stage('Run Python Task') {
            steps {
                // Create the script on the fly if it's not in your workspace
                sh '''
                echo "print('Hello from Python inside Jenkins!')" > task.py
                python3 task.py
                '''
            }
        }
    }
}
