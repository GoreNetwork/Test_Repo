pipeline{
    agent any
    stages{
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
    }
}