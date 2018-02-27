from setuptools import setup, find_packages


PACKAGES = find_packages('../blog')

PACKAGES.extend(['static', 'templates'])

# blog.egg-info/ is the information of packaging in python, need to be deleted if modify setup.py
setup(
    name='blog',
    version='1.0',
    description="atlednolispe's simple blog established on django2.0.",
    author='atlednolispe',
    author_email='atlednolispe@gmail.com',
    url='http://www.mayangbin.com',
    packages=PACKAGES,  # (python3 blog/setup.py sdist)'s pwd/../blog to find
    # packages=[''],  # package *.py if packages=['']
    # packages=['blog_nickname'],
    # package_dir={'blog_nickname': 'blog'},  # point out the name in packages
    # package_data={'docs': ['*.txt']},  # failed, use MANIFEST.in instead
    include_package_data=True,  # 配置MANIFEST.in文件 + packages=find_packages('../blog'),
    install_requires=[
        'coreapi==2.3.3',
        'Django==2.0.2',
        'django-autocomplete-light==3.2.10',
        'django-ckeditor==5.4.0',
        'django-crispy-forms==1.7.0',
        'django-redis==4.8.0',
        'djangorestframework==3.7.7',
        'django-reversion==2.0.13',
        'gunicorn==19.7.1',
        'hiredis==0.2.0',
        'Markdown==2.6.11',
        'Pillow==5.0.0',
        'PyMySQL==0.8.0',
        'redis==2.10.6',
        'xadmin==2.0.1',
    ],
    scripts=[
        'manage.py',  # will be added to virtualenv/bin/manage.py
    ],
)
