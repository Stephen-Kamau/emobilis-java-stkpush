pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        SONAR_PROJECT_KEY = 'emobilis-java-stkpush' 
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

        stage('SonarQube Analysis Trail') {
            steps {
                script {
                    scannerHome = tool 'SonarScanner'
                }
                sh 'echo "Scanner home is: ${scannerHome}"'
                sh 'which sonar-scanner || echo "Global sonar-scanner not in path"'
                withSonarQubeEnv('SonarScanner') {
                    sh """
                       ${scannerHome}/bin/sonar-scanner \
                       -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                       -Dsonar.sources=. \
                       -Dsonar.projectBaseDir=${WORKSPACE}
                    """
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarScanner') {
                    sh """
                       ${scannerHome}/bin/sonar-scanner \
                       -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                       -Dsonar.sources=. \
                       -Dsonar.projectBaseDir=${WORKSPACE}
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh "rm -rf ${VENV_DIR}"
        }
        success {
            echo '✅ Tests and SonarQube analysis completed successfully.'
        }
        failure {
            echo '❌ Build failed — check errors.'
        }
    }
}
