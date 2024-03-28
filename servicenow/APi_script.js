#!/usr/bin/env node
var axios = require('axios');


        var username = 'admin';
        var password = 'Barbibi2003!';


            axios.get('https://dev211781.service-now.com/api/now/table/incident?sysparm_limit=10', {
    auth: {
        username: username,
        password: password
    }
})
.then(function(response) {
    console.log(response.data);
})
.catch(function(error) {
    console.error('Error fetching incidents:', error);
});