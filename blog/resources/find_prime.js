self.onmessage = function(event){
	
	// Read the request
	var nth_prime = parseInt(event.data, 10);
	
	var is_prime = function(num){
		// The purpose of this function is to be slow.
		
		var counter = num - 1;
		while(counter > 1){
			if(num % counter == 0){
				return false;
			}
			counter--;
		}
		return true;
	};
	
	var find_prime = function(nth_prime){
		
		var current_num = 3;
		var primes = [];
		while(primes.length != nth_prime){
			if(is_prime(current_num)){
				primes.push(current_num);
			}
			current_num++;
		}
		
		return primes[primes.length - 1];
	};
	
	var result = find_prime(nth_prime);
	
	// Send back the result
	self.postMessage(result);
	
};

