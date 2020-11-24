# Bidirectional Telemetry

Bi-directional telemetry allows you to send messages from your Ground Station Software to the Flight Controller connected to the Air SBC.

### Enabling bidirectional telemetry

By default bidirectional telemetry is disabled, to enable it simple set the following options in the config file or enable them in the QOpen.HD settings.

```text
TELEMETRY_UPLINK=mavlink
TELEMETRY_TRANSMISSION=wbc
RC=mavlink
```

In order for this to work please make sure you have [connected ](../hardware/wiring.md#flight-controller)your Flight Controller properly.

