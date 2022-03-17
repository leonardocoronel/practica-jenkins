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
        stage('Coverage') {
            steps {
                dir('python-application-example/python') {
                    sh 'python -m coverage report -m --fail-under=90'
                }
            }
        }
         stage('integration_test') {
            steps {
                {
                    docker run --rm leonardo7coronel/python-app-leonardo-devops:v1
                }
            }
        }
    }
}
