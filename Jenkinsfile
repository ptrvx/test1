pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ptrvx/test1'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    echo "Running tests..."
                '''
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    docker image build --tag test1:latest .
                '''
            }
        }
        
        stage('Stop') {
            steps {
                sh '''
                    docker container stop getdeckapi
                    docker container rm getdeckapi
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    docker run -d --name getdeckapi -p 9090:5000 test1:latest
                '''
            }
        }
        
    }
}
