pipeline {
  agent any  // runs on any available Jenkins nodes

  environment {
    LABS_CREDS = credentials('labcreds')  // securely injects username/password
    JAVA_HOME  = '/opt/bitnami/java'
    PATH       = "${env.JAVA_HOME}/bin:${env.PATH}"
  }

  stages {
    stage('Setup Python') {
      steps {
        echo "Setting up Python environment..."
        sh 'python3 -m venv venv'
        sh 'venv/bin/pip install --upgrade pip pipenv'
      }
    }

    stage('Install Dependencies') {
      steps {
        echo "Installing dependencies..."
        sh 'venv/bin/pipenv install --deploy'
      }
    }

    stage('Test') {
      steps {
        echo "Running tests..."
        sh 'venv/bin/pipenv run pytest --maxfail=1 --disable-warnings'
      }
    }

    stage('Package') {
      steps {
        echo "Packaging project..."
        sh 'zip -r project.zip . -x "venv/*"'
      }
    }

    stage('Deploy') {
      steps {
        echo "Deploying to remote server..."
        sh '''
          sshpass -p $LABS_CREDS_PSW \
            scp -o StrictHostKeyChecking=no \
            project.zip $LABS_CREDS_USR@remote.server:/deploy/path
        '''
      }
    }
  }

  post {
    always {
      node {  // Added node block for context
        echo "Archiving artifacts and processing test results..."
        archiveArtifacts artifacts: 'project.zip', fingerprint: true, allowEmptyArchive: true
        junit 'reports/**/*.xml'
      }
    }
    success { 
      echo 'Build succeeded!'
    }
    failure { 
      node {  // Added node block for context
        echo "Sending failure notification..."
        mail to: 'dev-team@example.com', 
             subject: "Failed: ${env.JOB_NAME}", 
             body: 'Check logs.'
      }
    }
  }
}