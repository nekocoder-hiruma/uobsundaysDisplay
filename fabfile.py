from fabric.api import *


def create_databases():
    local('psql -c "CREATE DATABASE uobsundays;"')
    local('psql -c "CREATE USER uobsundays WITH PASSWORD \'ldsjl_039\'"')
    local('psql -c "GRANT ALL PRIVILEGES ON DATABASE uobsundays TO uobsundays;"')


def build():
    with lcd('src/uobsundays/'):
        local('git fetch')
        local('git checkout upgrade-dev')
        local('git pull')
        local('ls')
        local('python ./manage.py migrate --noinput --settings=conf.settings.local')
        with lcd('static/'):
            local('npm install')
            local('bower install')
            local('gulp')
