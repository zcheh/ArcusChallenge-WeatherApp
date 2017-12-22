% rebase('base.tpl')
<div class="container">
<div class="row">
<h2>{{header}}</h2>
  <div class="col-lg-6 col-md-6 col-sm-6 col-lg-offset-3 col-md-offset-3 col-sm-offset-3">
  <form action="/weather" method="post">
    <div class="form-group">
       <input id="address" class="form-control" name="address" type="text" placeholder="City, zip, or place" required>
    </div>
      <input class="btn btn-default btn-block" value="Get Weather" type="submit" />
  </form>
 </div>
</div>
</div>
