"""
======= Create a local cache for an experiment ========
"""
doclines = __doc__.split("\n")


if __name__ == '__main__':
    from distutils.core import setup
    setup(name = "trackline",
          version = '0.1',
          description = doclines[0],
          long_description = "\n".join(doclines[2:]),
          author = "Matthew Harrison",
          author_email = "matthew.harrison@noaa.gov",
          url = "none",
          license = 'CCL',
          platforms = ["any"],
          packages=['trackline'],
          )
    
