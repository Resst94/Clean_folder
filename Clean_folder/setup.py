from setuptools import setup, find_namespace_packages

setup(
    name='my_clean_folder',
    version='0.1.8',
    description='This package is used to sort and clean required folders',
    url='https://github.com/Resst94/Clean_folder.git',
    author='Maksym Melnyk',
    author_email='maks.melnyk.94@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']},
    zip_safe=False
)
