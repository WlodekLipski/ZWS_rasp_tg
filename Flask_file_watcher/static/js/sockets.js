var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
	socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('modified', function(data) {                                  
	console.log('File was modified');
});
