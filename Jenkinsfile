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
                    Running tests...
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
        
        stage('Deploy') {
            steps {
                sh '''
                    docker container run --name getdeckapi test1:2.0
                '''
            }
        }
        
    }
}
