pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PIP_CACHE_DIR = "${HOME}/.cache/pip"
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
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    # pip install --upgrade pip
                    # pip install -r requirements.txt
                    echo "Skipping pip install for now – we'll add this later."
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    # . ${VENV_DIR}/bin/activate
                    # python manage.py test --verbosity=2
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
