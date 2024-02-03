# QGroundControl

To establish a connection between OpenHD and QGroundControl over Wi-Fi or Ethernet, follow these steps:

1. Navigate to the "Comm Links" tab within QGroundControl and click on "Add" located in the lower part of the screen.
![QGC-Connection-Page](.gitbook/assets/QGC1.png)


2. Fill in the following parameters:
   - **Name:** Enter a name for the connection, e.g., "TCP OpenHD".
   - **Automatically Connect on Start:** Check this option.
   - **Type:** Select "TCP".
   - **Server Address:** Input "192.168.3.1".
   - **Port:** Set the port to "5760".
   - Click "OK" to confirm.
![QGC-Comm-Links](.gitbook/assets/QGC2.png)

3. Click on "Connect" and wait for telemetry data to be received, which typically takes around 5 seconds.
![QGC-Connect](.gitbook/assets/QGC3.png)


4. At this point, telemetry data should be available, but video may not be. Follow these steps to resolve this:
![QGC-Main-Page](.gitbook/assets/QGC4.png)


5. Select "UDP" as the source and set the port to "5600".
![QGC-General-Page](.gitbook/assets/QGC5.png)


By following these steps, telemetry data and video feed should now be accessible within QGroundControl. Enabling the "Automatically Connect on Start" option eliminates the need to reconnect during subsequent program launches.