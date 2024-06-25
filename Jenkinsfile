pipeline {
    agent any
    stages {
        stage('create score.txt') {
            steps {
                bat '( echo Currency Roulette = 60 & echo.Guess Game = 60 & echo.Memory Game = 60 ) > Score.txt'
            }
        }
        stage('Build docker image') {
            steps {
                bat 'docker-compose build'
            }
        }

         stage('run docker image and tests') {
             steps {
                bat 'docker compose up --abort-on-container-exit --exit-code-from selenium-tests'
             }
        }
         stage('push to docker hub') {
            steps {
                script {
                    bat 'docker-compose push wog-app'
                }
            }
        }
    }
}

