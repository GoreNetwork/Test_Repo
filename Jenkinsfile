pipeline {
    agent any
    dir('$workspace/Playbooks')
    stages {
        stage('Build Configs') {
            // environment {
                // SERVICE_CREDS = credentials('ANSIBLE')
                // USER = "$SERVICE_CREDS_USR"
                // PASSWORD = "$SERVICE_CREDS_PSW"
            // }
            steps {
                sh 'ansible-playbook -i Playbooks/hosts Playbooks/build_switches.yml'
                sh "ll Playbooks/Output/R1/"
            }
        }
    }
}