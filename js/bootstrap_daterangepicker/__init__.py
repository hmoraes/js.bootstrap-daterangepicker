from fanstatic import Library, Resource, Group
from js.bootstrap import bootstrap
from js.jquery import jquery
from js.momentjs import moment

library = Library('bootstrap_daterangepicker', 'resources')

daterangepicker_css = Resource(library, 'daterangepicker.css',
                               minified='daterangepicker.min.css',
                               minifier='cssmin',
                               depends=[])

daterangepicker_js = Resource(library, 'daterangepicker.js',
                              minified='daterangepicker.min.js',
                              minifier='jsmin',
                              bottom=True,
                              depends=[bootstrap, jquery, moment, ])

daterangepicker = Group([daterangepicker_css, daterangepicker_js, ])
