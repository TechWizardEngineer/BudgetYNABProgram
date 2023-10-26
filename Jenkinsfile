// pipeline must be top-level
pipeline {

  //where to execture. This is equals to node {groovy}
  agent any

  //Where the work happens
  stages {

    stage("Build"){
        steps {
          echo "Building app"
        }
    }

    stage("Test"){
        steps {
          echo "Testing app"
        }
    }

    stage("Deploy"){
        steps {
          echo "Deploying app"

        }
    }

  }

}
