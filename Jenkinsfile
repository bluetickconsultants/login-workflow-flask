pipeline {
    agent any

    environment {
        // Set your AWS credentials here
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')

        // EC2 server details
        EC2_INSTANCE_IP = 'YOUR_EC2_INSTANCE_IP'
        EC2_INSTANCE_USERNAME = 'ec2-user'
        APP_DIRECTORY = '/home/ubuntu'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your Flask app repository from version control (e.g., Git)
                // Modify this step according to your VCS system (e.g., Git, SVN)
                git branch: 'main', credentialsId: 'YOUR_GIT_CREDENTIALS_ID', url: 'https://github.com/bluetickconsultants/login-workflow-flask.git'
            }
        }

        stage('Build') {
            steps {
                // This stage can be used to install any dependencies or perform any pre-deployment tasks
                sh 'make install'
            }
        }

        stage('Deploy') {
            steps {
                // Upload your Flask app to the EC2 instance
                sh "scp -i ~/.ssh/your-ec2-key.pem -o StrictHostKeyChecking=no -r * $EC2_INSTANCE_USERNAME@$EC2_INSTANCE_IP:$APP_DIRECTORY"
            }
        }

        stage('Start Uvicorn') {
            steps {
                // SSH into the EC2 instance and start Uvicorn
                sh "ssh -i ~/.ssh/your-ec2-key.pem -o StrictHostKeyChecking=no $EC2_INSTANCE_USERNAME@$EC2_INSTANCE_IP 'cd $APP_DIRECTORY && make deploy &'"
            }
        }
    }

    post {
        always {
            // Clean up or perform any post-deployment tasks here
        }
    }
}
