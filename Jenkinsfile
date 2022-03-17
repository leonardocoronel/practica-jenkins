pipeline {
    agent {
        label('python')
    }
    stages {
        stage('Build') {
            steps {
                dir('python-application-example/python') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Unit Test') {
            steps {
                dir('python-application-example/python') {
                    sh 'python -m coverage run -m pytest -s -v'
                }
            }
        }
    }
}
