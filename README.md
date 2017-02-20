# emoncms-epsolar_tracer-uploader
Little script to upload readings from EPSolar MPPT Solar Charge Controller RN series. It was tested on 4215RN. Signal from charge controller processed by Raspberry Pi B+.

File `tracer.service` to be used by systemd on Raspbian to launch the tracer script after launch when internet connectivity becomes available.

The tracer module comes from here: https://github.com/xxv/tracer/tree/master/python
