#
# The config file. Set the important variables here.
#

camera_resolution = (640,480)

fonts = {
		 	'din_black'		:"DINPro-Black",
			'din_bold'		:"DINPro-Bold",
			'din_light'		:"DINPro-Light",
			'din_regular'	:"DINPro-Regular",
			'din_medium'	:"DINPro-Medium",
			'lobster'		:"Lobster 1.4"
		}

positions = {
				'top_left'		:(25, 25),
				'top_center'	:(camera_resolution[0]/2, 25),
				'top_right'		:(camera_resolution[0]-25, 25),
				'middle_left'	:(25, camera_resolution[1]/2),	
				'middle_center'	:(camera_resolution[0]/2, camera_resolution[1]/2),
				'middle_right'	:(camera_resolution[0]-25, camera_resolution[1]/2),
				'bottom_left'	:(25, camera_resolution[1]-25),
				'bottom_center'	:(camera_resolution[0]/2, camera_resolution[1]-25),
				'bottom_right'	:(camera_resolution[0]-25, camera_resolution[1]-25)
			}

colors = {
		 	"white"	:(255,255,255),
			"black"	:(0,0,0),
			"red"	:(255,69,49),
			"green"	:(165,255,49),
			"blue"	:(41,89,214)  
		 }

overlays = 	{
				"Happy"		:"smile.png",
				"Sad"		:"frown.png",
				"Content"	:"content.png",
				"Angry"		:"angry.png",
				"Surprised"	:"surprised.png"
			}

expressions = ["Happy", "Sad", "Surprised", "Content", "Angry"]

# state = 0			