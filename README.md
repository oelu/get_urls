# Get URLS out of web pages

## Requirements
* Requires python docopt module

## Usage: 

    get_urls.py
        shows embedded links in websites
    Usage:
        get_urls.py (-u <url> | --url <url>)

## Example Session

    $ ./get_urls.py
        Usage:
        get_urls.py (-u <url> | --url <url>)
    
    
    ./get_urls.py --url www.google.ch
    connecting to: www.google.ch
    [u'http://schema.org/WebPage',
    u'http://www.google.ch/imghp?hl=de&tab=wi',
    u'http://maps.google.ch/maps?hl=de&tab=wl',
    u'https://play.google.com/?hl=de&tab=w8',
    u'http://www.youtube.com/?gl=CH&tab=w1',
    u'http://news.google.ch/nwshp?hl=de&tab=wn',
    u'https://mail.google.com/mail/?tab=wm',
    u'https://drive.google.com/?tab=wo',
    u'http://www.google.ch/intl/de/options/',
    u'http://www.google.ch/history/optout?hl=de',
    u'https://accounts.google.com/ServiceLogin?hl=de&continue=http://www.google.ch/',
    u'http://www.google.ch/setprefs?sig=0_4RHihQOz6O6KRxAMlFVBVOMaeMc%3D&amp;hl=en&amp;source=homepage',
    u'http://www.google.ch/setprefs?sig=0_4RHihQOz6O6KRxAMlFVBVOMaeMc%3D&amp;hl=fr&amp;source=homepage',
    u'http://www.google.ch/setprefs?sig=0_4RHihQOz6O6KRxAMlFVBVOMaeMc%3D&amp;hl=it&amp;source=homepage',
    u'http://www.google.ch/setprefs?sig=0_4RHihQOz6O6KRxAMlFVBVOMaeMc%3D&amp;hl=rm&amp;source=homepage',
    u'http://www.google.ch/intl/de/services/',
    u'https://plus.google.com/105772902399567012021',
    u'http://www.google.ch/setprefdomain?prefdom=US&amp;sig=0_DSiTJ9D38528TCnx3gL8VUozFYk%3D']
