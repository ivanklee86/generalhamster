def quietsh(cmd) {
    sh('#!/bin/sh -e\n' + cmd)
}

pipeline {
    agent {
        docker {
            image 'python:3.7.0'
            label 'dev-test'
            args '-u root'
        }
    }
    environment {
        LC_ALL = 'en_US.UTF-8'
        LANG = 'en_US.UTF-8'
        PYTHONPATH = $WORKSPACE
        AAPTIVSECRETS_ENV = prod
    }
    stages {
        stage("Content Service Alert") {
            steps{
                sh 'python ./app/run.py'
        }
    }
}