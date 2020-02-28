We need a configuration server that hosts our agent zip files. In addition we need a python flask app that acts as an intermediary proxy to fetch the agent from internal backend. Finally, we push Dotnet app (cf-net-linux) that uses 
a generic APPD_AGENT_HTTP_URL pointing to our proxy (flask app)

1. Push cf-configuration server using Static Buildpack
	```
	$ cd cf-configuration-server
	$ cf push appd-configuration-server
	```	

2. Push Python flask app that hosts the forward endpoint

       
       $ cd cf-python
       $ cf push cf-python
       

3. Push Dotnet app 

       
       $ cd cf-net-linux
       $ cf push test-generic-endpoint
       

Note that flask app request timeouts may need to be modified depending on how long it takes to download from the internal endpoints
