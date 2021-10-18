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
                dir('$workspace/Playbooks'){
                // sh "echo $workspace/Playbooks"
                sh 'ansible-playbook -i Playbooks/hosts Playbooks/build_switches.yml'
                sh "ll Playbooks/Output/R1/"}
            }
        }
    }
}