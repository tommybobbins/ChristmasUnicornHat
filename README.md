ChristmasUnicornHat
===================

Animated sequence of text and Christmas tree for Pimoroni's Unicorn Hat: http://shop.pimoroni.com/products/unicorn-hat

Install the usual unicorn hat drivers from : https://github.com/pimoroni/UnicornHat

Add the following to the /etc/rc.local

    /usr/bin/python /home/pi/UnicornHat/python/examples/christmas.py &

Just before the 

    exit 0

To convert the Unicorn paint code to Python, this one liner is useful:

    grep "GET /pixel" unicorn_paint.log | awk '{print $7}' | sort | sed -e 's/\/pixel\//    unicorn\.set\_pixel\(/g' | sed -e 's/$/)/g' | sed -e 's/\//\,/g'
