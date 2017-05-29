node {
    stage "Clone", {
        checkout scm
    }
    
    stage "Run tests", {
        sh "python -m unittest test.py"
    }
    
    stage "Deploy", {
        sh "echo Your preferred deploy tool here"
    }
}
