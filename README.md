# xcal

ical and jcal utilities as well as support for yaml

## Background

This work started while adding config to a tornado based web site.
yaml had been chosen for the config format and there was a requirement to add
scheduling information into the config. Rather than use a custom scheduling
definition I looked at iCalendar whilst looking at this I also came across
jcal (RFC 7265), ical represented as json. Conversion from json to yaml is
straight forawrd in python so it made sense to look at the chain::

    ical <--> icalendar <--> jcal <--> yaml

## References

* [RFC 5545](http://tools.ietf.org/html/rfc5545)
* [RFC 6321](http://tools.ietf.org/html/rfc6321)
* [RFC 5350](http://tools.ietf.org/html/rfc6350)
* [RFC 6868](http://tools.ietf.org/html/rfc6868)
* [RFC 7529](http://tools.ietf.org/html/rfc7529) (supercedes: [RFC 7265](http://tools.ietf.org/html/rfc7265))
