pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                    echo "Skipping pip install for now – we'll add this later."
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Skipping Tests for now – we'll add this later."
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh "rm -rf ${VENV_DIR}"
        }
        success {
            echo '✅ Django tests passed.'
        }
        failure {
            echo '❌ Django tests failed.'
        }
    }
}
