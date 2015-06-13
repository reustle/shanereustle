---
title: Free Up The Event Loop With Web Workers
---

JavaScript gives us an event loop so we can set timeouts and listeners without blocking all script execution. The problem with this approach shows when you start writing CPU intensive code. The event loop can only execute one task at a time, so if one of those operations takes 5 seconds, nothing else can run until it has finished. On top of the JavaScript engine being locked during this time, the browser will not render any UI changes. This results in the entire browser freezing. As we move to heavier client side applications, this limitation becomes more obvious.

Web Workers are one of the new features in the HTML5 spec and allow us to essentially create multiple event loops. By running expensive operations in their own threads, the user experience stays responsive. Below is an example of an expensive operation implemented with and without a worker.

<select id='nth_prime' class='form-control' style='width: 150px; display: inline-block;'>
	<option value='2000'>2,000th Prime</option>
	<option value='4000'>4,000th Prime</option>
	<option value='6000'>6,000th Prime</option>
	<option value='8000'>8,000th Prime</option>
</select>
<input type='button' value='Find Prime' onclick='find_prime()' class='btn btn-default'/>
<input type='button' value='Find Prime with Web Worker' onclick='find_prime_worker()' class='btn btn-default'/><br/>
<div id='result' class='alert alert-info'><em>Select an option above</em></div>

A worker is initiated by passing a JavaScript file which includes a specific event listener. No global variables from the parent are available in the worker, which includes the document and window objects. The only way to pass data in is to fire a message event to the worker with a string attached. More recently, browsers have been starting to support sending an object which will be json stringified automatically. To be safe, you should always stringify the object yourself before sending to prevent any cross browser issues.

Take a look at the source code of this article for a simple working example. You can [read more about web workesr here](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers). If you have any questions, feel free to ask me.

<script>
	
	var start_time;
	
	var find_prime = function(){
		// Find Nth prime
		
		start_time = new Date();
		document.getElementById('result').innerHTML = 'Running...';
		var nth_prime = parseInt(document.getElementById('nth_prime').value, 10);
		
		var is_prime = function(num){
			// This function is intentionally slow
			
			var counter = num - 1;
			while(counter > 1){
				if(num % counter == 0){
					return false;
				}
				counter--;
			}
			return true;
		};
		
		var current_num = 3;
		var primes = [];
		
		while(primes.length != nth_prime){
			if(is_prime(current_num)){
				primes.push(current_num);
			}
			current_num++;
		}
		
		var duration = parseFloat((new Date()) - start_time) / 1000;
		document.getElementById('result').innerHTML = 'Took ' + duration + ' seconds';
		
	};
	
	// Initiate the worker. It will now wait for messages
	var worker = new Worker('/static/resources/find-prime.js');
	
	var find_prime_worker = function(){
		// Find Nth prime using a web worker
		
		start_time = new Date();
		document.getElementById('result').innerHTML = 'Running...';
		var nth_prime = parseInt(document.getElementById('nth_prime').value, 10);
		
		// Send the worker a message
		worker.postMessage(nth_prime);
		
	};
	
	worker.onmessage = function(event){
		// Once the worker returns the result, update the UI
		
		var duration = parseFloat((new Date()) - start_time) / 1000;
		document.getElementById('result').innerHTML = 'Took ' + duration + ' seconds';
		
	};

</script>

