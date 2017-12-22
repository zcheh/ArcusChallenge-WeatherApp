<!DOCTYPE html>
<html>
    <head>
        <title>{{title}}</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <style>
      .bg-1 { 
        background-color: #8a8e99; 
        color: black;
      }
      body, html {
	width: 100%;
        height: 100%;
	background-color: #8a8e99; 
     }
  </style>

    </head>
    <body>
	<div class="container-fluid bg-1 text-center" style="width: 100%; height: 100%">
	% for error in errors:
	 <div class="alert alert-danger">
	  <strong>{{error}}</strong>
	 </div>
        % end
	  {{!base}}
	</div>
    </body>
</html>
