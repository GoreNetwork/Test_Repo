pipeline {
    agent any
    stages {
        stage('Example Username/Password') {
            environment {
                SERVICE_CREDS = credentials('ANSIBLE')
            }
            steps {
                sh 'echo bob'
            }
        }
    }
}