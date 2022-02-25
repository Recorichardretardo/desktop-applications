var express = require('express');
const screenshot = require('screenshot-desktop')
const fs = require('fs')


var app = express();


app.get('/listUsers', function (req, res) {

    screenshot().then((img) => {
        fs.writeFile('out1.jpg', img, function (err) {
          if (err) {
            throw err
          }
          console.log('written to out.jpg')
        })
      }).catch((err) => {
        throw err
      })


      res.send( {"test":"test"} );
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})









// screenshot({format: 'png'}).then((img) => {


//     console.log("img",img)
//   // img: Buffer filled with png goodness
//   // ...
// }).catch((err) => {
//   // ...
// })