self.onmessage = function(event){
	
	var frame_data = event.data;
	
	// Get the length of the data, divide that by 4 to get the number of pixels
	// then divide that by 4 again so we check the color of every 4th pixel
	var frame_data_length = (frame_data.length / 4) / 4;
		
	// Loop through the raw image data, adding the rgb of every 4th pixel to rgb_sums
	var pixel_count = 0;
	var rgb_sums = [0, 0, 0];
	for(var i = 0; i < frame_data_length; i += 4){
		rgb_sums[0] += frame_data[i*4];
		rgb_sums[1] += frame_data[i*4+1];
		rgb_sums[2] += frame_data[i*4+2];
		pixel_count++;
	}
	
	// Average the rgb sums to get the average color of the frame in rgb
	rgb_sums[0] = Math.floor(rgb_sums[0]/pixel_count);
	rgb_sums[1] = Math.floor(rgb_sums[1]/pixel_count);
	rgb_sums[2] = Math.floor(rgb_sums[2]/pixel_count);
	
	// Send back the average color
	self.postMessage(rgb_sums);
	
}

