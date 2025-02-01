from setuptools import setup, find_packages

# اطلاعات پروژه
setup(
    name='installer-tool',
    version='1.0.0',
    author='Alirezashamsadinloo',
    author_email='alirezashamsadinloo@example.com',
    description='A tool to create installer batch files for .exe files, automate installation, and manage system-level installations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alirezashamsadinloo/installer-tool',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'tqdm',             # For progress bar
        'colorama',         # For colored output in the console
        'tkinter',          # For GUI file dialogs
    ],
    entry_points={
        'console_scripts': [
            'installer-tool=installer:main',  # Replace with the main entry function of your installer script
        ],
    },
    python_requires='>=3.7',
    include_package_data=True,
    data_files=[
        ('/etc/installer-tool', ['config/config.json']),  # Adjust paths if necessary
    ],
)
