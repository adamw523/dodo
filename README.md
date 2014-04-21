# dodo - DigitalOcean Library and Command Line tools

[![dodo](http://adamw523.s3.amazonaws.com/dodo/dodo.png)](http://commons.wikimedia.org/wiki/File:Dodo_head_\(1848\).jpg)

## Installation
```
pip install dodo
```

or

```
easy_install dodo
```

## Configuration File

Located at `~/.dodo`

```
[credentials]
client={client_key}
api={api_key}
```

## Command line tool

List your droplets

```
$ dodo droplets
id        name                                     image region size status     backups
----------------------------------------------------------------------------------------
97664     adamtest                                 2530  1      66   active     True   
98447     testingnew                               2548  1      66   active     None  
```

Boot new droplet

```
dodo droplets --new --name=testingnew --size_id=66 --image_id=25485 --region_id=1
event_id        :  698622
image_id        :  25485
size_id         :  66
id              :  98444
name            :  testingnew
```

Get droplet IP address

```
$ dodo droplets --show --droplet_id=98444
status          :  active
region_id       :  1
size_id         :  66
image_id        :  25485
backups_active  :  None
ip_address      :  192.34.61.80
id              :  98444
name            :  testingnew
```

Take a snapshot of a droplet

```
$ dodo droplets --snapshot --droplet_id=98447 --name='Testing Snapshots'
status          :  OK
event_id        :  698651
```

Get more help

```
$ dodo --help
NAME
    dodo - A DigitalOcean command line interface

SYNOPSIS
    dodo resource [--destroy] [--disable_backups] [--droplet_id] [--enable_backups]
                  [--filter] [--help] [--image_id] [--name]
                  [--new] [--power_cycle] [--power_off] [--power_on]
                  [--reboot] [--rebuild] [--region_id] [--reset_root_password]
                  [--resize] [--restore] [--show] [--shutdown]
                  [--size_id] [--snapshot] [--ssh_key_id] [--ssh_key_ids]
                  [--ssh_key_pub]
OPTIONS
    resource
        droplets, images, regions, sizes, ssh_keys

    --filter
        my_images, global

FILES
    ~/.dodo
        Credentials configuration file:

        Example:

        [crednetials]
        client=<client_key>
        api=<api_key>
```


## Example Cration of new Droplet
![Creating a new Droplet](http://adamw523.s3.amazonaws.com/dodo/dodo_v1.gif)

## Development

### Setting Up Envirnment

```
$ git clone git@github.com:adamw523/dodo.git
$ cd dodo
$ virtualenv ~/dodove
$ . ~/dodove/bin/activate
```

Set up local symlinks for development
```
python setup.py develop
```

###

Building And Uploading to PyPi

```
$ python setup.py sdist upload
```

If not registered on local machine yet:

```
$ python setup.py sdist register upload
```

## License

MIT
