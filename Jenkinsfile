pipeline {
    agent { label 'agent_1' }
    stages {
        stage('Checkout') { 
            steps {
                sh 'git config --global user.name danielmalka14'
                sh 'git init'
                sh 'git checkout -b my-main-branch'
            }
        }
        stage('Build') { 
            steps {
                sh 'docker rm -f flask-api'
                sh 'docker rmi -f flask-app'
                sh 'docker build -t flask-app /var/jenkins_home/worker/app'
                sh 'docker run -d --network jenkins_bridge -h my-flask-app --name flask-api flask-app'
            }
        }
        stage('Run') { 
            steps {
                sh 'sleep 5'
                sh 'curl 172.18.0.4:80'
            }
        }
        stage('Test') { 
            steps {
                sh 'python /var/jenkins_home/worker/app/tests/e2e.py' 
            }
        }
        stage('Finalize') { 
            steps {
                sh 'docker rm -f flask-api'
                sh 'docker login -u danielmalka -p SS1412DDM!'
                sh 'docker tag flask-app danielmalka/flask-app:latest'
                sh 'docker push danielmalka/flask-app:latest'
                sh 'docker rmi -f danielmalka/flask-app:latest'
            }
        }
    }
}
