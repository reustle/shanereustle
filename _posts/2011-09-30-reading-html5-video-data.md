---
title: Reading HTML5 Video Data
---

One of the cooler features I've found in HTML5&#39;s new &#60;video&#62; tag is the ability to easily stream its content to a canvas. By passing the video element to the **drawImage** method of a canvas, along with some size parameters, you're able to create a duplicate output of the video. This opens up a whole new set of options for what you can do with your video data. We're going to use it to find the average color of the frame.

Once you have your video piped into a canvas, you can use the **getImageData** method on the canvas to pull the current frame. This will return an ImageData object which includes a CanvasPixelArray list named data. The length of this list is **video_width * video_height * 4**, commonly known as RGBA format. For every pixel there is a red, green, blue and alpha value. By using every pixel on the canvas (or every 4 in our case, to increase speed), we are able to calculate the average color of the frame. In the example below, I set the average frame color as the background at 30fps. You can also see the average frame color listed below the video. You may need to be using Google Chrome or Firefox to see this example.

<div class='text-center'>
	<video id='my_video' height='250' width='600' controls loop>
		<source src='/static/resources/cars2.webm' type='video/webm'/>
	</video>
	<canvas id='my_canvas' style='display:none'></canvas>
	
	<div>
		<div id='current_rgb' class='btn btn-default disabled'>rgb(255,255,255)</div>
		<div id='reset_bg' class='btn btn-default'>Reset</div>
	</div>
</div>

If you take a look at the source code of this page, it should be fairly clear as to how it works. To reiterate, I am playing a video using the new HTML5 &#60;video&#62; tag, which is hidden. I then stream that video data into a canvas, which I read 30 times per second. Every time I read the canvas, I figure out the average color and set that as the background color. In my next blog post, I will work on moving some of these expensive calculations out of the main event loop using web workers.

<script>
	
	// Main elements
	var body = document.getElementsByTagName('body')[0];
	var current_rgb = document.getElementById('current_rgb');
	var my_video = document.getElementById('my_video');
	var my_canvas = document.getElementById('my_canvas');
	var my_canvas_context = my_canvas.getContext('2d');
	
	var update_bg = function(){
		
		// If the video isn't playing, don't loop
		if(my_video.paused || my_video.ended){
			return false;
		}
		
		// Draw the current frame of the video onto the hidden canvas
		my_canvas_context.drawImage(my_video, 0, 0, my_video.width/2, my_video.height/2);
		
		// Pull the image data from the canvas
		var frame_data = my_canvas_context.getImageData(0, 0, my_video.width/2, my_video.height/2).data;
		
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
		
		// Set the background color to the new color
		var new_rgb = 'rgb(' + rgb_sums.join(',') + ')';
		body.style.background = new_rgb;
		
		// Update the rgb label
		current_rgb.innerHTML = new_rgb;
		
		// Repeat every 1/10th of a second
		setTimeout(update_bg, 100);
	}
	
	var init = function(){
		// Update the size of the canvas to match the video
		my_canvas.width = my_video.width/2;
		my_canvas.height = my_video.height/2;
		
		// Start updating the bg color
		update_bg();
	}
	
	my_video.addEventListener('play', init);
	
	document.getElementById('reset_bg').onclick = function(){
		document.getElementsByTagName('body')[0].style.background = '#fff';
	}

</script>

