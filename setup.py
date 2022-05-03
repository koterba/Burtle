from distutils.core import setup
setup(
  name = 'burtle',         # How you named your package folder (MyLib)
  packages = ['burtle'],   # Chose the same as "name"
  version = '1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A game focued version of the turtle module',   # Give a short description about your library
  author = 'Alan Koterba',                   # Type in your name
  author_email = 'alankoterba12321@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/alannxq/Burtle',   # Provide either the link to your github or to your website
  keywords = ['turtle', 'burtle', 'game'],   # Keywords that define your package best
  install_requires=["pillow", "pygame", "keyboard"],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
  package_data={'': ['default_images/*.gif']}
)
