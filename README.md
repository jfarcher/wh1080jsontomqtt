Takes data from a file in JSON format, this data is generated by https://github.com/jfarcher/rtl_wh1080.
It will then publish this data to MQTT, publishing the full string then each element of the array individually.

TODO, make the script itterate through the array and generate the publish string on the fly rather than have individual entries for each element.

Usage:
Edit the variable to reflect your MQTT server (if you use authentication you'll need to add it in.
