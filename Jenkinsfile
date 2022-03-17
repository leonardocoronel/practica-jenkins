pipeline {
    agent {
        label('python')
    }
    stages {
        stage('Build') {
            steps {
                dir('python-aplicacion-ejemplo') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Unit Test') {
            steps {
                dir('python-aplicacion-ejemplo') {
                    sh 'python -m coverage run -m pytest -s -v'
                }
            }
        }
    }
}
