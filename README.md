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

Logs would indicate a successful download (Downloaded /tmp/app/vendor/forward) if all goes well.
AppD tile names the download after the url endpoint (forward in this case) and places it under vendor directory 

```
 Downloaded app package (39.5M)
   -----> Appdynamics Buildpack version 5.0.145
   [APPD_BP]       Setting up AppDynamics
   [APPD_BP]       Setting up AppDynamics DotNetCore Agent
   [APPD_BP_LIB]       Checking for Bound AppDynamics service instances
   [APPD_BP_LIB]       Using access key from secret field
   [APPD_BP_LIB]       Creating /tmp/app/.appdynamics directory

   [APPD_BP_LIB]       Creating /tmp/app/vendor directory

   [APPD_BP]       Downloaded /tmp/app/vendor/forward from APPD_AGENT_HTTP_URL
   [APPD_BP]       Unzipping /tmp/app/vendor/forward
   [APPD_BP_LIB]       Downloading [AppDynamicsAgentLog.config AppDynamicsConfig.json] to /tmp/app/.appdynamics

   [APPD_BP]       Writing AppDynamics Core CLR profiler environment
   -----> Dotnet-Core Buildpack version 2.3.2
   -----> Supplying Dotnet Core
   -----> Installing libunwind 1.3.1
   ```
