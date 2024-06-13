pipeline {

    agent any

    tools {
        jdk 'JDK 17'
    }

    environment {
        GITHUB_TOKEN = credentials("GITHUB_TOKEN_KB")
    }

    stages {
         
        stage("pre-build") {
            steps {
                echo 'Starting the build Stage '
                sh 'printenv'
            }
        }

          
        stage("build") {
            steps {
                echo 'Starting the build Stage'
            }
        }

                 
        stage("post-build") {
            steps {
                echo 'Starting the build Stage'
            }
        }

    }

}

