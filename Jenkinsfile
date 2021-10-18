pipeline {
    agent any
    // dir('$workspace/Playbooks')
    // dir('/home/dhimes/Test_Repo/Playbooks')
    stages {
        stage('Build Configs') {
            // environment {
                // SERVICE_CREDS = credentials('ANSIBLE')
                // USER = "$SERVICE_CREDS_USR"
                // PASSWORD = "$SERVICE_CREDS_PSW"
            // }
            steps {
                // dir('$workspace/Playbooks'){}
                sh "pwd"
                sh "ll"
                // sh "echo $workspace/Playbooks"
                sh 'ansible-playbook -i hosts build_switches.yml'
            }
        }
    }
}