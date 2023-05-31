from setuptools import setup

setup(
    name='text-generation-app',
    version='1.0',
    description='Text Generation Streamlit App',
    author='yash',
    author_email='sharyash1101@gmail.com',
    packages=[''],
    install_requires=[
        'streamlit==0.87.0',
        'transformers==4.11.3',
    ],
)
