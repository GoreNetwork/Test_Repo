pipeline {
    agent any
    stages {
        stage('Example Username/Password') {
            environment {
                SERVICE_CREDS = credentials('Ansible_Account')
            }
            steps {
                sh 'echo bob'
            }
        }
    }
}