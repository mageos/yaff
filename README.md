# yaff
Yet another firewall frontend

In reality, yaff is much more than just a firewall frontend.  Yaff is an attempt to build a consumer-grade routing solution that provides a robust set of features that are easy enough to configure that your average home-owner can manage.

## Target Features
### Named Object Groups
When setting up a firewall, there are often rules that don't apply to a single computer, but rather apply to a set of computers, networks or domains.  Yaff aims to allow people to create simple yet effective rules that are based on simple actions against named devices, targets or groups.

### IoT Switches
Since firewall rules essentially turn on or off connections, yaff should also expose IoT compatible switches that can be used to change the effect of a rule.  For example, if you had a rule named "John's Internet Access", that was by default allowed, you could have the switch, when off set the action to deny.  After registering the switch with google, you could then say "Hey google, turn off 'John's Internet Access'" and the firewall rule would be changed from allow to deny.

## Configuration File

### Data Types
* _string_: A simple string of characters

### Devices
The devices section provides a description of devices that are present on the local network.

| Property | Type | Description |
|------|------|-----|
| name | string | the DNS host name to use for the device |
| descritpion | string | A longer description of what the device is |
| aliases | string[] | A list of additional host names to be assigned to the device |
| interfaces | string[] | A list of Mac Address and optionally reserved IPv4 addresses attached to the device.  The format of the value is mac_address[@ipv4_address].  For example 12:34:56:78@192.168.1.123 would be a device with the mac address 12:34:56:78 that would always be assigned an IP address of 192.168.1.123 |

### Targets
A list of identifiers that can be used in firewall rules that are not a part of your current network



### Sample Config

```yaml
schema: yaff
version: 0.1
network:
  domain: home.local
  network: 192.168.1.1/24
  start: 192.168.1.100
  end: 192.168.1.199

devices:
  - name: piserver
    description: Raspberry Pi Server
    aliases:
      - docker
      - monitoring
      - automation
    interfaces:
      - 00:00:00@192.168.5.14
      - 00:00:01@192.168.5.15

targets:
  - name: youtube
    type: dns
    domains:
      - youtube.com
      - youtu.be
      - streaming.youtube.com
  - name: iot devices
    type: group
    members:
      - piserver

rules:
  - name: Allow All Outbound
    action: allow
    source: @all
    destination: @all
  - name: Log Iot
    action: monitor
    source: @iot devices
    destination: @all    

switches:
  - name: Kids Devices
    rules:
      - Log Iot
    action: deny
```
