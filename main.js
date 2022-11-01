var https = require("https");
const settings = {
  path: "/ip/",
  host: "ipapi.co",
  port: 443,
  headers: {"User-Agents": "nodejs-ipapi-v1.02"}
};

https.get(settings, function(response) {
  var res = '';
  response.on('data', function(data) {
    res += data;
  });
  
  response.on('end', function() {
    console.log(res);
  });
});
    
  
