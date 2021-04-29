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
                    docker image build --tag test1:2.0 .
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
                    docker container run --name getdeckapi test1:2.0
                '''
            }
        }
        
    }
}
