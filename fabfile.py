import os

from fabric.api import run, env, roles, prefix, cd
from fabric.contrib.files import exists

from atlednolispe_fabric import HOST1, PYPI_SIMPLE_PATH, TRUSTED_HOST


env.roledefs = {
    'develop': [
        HOST1,
    ]
}


@roles('develop')
def host_type():
    run('uname -s')


def deploy(version):
    ENV_PATH = '~/.virtualenvs/django20/'
    ACTIVE_FILE_PATH = os.path.join(ENV_PATH, 'bin/activate')
    SUPERVISOR = os.path.join('~/.virtualenvs/supervisor/', 'bin/activate')

    if exists(ACTIVE_FILE_PATH):
        with prefix('source %s' % ACTIVE_FILE_PATH):
            pypi_simple_path = PYPI_SIMPLE_PATH
            run(
                'pip install -i {pypi_simple_path} blog=={version} --trusted-host {trusted_host}'.format(
                    pypi_simple_path=PYPI_SIMPLE_PATH,
                    version=version,
                    trusted_host=TRUSTED_HOST,
                )
            )
            run('cp ~/atlednolispe_settings.py ~/.virtualenvs/django20/lib/python3.6/site-packages/')
            run('manage.py collectstatic')
            with prefix('source %s' % SUPERVISOR):
                with cd('~/supervisor'):
                    run('supervisord -c supervisord_blog.conf')
