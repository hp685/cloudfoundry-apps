1. Push cf-configuration server using Static Buildpack
	```
	$ cd cf-configuration-server
        $ cf push appd-configuration-server
	```

2. Push Python flask app that hosts the forward endpoint
       ```
       $ cd cf-python
       $ cf push cf-python
       ```

3. Push Dotnet app 
       ```
       $ cd cf-net-linux
       $ cf push cf test-generic-endpoint
       ```

Note that flask app request timeouts may need to be modified depending on how long it takes to download from the internal endpoints
