from setuptools import setup

setup(
    name='undermath',
    version='1.0.3',
    description='Este paquete contiene módulos para realizar cálculos aritméticos y estadísticos sencillos.',
    author='Underdoge',
    author_email='eduardo.chapa@gmail.com',
    url='https://github.com/Underdoge/undermath',
    install_requires=[
        'argparse',
        'importlib-metadata; python_version == "3.10"',
    ],
)
