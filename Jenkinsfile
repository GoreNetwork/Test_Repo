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
                dir('Playbooks'){
                    sh 'ansible-playbook build_switches.yml'
                }
                // sh 'ansible-playbook Playbooks/build_switches.yml'
            }
        }
        stage('Copy over configs to batfish test') {
            steps {
                    sh 'cp ./Playbooks/output/ ./batfish_tests/snapshots/lab/'
                }
            }
        
        stage('Run Tests') {
            steps {
                dir('batfish_tests'){
                    sh 'python brand_new_work.py'
                        
                }
            }
        }
    }
}
