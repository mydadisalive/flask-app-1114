pipeline {
    agent any

    stages {
        stage('Cleanup') {
            steps {
                cleanWs() // Jenkins workspace cleanup step
            }
        }        stage('Clone Code') {
            steps {
                sh 'git clone https://github.com/mydadisalive/flask-app-1114.git'
                sh 'ls'
            }
        }
        stage('Build') {
            steps {
                sh 'cd flask-app-1114'
                sh 'docker build -t mydadisalive/cat-gifs:1.0 .'
            }
        }
        stage('Test') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
