# from Cython.Build import cythonize
from setuptools import setup


setup(name='Azimuth',
      version='2.0',
      author='Nicolo Fusi and Jennifer Listgarten',
      author_email="fusi@microsoft.com, jennl@microsoft.com",
      description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 guide efficiency"),
      packages=["azimuth", "azimuth.features", "azimuth.models", "azimuth.tests"],
      package_data={'azimuth': ['saved_models/*.*', 'saved_models/*.*']},
      install_requires=['scipy', 'numpy', 'matplotlib', 'nose', 'scikit-learn>=0.18', 'pandas', 'biopython'],
      license="BSD",
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      # ext_modules=cythonize("ssk_cython.pyx"),
)
