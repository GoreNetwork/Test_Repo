pipeline {
    agent any
    // dir('/home/dhimes/Test_Repo/Playbooks')
    stages {
        stage('Example Username/Password') {
            environment {
                SERVICE_CREDS = credentials('ANSIBLE')
                USER = "$SERVICE_CREDS_USR"
                PASSWORD = "$SERVICE_CREDS_PSW"
            }
            steps {
                sh 'ansible-playbook -i hosts Playbooks/build_switches.yml'
            }
        }
    }
}