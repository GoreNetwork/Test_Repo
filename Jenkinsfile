pipeline{
    agent any
    environment {
        ANSIBLE_SERVER = 192.168.174.132
        ANSIBLE_USER = credentials('Ansible_Account')
        ANSIBLE_PASSWORD = 
    }
    stages{
        stage("Username, and Password"){
            SERVICE_CREDS = credentials('Ansible_Account')
        }
        steps {
                sh 'echo "Service user is $SERVICE_CREDS_USR"'
                sh 'echo "Service password is $SERVICE_CREDS_PSW"'
                sh 'curl -u $SERVICE_CREDS https://myservice.example.com'
            }
        stage("Show Branch") { 
            steps{
                echo "$GIT_BRANCH"
            }
        }
        stage("Hello World") { 
            steps{
                echo "Hello World"
            }
        }
        stage("Build Configs") { 
            steps{
                echo "Building..."
            }
        }
    }
}