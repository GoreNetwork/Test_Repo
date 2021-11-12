pipeline {
    agent any
    environment {
        PATH = "/home/dhimes/.local/bin/ansible:/usr/bin/ansible:/usr/bin/ansible-playbook:$PATH"
            }
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
                    sh "whoami"
                    sh "echo $PATH"
                    echo "PATH is: $ANS_HOME"
                    sh 'ansible-playbook build_switches.yml'
                    // sh 'who'
                }
                // sh 'ansible-playbook Playbooks/build_switches.yml'
            }
        }
        stage('Copy over configs to batfish test') {
            steps {
                    sh 'mkdir -p ./batfish_tests/snapshots/lab/configs'
                    sh 'cp -a ./Playbooks/final_output/. ./batfish_tests/snapshots/lab/configs'
                }
            }
        
        stage('Run Tests') {
            steps {
                dir('batfish_tests'){
                    sh 'pip3 install pandas'
                    sh 'pip3 install pybatfish'
                    sh 'python3 brand_new_work.py'
                        
                }
            }
        }
    }
}
