pipeline {
    agent any

    environment {
        SELENIUM_URL = 'http://localhost:4444/wd/hub'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'docker-compose up --build -d'
                    sh 'docker-compose exec test-runner pytest tests/'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            sh 'docker-compose down'
        }
    }
}
