pipeline {
    agent any
    environment {
        DOCKER_COMPOSE_VERSION = '3' 
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/adithyan-lp/dapp.git', credentialsId: 'dapp_id']]])
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh "docker-compose build"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh "docker-compose up -d"
                }
            }
        }
    }
    post {
        success {
            echo "Deployment successful. Add further steps if needed."
        }
        failure {
            echo "Deployment failed. Take necessary actions for failure handling."
        }
    }
}
