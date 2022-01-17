pipeline {
    agent any 
    stages {
        stage('Checkout') { 
            steps {
                'git checkout master'
            }
        }
        stage('Build') { 
            steps {
                'docker build -t flask-app .'
            }
        }
        stage('Run') { 
            steps {
                'docker run -p 8777:8777 -d flask-app' 
            }
        }
        stage('Test') { 
            steps {
                'python e2e.py' 
            }
        }
        stage('Finalize') { 
            steps {
                'docker-compose down'
                'docker push danielmalka/devops_experts:flask-app'
            }
        }
    }
}
