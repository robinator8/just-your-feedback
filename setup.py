from setuptools import setup

requires = [
    'pyramid==1.9.2',
    'pyramid_jinja2==2.7',
    'requests==2.20.0',
    'waitress==1.4.2',
    'tensorflow',
    'opencv-python',
    'keras',
    'imageai'

]

setup(
    name='webapp',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = webapp:main
    """
)

