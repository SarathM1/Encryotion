<html>

	<head>
		<script type="text/javascript" src="jquery.js"></script>
		<script type="text/javascript">
			$document.ready(function(){
				var number=10;
				url='';

				function countdown(){
					setTimeout(countdown,1000);
					$('#box').html("Redirecting in"+number+" seconds.");
					number--;
				}
			}


			);

		</script>

	</head>
	
	<body>
		<div id="box"></div>
	</body>
</html>