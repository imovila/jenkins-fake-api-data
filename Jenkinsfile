pipeline {
  agent any
  stages {
	  stage('Build') {
		  steps {
			  script {
				  sh 'python get-fake-data.py'
			  }
		  }
	  }
  }
}
